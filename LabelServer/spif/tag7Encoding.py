'''
Created on 8 sept. 2018

@author: Pascal Jakobi
'''
from enum import Enum
import syslog

class Tag7Encoding(Enum):
    '''
    Encoding - can only have 2 values : "bitSetAttributes", "securityAttributes"
    '''
    bitsSetsAttr = 1
    securityAttributes = 2

    def __init__(self, fname, value):
        '''
        Constructor
        '''
        self.fname = fname
        if value.lower() == "bitSetAttributes".lower(): self.value = Tag7Encoding.bitsSetsAttr
        elif value.lower() == "securityAttributes".lower(): self.value = Tag7Encoding.securityAttributes
        else: 
            syslog.syslog(syslog.LOG_WARNING,_('{0} : invalid tag encoding: {1}').format(fname,value))
            return None
    
    def __str__(self):
        if self.value == Tag7Encoding.bitsSetsAttr: return _("bitSetAttributes")
        elif self.value == Tag7Encoding.securityAttributes: return _("securityAttributes")
        else: 
            syslog.syslog(syslog.LOG_WARNING,_('{0} : unknown tag encoding: {1}').format(self.fname,self.value))
            return ''