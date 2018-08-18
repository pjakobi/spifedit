
class Classification(object):
    def __init__(self, classifDict): # name, hierarchy, lacv
        if not ('name' in classifDict): raise SyntaxError('Classification has no name') # should not happen

        self.name = classifDict['name']
        if ('hierarchy' in classifDict): self.hierarchy = classifDict['hierarchy']
        else: self.hierarchy =  -1
        if ('lacv' in classifDict): self.lacv = classifDict['lacv']
        else: self.lacv = -1
        
    def __str__(self):
        return "Classification : {0} - ({1}, {2})".format(self.name,self.hierarchy,self.lacv)      