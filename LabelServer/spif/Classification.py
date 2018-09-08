import gettext
import syslog

class Classification(object):
    def __init__(self, classif, oid): # name, hierarchy, lacv
        
        if classif.get('name') is None : raise SyntaxError(_('Internal error : Classification has no name')) # should not happen
        
        self.name = classif.get('name')
        if classif.get('hierarchy') is not None: self.hierarchy = classif.get('hierarchy')
        else: self.hierarchy = -1 # Should not happen (xsd)
        if classif.get('lacv') is not None: self.lacv = classif.get('lacv')
        else: self.lacv = -1 # Should not happen (xsd)
        syslog.syslog(syslog.LOG_DEBUG,_('Classification for oid {0}: {1} (h:{2}-lacv:{3})').format(oid,self.name,self.hierarchy,self.lacv))
        
    def __str__(self):
        return _("Classification : {0} - ({1}, {2})").format(self.name,self.hierarchy,self.lacv)   
    
    def setLacv(self, lacv):
        self.lacv = lacv 
        
    def setHierarchy(self, hierarchy):
        self.hierarchy = hierarchy
    
    def getName(self):
        return self.name
        
    def getLacv(self):
        return self.lacv
    
    def getHierarchy(self):
        return self.hierarchy
    