/**
 * 
 */
var serverHost = "http://x841.home:5000/";
var urlClassifs = serverHost + "v1/classifications/";
var xmlhttp = new XMLHttpRequest();


// add "<td class=htmlclass>data</td>"
function addClassifCell(htmlclass, row) {
	var td = document.createElement('td');
	td.class = htmlclass;
	td.append(row);
	return td;
} // addClassifCell

//Change classification Button
function AddChangeButton(name,tr) {
	var td = document.createElement('td');
	td.class = 'chgClassifButtons';
	tr.append(td);
	
	var button = document.createElement('input');
	button.type = 'button';
	button.className = 'chgClassifButton';
	button.id = name;
	button.value = 'Change';
	button.onclick='Change_Ligne_Classif(this)';
//	button.attr('alt') = 'Change';
	td.append(button);
}

// Delete classification Button
function AddDeleteButton(name,tr) {
	var td = document.createElement('td');
	td.class = 'delClassifButtons';
	tr.append(td);
	
	var button = document.createElement('input');
	button.type = 'button';
	button.id = name;
	button.className = 'delClassifButton';
	button.value = 'Delete';
	button.onclick='Delete_Ligne_Classif(this)';
//	button.attr('alt') = 'Delete';
	td.append(button);
	
} // AddDeleteButton

// Add a classification row in tableClassifs
function addClassifRow(data) {
	// Add row
	var tr = document.createElement('tr');
	tr.setAttribute("id","trClassifs");
	document.getElementById("tbodyClassifs").append(tr);
	
	// Add delete & change buttons
	AddDeleteButton(data.name,tr);
	AddChangeButton(data.name,tr);
	
	
	// Add data cells (td) in row
	var tdName = document.createElement('td');
	tdName.className = 'name';
	tdName.innerHTML = data.name;
	tr.append(tdName);
	
	var tdHier = document.createElement('td');
	tdHier.className = 'hierarchy';
	var inHier = document.createElement('input');
	inHier.id = data.name;
	inHier.className = 'hierarchyInput';
	inHier.type = 'number';
	inHier.value = data.hierarchy;
	tdHier.append(inHier);
	tr.append(tdHier);
	
	tdLacv = document.createElement('td');
	tdLacv.className = 'lacv';
	var inLacv = document.createElement('input');
	inLacv.id = data.name;
	inLacv.className = 'lacvInput';
	inLacv.type = 'number';
	inLacv.value = data.lacv;
	tdLacv.append(inLacv);
	tr.append(tdLacv);
} // addClassifRow


// Callback when classifications JSON received
function classifications(resp) {
	var arr = JSON.parse(resp);
	var tbody = document.getElementById('tbodyClassifs');
	
	while (tbody.firstChild) tbody.removeChild(tbody.firstChild); // Remove all table rows
	for(var i = 0; i < arr.length; i++) // Add classifications from selected spif
		addClassifRow(arr[i]); 
} // classifications

// Callback when policy is selected
function policySelect(val) {
	var spifChoice = document.getElementById("spifChoice").selectedIndex;
	var oid = document.getElementById("spifChoice").options[spifChoice].value;
	var targetUrl = urlClassifs + oid; // http://server/v1/classifications/<oid>

	document.getElementById("tbodyClassifs").innerHTML = "";
	document.getElementById("errorMsg").innerHTML = "&nbsp;";
	xmlhttp.onreadystatechange=function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        classifications(xmlhttp.responseText);
	    }
	}
	xmlhttp.open("GET", targetUrl, true);
	xmlhttp.send();
} // policySelect

// Check some data (input field) has been entered (field is not empty) - shorthand
function check_data_provided(str,inLabel) {
	if (str.length > 0) return true; // OK
	document.getElementById("errorMsg").innerHTML = inLabel;
	return false; // NOK
} // check_data_provided

// Set Error message - shorthand
function errorMsg(label) {
	document.getElementById("errorMsg").innerHTML = label;
} // errorMsg


// Check some data (input field) is duplicate against a row - shorthand
function check_data_duplicate(str,className,inLabel) {
	// Get all "td class="className" nodes
	var cells = document.getElementsByClassName(className);
	for (var i=0; i < cells.length; i++) {
		if (cells[i].tagName != 'TD') continue; // just check table cells
    	if (str.toUpperCase() == cells[i].innerHTML.toUpperCase()) {
    		errorMsg(inLabel);
    		return false; // NOK
    	} // if
    } // for cells
	return true; // OK (no duplicate found)
} // check_data_duplicate


