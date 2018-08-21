
from xml.dom import minidom
import os
from spif.Classification import Classification
from spif.ObjectId import ObjectId 

class ConfigFile(object):
    '''
    classdocs
    '''

      


    def __init__(self, dirName, fileName):
        '''
        Constructor
        '''
        doc = minidom.parse(os.path.join(dirName,fileName))
        self.fname = os.path.basename(fileName)
        els = doc.getElementsByTagNameNS('*', 'securityPolicyId')
        if els.length != 1: 
            raise ValueError("No security Policy Id or more than one (one exactly expected)")
            
        if els[0].hasAttribute('name'):  self.name = els[0].getAttribute('name')
        else: raise ValueError("No security Policy name (attribute is mandatory)")
        if els[0].hasAttribute('id'):  self.oid = ObjectId(els[0].getAttribute('id'))
        else: raise ValueError("No security Policy Object Id (attribute is mandatory)")
        '''
        Retrieve security classifications
        '''
        self.classifications = []
        for x in doc.getElementsByTagNameNS('*', 'securityClassification'):
            myDict = {}
            if x.hasAttribute('name'): myDict['name'] = x.getAttribute('name')
            if x.hasAttribute('lacv'): myDict['lacv'] = x.getAttribute('lacv')
            if x.hasAttribute('hierarchy'): myDict['hierarchy'] = x.getAttribute('hierarchy')            
            self.classifications.append(Classification(myDict))
    
    def getOid(self):
        return self.oid
    
    def getFile(self):
        return self.fname
    
    def getName(self):
        return self.name
    
    def getClassifications(self):
        return self.classifications
    
    def delClassification(self,classif):
        for item in self.classifications:
            if item.name.lower() == classif.lower(): # found
                self.classifications.remove(item)
                return
# Log error : "Trying to delete a non existant classification : {0}/{1}".format(self.oid,classif)
        
    def getInfo(self,selected=False):
        returnValue={}
        returnValue['oid'] = str(self.getOid())
        returnValue['fname'] = self.getFile()
        returnValue['name'] = self.getName()
        returnValue['selected'] = selected
        return returnValue
    
    def __str__(self):
        result = "Config. file: {0} ({1}) - {2}\n".format(self.name,self.fname,str(self.oid))
        for index in self.classifications: result += "{0}\n".format(str(index))
        return result
    

        