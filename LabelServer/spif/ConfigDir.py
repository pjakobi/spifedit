

import os
import gettext
from spif.ConfigFile import ConfigFile
import syslog

class ConfigDir(object):
    '''
    classdocs
    '''
# Object init - contains a list of objects (individual config files)
    def __init__(self, dirName,nameSpace):
        syslog.syslog(syslog.LOG_DEBUG,_('SPIF Directory: {0}').format(dirName))
        self.directory = dirName
        self.files = []
        for name in os.listdir(dirName):
            if os.path.isfile(os.path.join(dirName,name)) and name.endswith('.spif'): 
                self.files.append(ConfigFile(os.path.join(dirName,name),nameSpace))
        if len(self.files) < 1: # No file in Directory
            raise ValueError(_("No policy file in Directory. Correct /etc/x841.yaml."))
                    
# Returns the file name for a given Object Id                    
    def findOid(self,oid):
        for spif in self.files:
            if str(spif.getOid()) == str(oid):  return spif
        raise ValueError(_("Unknown object id requested"))
                              
# Return a list of (oid + name + file name)
    def getInfo(self,oid):
        result = []
        for x in self.files:
            if oid is None: selected = False
            else:
                if x.getOid() == oid: selected = True
                else:  selected = False
            result.append(x.getInfo(selected))
        return result

    def __str__(self):
        result = _("ConfigFiles : {0}\n").format(self.directory)
        for index in self.files: result += "{0}\n".format(str(index))
        return result

    def getConfigFile(self,oid):
        for x in self.files: 
            if oid == str(x.getOid()): return x
        return None
    
    def findIndex(self,oid): 
        for index in self.files:
            if oid == index.getOid(): return index.keys()
        raise IndexError(_("Unknown object id requested (pls report bug)"))
