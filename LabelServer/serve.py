# serve.py
import gi
from cookielib import logger
gi.require_version("Gtk", "3.0")
import os
import yaml
import json
import sys
import glob
import syslog

from flask import Flask, Response  
from flask import render_template
from flask import session
from flask import request,redirect, url_for 
from flask.helpers import make_response

from spif.ConfigDir import ConfigDir
from spif.ConfigFile import ConfigFile

#import logging
#import logging.handlers
#from logging import config
#from logging.handlers import SysLogHandler


from spif.ObjectId import ObjectId 
from spif.Classification import Classification


# creates a Flask application, named app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SPIFedit'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CONFIG_FILE'] = '/etc/x841/spifedit.yml'
app.config['CONFIG_DIRECTORY'] = '/opt/x841/spifedit'

configDir = None

def jsonDefault(object):
    return object.__dict__

def loadConfig():
    global configDir
    
    # if config. directory or file does not exist, load default values
    if os.path.exists(app.config['CONFIG_FILE']): 
        configDict=yaml.load(open(app.config['CONFIG_FILE']))
        if not configDict.has_key('Log level'): configDict['Log level'] = syslog.LOG_INFO
        if not configDict.has_key('spif facility'): configDict['spif facility'] = syslog.LOG_LOCAL5
        if configDict.has_key('spif config'): app.config['CONFIG_DIRECTORY'] = configDict['spif config']
        else: 
            syslog.syslog(syslog.LOG_WARNING,'spif_config not set in /etc/x841/spifedit.yml. Using {0}.'.format(app.config['CONFIG_DIRECTORY']))
    else: 
        configDict = {}
        configDict['spif facility'] = syslog.LOG_LOCAL5
        configDict['Log level'] = syslog.LOG_INFO
    
    # First of all, configure logging
    syslog.setlogmask(syslog.LOG_UPTO(int(configDict['Log level'])))
    syslog.openlog("SPIFedit",0, configDict['spif facility'])
    syslog.syslog(syslog.LOG_NOTICE, 'Service started')
    
    # Then configure application
    configDir = ConfigDir(app.config['CONFIG_DIRECTORY'])
    configFiles = glob.glob(configDict['spif config'] + "/*.spif")
    syslog.syslog(syslog.LOG_INFO, 'Configuration loaded'.format(''))
    
    return configDict

   

# Init page
@app.route("/", methods=['GET'])
def showDefault(): 
    syslog.syslog(syslog.LOG_INFO, 'Web app started'.format(''))
    myOid = configDir.files[0].oid
    selected = configDir.files[0].oid
    syslog.syslog(syslog.LOG_DEBUG, 'showDefault oid {0} - selected {1}'.format(str(myOid),selected))
    info = configDir.getInfo(myOid)
    classifs = configDir.files[0].getClassifications()
    return render_template('spifedit.html', items=info, classifs=classifs, selected=selected)

# Return SPIF related data
@app.route('/v1/classifications/<oid>', methods=['GET'])
def showOid(oid):
    syslog.syslog(syslog.LOG_INFO, 'showOid : show classifications for oid {0}'.format(oid))
    classifs = configDir.findOid(ObjectId(oid)).getClassifications()
    jsonClassifs = json.dumps(classifs, default=jsonDefault)
    resp = Response(response=jsonClassifs,status=200,mimetype="application/json")
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

# Add a classification for a given SPIF (using its object id)
@app.route('/v1/classifications/<oid>/<classif>', methods=['POST'])
def changeClassifications(oid,classif):
    syslog.syslog(syslog.LOG_INFO,'DEBUG : Changing classification {1} for oid {0}'.format(oid, classif))
    classifObject = configDir.findOid(ObjectId(oid)).getClassification(classif)
    oldHierarchy = classifObject.getHierarchy()
    oldLacv = classifObject.getLacv()
    if request.args.get("hierarchy") != None: classifObject.setHierarchy(request.args.get("hierarchy"))  
    if request.args.get("lacv") != None: classifObject.setLacv(request.args.get("lacv"))  
    syslog.syslog(syslog.LOG_DEBUG, 'Hierarchy set from {0} to {1}, LACV set from {2} to {3}'.format(oldHierarchy, classifObject.getHierarchy(),oldLacv, classifObject.getLacv()))
    resp = Response(status=200)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

# Add a classification for a given SPIF (using its object id)
@app.route('/v1/classifications/<oid>', methods=['POST'])
def addClassifications(oid):
    if 'name' in request.form.keys(): cname = request.form['name']
    else: cname = '???'
    syslog.syslog(syslog.LOG_INFO, "Adding classification {1} for oid {0}".format(oid, cname))
    
    # Fill a dictionary
    myDict = {}
    try: myDict['name'] = request.form['name']
    except KeyError: raise KeyError("Error : unnamed classification")
    try: myDict['hierarchy'] = request.form['hierarchy']
    except KeyError: raise KeyError("Error : no hierarchy in request")
    try: myDict['lacv'] = request.form['lacv']
    except KeyError: raise KeyError("Error : no lacv in request")

    # Find SPIF & add classification
    confFile = configDir.getConfigFile(oid)
    if confFile == None: return (Response("Unknown SPIF/object id",code=404)) 
    
    classif = Classification(myDict)
    confFile.classifications.append(classif)
    syslog.syslog(syslog.LOG_DEBUG, 'Added classification {0}/{1} (h:{2},l:{3})'.format(oid,classif.getName(),classif.getHierarchy(),classif.getLacv()))

    selected = str(oid)
    info = configDir.getInfo(oid)
    classifs = configDir.findOid(ObjectId(oid)).getClassifications()
    return render_template('spifedit.html', items=info, classifs=classifs, selected=selected)

# Delete a classification for a given SPIF (using its object id and classification name)
@app.route('/v1/classifications/<oid>/<classif>', methods=['DELETE'])
def delClassifications(oid,classif):
    syslog.syslog(syslog.LOG_INFO, "Deleting classification {1} for oid {0}".format(oid, classif))
    
    confFile = configDir.getConfigFile(oid)
    if confFile == None: return (Response("Unknown SPIF/object id",code=404))
    confFile.delClassification(classif)
    syslog.syslog(syslog.LOG_DEBUG, 'Deleted classification {0}'.format(classif))
    
    classifs = configDir.findOid(ObjectId(oid)).getClassifications()
    info = configDir.getInfo(oid)
    selected = str(oid)
    return render_template('spifedit.html', items=info, classifs=classifs, selected=selected)

# run the application
if __name__ == "__main__":  
    configDict = loadConfig() 
    app.run(debug=True)
