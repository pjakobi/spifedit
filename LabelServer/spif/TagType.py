'''
Created on 7 sept. 2018

@author:  Pascal Jakobi



        Possible tag types :
        . notApplicable - not applicable</li>
        . restrictive - bit set of tag categories where all of the selected tag categories are required in the security clearance.
        . enumerated - integer set of tag categories, with tag further refined by the enumType.
        . permissive - bit set of tag categories where at least one of the selected tag categories are required in the security clearance</li>
        . tagType7 - informative
        Tag types are required.
        '''   
import syslog

class TagType(object):
    def __init__(self, fname, tagType):
        '''
        Tag type has a defined set of values as per xsd.
        '''
        if tagType.lower() == 'notApplicable'.lower(): self.value = 'notApplicable'
        elif tagType.lower() == 'restrictive'.lower(): self.value = 'restrictive'
        elif tagType.lower() == 'enumerated'.lower(): self.value = 'enumerated'
        elif tagType.lower() == 'permissive'.lower(): self.value = 'permissive'
        elif tagType.lower() == 'tagType7'.lower(): self.value = 'tagType7'
        else: 
            syslog.syslog(syslog.LOG_WARNING,_('{0} : invalid tag type: {1}').format(fname,tagType))
            return None
    
    def get(self):
        return self.value