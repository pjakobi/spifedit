'''
Created on 4 sept. 2018

@author: Pascal Jakobi
'''
import syslog 

class PrivMark(object):
    '''
    classdocs
    '''


    def __init__(self, fname, privMark):
        '''
        Constructor
        '''
        self.name = privMark.get('name')
        self.obsolete = privMark.get('obsolete')
        if self.obsolete: 
            syslog.syslog(syslog.LOG_DEBUG,_('Privacy Mark for {0}: {1} (obsolete)').format(fname,self.name))
        else:
            syslog.syslog(syslog.LOG_DEBUG,_('Privacy Mark for {0}: {1}').format(fname,self.name))