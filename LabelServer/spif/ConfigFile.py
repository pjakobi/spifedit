
from xml.dom import minidom
import os
from spif.Classification import Classification
from spif.ObjectId import ObjectId 
import syslog
import gettext
# import xmlspif
# import pyxb
import sys
import spifDS
from TagSet import TagSet
from Tag import Tag
from flask import current_app as app
from PrivMark import PrivMark
import xml.etree.ElementTree as ET

class ConfigFile(object):
    '''
    classdocs
    '''

    def __init__(self, fileName, nameSpace):
        '''
        Constructor
        '''
        
        global app;
        
        syslog.syslog(syslog.LOG_DEBUG,_('SPIF: {0} - {1}').format(os.path.basename(fileName),''))
#       doc = minidom.parse(os.path.join(dirName,fileName))
        self.fname = os.path.basename(fileName)
     
#       try: spifFile= xmlspif.CreateFromDocument(open(os.path.join(dirName,fileName)).read())
#       except pyxb.ValidationError as e:
#            print e.details()
#            raise ValueError('Invalid XML document {0}'.format(fileName))
        
        spifFile = spifDS.parsexml_(fileName)
        rootNode = spifFile.getroot()
        
        
        # Name & Object Id are mandatory in the XSD
        if len(rootNode.findall(nameSpace + 'securityPolicyId')) != 1:
            syslog.syslog(syslog.LOG_NOTICE,_('Invalid XML document {0}'.format(fileName)))
            return
                    
        policyId = rootNode.find(nameSpace + 'securityPolicyId')
        self.oid = policyId.attrib['id']
        self.name = policyId.attrib['name']
        syslog.syslog(syslog.LOG_DEBUG,_('SPIF oid for {0}: {1}').format(os.path.basename(fileName),self.oid))
        
        '''
        Retrieve security classifications
        '''
        self.classifications = []
        for classifs in rootNode.iter(nameSpace + 'securityClassification'):
            self.classifications.append(Classification(classifs,self.oid))

        '''
        Retrieve privacy marks
        '''
        self.privMarks  = []
        for privMark in rootNode.iter(nameSpace + 'privacyMark'):
            self.privMarks.append(PrivMark(self.fname, privMark))
        
                 
        '''
        Retrieve tags
        '''
        self.tagSets  = [] 
        for index in rootNode.iter(nameSpace + 'securityCategoryTagSet'):
            self.tagSets.append(TagSet(index, self.fname, nameSpace))
            for index2 in index.iter(nameSpace + 'securityCategoryTag'):
                tag = Tag(index2, self.fname, nameSpace)
    
    def getOid(self):
        return self.oid
    
    def getFile(self):
        return self.fname
    
    def getName(self):
        return self.name
    
    def getClassifications(self):
        return self.classifications
    
    def getClassification(self, classif):
        for item in self.classifications:
            if classif == item.name: return item
            # Classification not found
        raise ValueError(_("Invalid classification {0} - object id {1}").format(classif.name,self.oid))
    
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
        result = _("Config. file: {0} ({1}) - {2}\n").format(self.name,self.fname,str(self.oid))
        for index in self.classifications: result += "{0}\n".format(str(index))
        return result
    

        