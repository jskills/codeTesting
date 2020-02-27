class Stack:
        def __init__(self, data=None, above=None, isBase=0):
                self.data = data
                self.above = above
                self.isBase = isBase

        def push(self, val):
                if self.above:
                        self.above.push(val)
                else:
                        self.above = Stack(val)

        def pop(self, below=None):
                if self.above:
                        return self.above.pop(below=self)
                else:
                        returnVal = self.data
                        if below:
                                below.above = None
                        else:
                                self.data = None
                        return returnVal

def parsePostfix(eval_me):
        s = Stack()
        result = ''
        eList = eval_me.split(' ')
        for el in eList:
                if el.isnumeric():
                        s.push(el)
                else:
                        op2 = int(s.pop())
                        op1 = int(s.pop())
                        if el == '+':
                                result = op1 + op2
                        elif el == '-':
                                result = op1 - op2
                        elif el == '×':
                                result = op1 * op2
                        elif el == '÷':
                                result = op1 / op2
                        s.push(result)
        result = s.pop()
        return result





##########################################


s = Stack(5)
s.push(6)
s.push(7)
s.push(9)
s.push(11)
print( str(s.pop()) )
s.push(55)
print( str(s.pop()) )
print( str(s.pop()) )
s.push('j')
print( str(s.pop()) )
print( str(s.pop()) )

postfixStr = '15 7 1 1 + - ÷ 3 × 2 1 1 + + -'
r = parsePostfix(postfixStr)
print('The result of : ' + postfixStr + ' is ' + str(r))
