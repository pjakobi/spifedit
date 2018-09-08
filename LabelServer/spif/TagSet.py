'''
Created on 1 sept. 2018

@author: Pascal Jakobi
'''
from ObjectId import ObjectId
from Tag import Tag
import syslog

class TagSet(object):
    '''
    Handles X.841 Tag Sets
    '''
    
    def __init__(self, tagSet, fname, nameSpace):
        '''
        Constructor
        '''
        if tagSet.get('name') is None : raise SyntaxError(_('Category tag set has no name - {0}').format(fname)) # should not happen
        
        self.tags  = []
        self.fname = fname
        self.name = tagSet.get('name')
        self.oid = ObjectId(tagSet.get('id'))
        syslog.syslog(syslog.LOG_DEBUG,self.__str__())
        tags = tagSet.find(nameSpace + 'securityCategoryTag')
        if tags is not None :
            for index in tags.findall(nameSpace + 'securityCategoryTag'):
                self.tags.append(Tag(index, self.fname, nameSpace))
                
                
    def __str__(self):
        result = _("Security category tags set for {0}: {1} - {2}\n").format(self.fname,self.name,str(self.oid))
        return result