// Callback for the "Add classification" button
function Create_Ligne_Add_Classif() {
	var form = document.getElementById("formClassif");
	var name = document.getElementById("formClassif").name.value;
	var lacv = document.getElementById("formClassif").lacv.value;
	var hierarchy = document.getElementById("formClassif").hierarchy.value;
	var choice = document.getElementById("spifChoice").selectedIndex;
	var oid = document.getElementById("spifChoice").options[choice].value;
	var targetUrl = serverHost + "v1/classifications/" + oid;
	
	if (!check_data_provided(name,"Error: classification name is mandatory")) return; // NOK - empty names not allowed
	if (!check_data_duplicate(name, "name","Error: duplicate classification name")) return; // NOK - duplicate name
	if (!check_data_provided(hierarchy.toString(),"Error: hierarchy level is mandatory")) return; // NOK
	if (!check_data_duplicate(hierarchy.toString(),"hierarchy", "Error: duplicate hierarchy level")) return; // NOK
	if (!check_data_provided(lacv.toString(),"Error: Label & Cert. Value is mandatory")) return; // NOK
	if (!check_data_duplicate(lacv.toString(),"lacv", "Error: duplicate Label & Cert. Value")) return; // NOK
	errorMsg("&nbsp;");

	document.getElementById('formClassif').action = targetUrl;
	document.forms['formClassif'].submit();

} // Create_Ligne_Add_Classif



//Callback for the "Change classification" button
function Change_Ligne_Classif(elmt) {
	// Build target URL
	var choice = document.getElementById("spifChoice").selectedIndex;
	var oid = document.getElementById("spifChoice").options[choice].value;
	var classif = elmt.getAttribute('id');
	var targetUrl = serverHost + "v1/classifications/" + oid + "/" + classif;
	
	// Retrieve hierarchy & LACV
	var inputs = document.getElementById('tbodyClassifs').getElementsByTagName("input");
	var hierarchy;
	var lacv;
	for (var i=0; i < inputs.length; i++) {
		if ((inputs[i].id == classif) && (inputs[i].className == 'hierarchyInput')) hierarchy = inputs[i].value;
		if ((inputs[i].id == classif) && (inputs[i].className == 'lacvInput')) lacv = inputs[i].value;	
	} // for
	if (lacv == undefined) {
		errorMsg("Error: no label & certificate value");
		return;
	}
	if (hierarchy == undefined) {
		errorMsg("Error: no hierarchy");
		return;
	}
	
	// Send to server
	targetUrl += ('?' + 'hierarchy=' + hierarchy + '&' + 'lacv=' + lacv);
	xmlhttp.onreadystatechange=function() {
	    if (xmlhttp.readyState == 4) {
	    	if (xmlhttp.status == 200) classification_changed();
	    	else {
	    		errorMsg("Error: " + xmlhttp.statusText); // should not happen
	    		return;
	    	}
	    } // readyState == 4
	}
	xmlhttp.open("POST", targetUrl, true);
	xmlhttp.send();
} // Change_Ligne_Classif

// Return function (after change on server) for the change classification operation
function classification_changed() {
	errorMsg('&nbsp;');
} // classification_changed

//Callback for the "Delete classification" button
function Delete_Ligne_Classif(elmt) {
	console.log("Delete")
	var choice = document.getElementById("spifChoice").selectedIndex;
	var oid = document.getElementById("spifChoice").options[choice].value;
	var classif = elmt.getAttribute('id');
	var targetUrl = serverHost + "v1/classifications/" + oid + "/" + classif;
	xmlhttp.onreadystatechange=function() {
	    if (xmlhttp.readyState == 4) {
	    	if (xmlhttp.status == 200) classification_deleted(oid, classif);
	    	else {
	    		errorMsg("Error: " + xmlhttp.statusText); // should not happen
	    		return;
	    	}
	    } // readyState == 4
	}
	xmlhttp.open("DELETE", targetUrl, true);
	xmlhttp.send();

} // Delete_Ligne_Classif

// Return function (after deletion on server) for the delete classification operation
function classification_deleted(oid, classif) {
	errorMsg("&nbsp;"); // erase message
	// erase line in web page
	var x = document.getElementsByTagName("p");
	var inputs = document.getElementById('tbodyClassifs').getElementsByTagName("input");
	for (var i=0; i < inputs.length; i++) {
		if ((inputs[i].id == classif) && (inputs[i].className == 'delClassifButton')) {
			var row = inputs[i].parentNode.parentNode;
			row.parentNode.removeChild(row);
			return;
		}  // if
	} // for
	console.log("Internal Error. Classification not deleted :" + classif);
} // classification_deleted