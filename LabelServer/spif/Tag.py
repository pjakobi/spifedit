'''
Created on 4 sept. 2018

@author:  Pascal Jakobi
'''
import syslog
from TagType import TagType
from Tag7Encoding import Tag7Encoding
class Tag(object):
    '''
    classdocs
    '''


    def __init__(self, tag, fname, nameSpace):
        '''
        Constructor
          <xs:complexType name="securityCategoryTag">
            <xs:sequence>
              <xs:element ref="tagCategory" minOccurs="0" maxOccurs="unbounded" />
              <xs:element ref="markingQualifier" minOccurs="0" maxOccurs="unbounded" />
            </xs:sequence>
            <xs:attribute name="name" type="xs:string" />
            <xs:attribute name="tagType" type="tagType" use="required" />
            <xs:attribute name="enumType" type="enumType" />
            <xs:attribute name="tag7Encoding" type="tag7Encoding" />
            <xs:attribute name="singleSelection" type="xs:boolean" default="false" />
            <xs:anyAttribute />
          </xs:complexType>
        '''
        if tag.get('name') is None : 
            raise SyntaxError(_('Category tag has no name - {0}').format(fname)) # should not happen
        self.fname = fname
        self.name = tag.get('name')
     
            
        if tag.get('tagType') is not None: 
            tagType = TagType(fname,tag.get('tagType'))
            if tagType is not None: self.tagType = tagType.value
        
        if tag.get('tag7Encoding') is not None: 
            tag7Encoding = Tag7Encoding(fname, tag.get('tag7Encoding'))
            if tag7Encoding  is not None: self.tag7Encoding = tag7Encoding.value
        
        if (tag.get('singleSelection') is not None) and (tag.get('singleSelection') == True): 
            self.singleSelection = True
        
        if tag.get('enumType') is not None: self.enumType = tag.get('enumType')

        if (hasattr(self,'tagType')): singleSelection = ','
        if (hasattr(self,'singleSelection')): singleSelection = 'Single selection,'
        else: singleSelection = ''
        print "Tag : {0} - {1}, Encoding: {2} {3}".format(
            self.name,
            self.tagType,
            self.tag7Encoding if (hasattr(self,'tag7Encoding')) else '',
            singleSelection
            )
        syslog.syslog(syslog.LOG_DEBUG,self.__str__())
            
    def __str__(self):
        result = _("Security category tag ({1}) : {0} -  {2}\n").format(self.name,self.fname,self.tagType)
        return result