class DictLast():
    def __init__(self):
        self.lastStack = []
        self.lastDict = dict()

    def set(self, key, val):
        self.lastDict[key] = val
        self.lastStack.append(key)

    def get(self, key):
        if key in self.lastDict:
            self.lastStack.append(key)
            return self.lastDict[key] 

    def last(self):
        return self.lastStack[-1]

    def delete(self, key):
        for i in self.lastStack:
            if key == i:
                self.lastStack.remove(i)
        del self.lastDict[key]


#####################################

# this exercise asks that the "last()" method always return the most recently accessed key in the Dictionary
# if the key is deleted, it's the last key that was read or written

d = DictLast()
d.set('First Name', 'Jim')
print d.last()
print d.get('First Name')
print d.last()
d.set('Last Name', 'Mortko')
print d.last()
d.set('City', 'Sea Cliff')
print d.last()
print d.get('First Name')
print d.last()
d.delete('First Name')
print d.last()

print str(d.lastDict)
print str(d.lastStack)

