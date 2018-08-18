# serve.py
import yaml
import json
import sys
import glob

from flask import Flask, Response  
from flask import render_template
from flask import session
from flask import request,redirect, url_for 
from flask.helpers import make_response

from spif.ConfigDir import ConfigDir
from spif.ConfigFile import ConfigFile

import logging
import logging.handlers
from logging import config


from spif.ObjectId import ObjectId 
from spif.Classification import Classification
from pyanaconda.ui.gui.spokes.lib.custom_storage_helpers import selectedRaidLevel

# creates a Flask application, named app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SPIFedit'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CONFIG_FILE'] = '/etc/x841/spifedit.yml'
app.config['LOGCFG_FILE'] = '/etc/x841/logging.yml'
app.config['CONFIG_DIRECTORY'] = None
app.config['LOGGER'] = None

directoryName = None
configFiles = []
configDirectory = None




def jsonDefault(object):
    return object.__dict__

def loadConfig():
    global directoryName
    global configFiles
    global configDirectory
    
    # First of all, configure logging
    logger = logging.getLogger('spifedit')
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.SysLogHandler(address = '/dev/log', facility='local6')
    logger.addHandler(handler)
    app.config['LOGGER'] = logger
    app.config['LOGGER'].debug("Syslog configuration loaded")

    
    # Then configure application
    configDict=yaml.load(open(app.config['CONFIG_FILE']))
    if not configDict.has_key('spif config'):
        app.config['LOGGER'].error("spif_config not set in /etc/x841/spifedit.yml. Application aborted.")
        raise ValueError("spif_config not set in /etc/x841/spifedit.yml. Please fix.")
    directoryName = configDict['spif config'] # Directory where the SPIF are stored
    configFiles = glob.glob(directoryName + "/*.spif")
    configDirectory = ConfigDir(directoryName)
    app.config['LOGGER'].debug("{0} configuration loaded".format("SPIFedit"))
    
    return configDict

# Shorthand
def logIndexPage(items,classifs,selection):
    if app.config['LOGGER'].level != logging.DEBUG: return
    for x in items: 
        current = str(x['oid'])
        if str(selection) == current: myChoice = " - {3}".format(selection)
        else : myChoice = ""
        app.config['LOGGER'].debug("SPIF : {0}({1}) : {2} {3}".format(x['name'],x['fname'],x['oid'], myChoice))
    for y in classifs: 
        app.config['LOGGER'].debug("{0}".format(str(y)))
    

# Init page
@app.route("/", methods=['GET'])
def showDefault(): 
    myOid = configDirectory.files[0].oid
    app.config['LOGGER'].info("showDefault oid {0}".format(str(myOid)))
    selected = configDirectory.files[0].oid
    app.config['LOGGER'].debug("Selected : {0}".format(selected))
    info = configDirectory.getInfo(myOid)
    classifs = configDirectory.files[0].getClassifications()
#    logIndexPage(info,classifs,selected)
    return render_template('index.html', items=info, classifs=classifs, selected=selected)

# Return SPIF related data
@app.route('/v1/classifications/<oid>', methods=['GET'])
def showOid(oid):
    app.config['LOGGER'].info("showOid : show classifications for oid {0}".format(oid))
    classifs = configDirectory.findOid(ObjectId(oid)).getClassifications()
    jsonClassifs = json.dumps(classifs, default=jsonDefault)
    if app.config['LOGGER'].level == logging.DEBUG:
        for y in classifs: app.config['LOGGER'].debug("{0}".format(str(y)))
    resp = Response(response=jsonClassifs,status=200,mimetype="application/json")
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

# Add a classification for a given SPIF (using its object id)
@app.route('/v1/classifications/<oid>', methods=['POST'])
def addClassifications(oid):
    app.config['LOGGER'].info("Adding classification for oid {0}".format(oid))
    # Fill a dictionary
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    
    # Check request
    myDict = {}
    try: myDict['name'] = request.form['name']
    except KeyError: raise KeyError("Error : unnamed classification")
    try: myDict['hierarchy'] = request.form['hierarchy']
    except KeyError: raise KeyError("Error : no hierarchy in request")
    try: myDict['lacv'] = request.form['lacv']
    except KeyError: raise KeyError("Error : no lacv in request")

    # Find SPIF & add classification
    confFile = configDirectory.getConfigFile(oid)
    if confFile == None: 
        return (Response("Unknown SPIF/object id",code=404)) 
    
    classif = Classification(myDict)
    confFile.classifications.append(classif)
    app.config['LOGGER'].debug("Added classification {0}".format(classif.name))

    selected = str(oid)
    info = configDirectory.getInfo(oid)
    classifs = configDirectory.findOid(ObjectId(oid)).getClassifications()
    logIndexPage(info,classifs,selected)
    return render_template('index.html', items=info, classifs=classifs, selected=selected)

# run the application
if __name__ == "__main__": 
    configDict = loadConfig() 
    app.config['LOGGER'].info("Application start")
    

    app.run(debug=True)
