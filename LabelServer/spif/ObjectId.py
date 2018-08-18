
class ObjectId(object):
    '''
    All operations related to object ids
    '''


    def __init__(self, oid):
        '''
        Check that oid is valid : [num.]*
        '''
        self.oid = oid.split(".")
        for field in self.oid: 
            if field.isdigit(): return
        raise ValueError("Invalid object id {0} - only numbers separated with dots".format(oid))
    
    def __str__(self): # return a.b.c.d.e...
        return ".".join(self.oid)    