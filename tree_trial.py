
# Using trees from: http://cbio.ufs.ac.za/live_docs/nbn_tut/trees.html

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)

        return ret

val1 = True
val2 = False

class exprnode(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self, level=0):
        ret = " "*(4*level)+("^--")+repr(self.value)+"\n"
        if self.left is not None:
            ret += self.left.__repr__(level+1)
        if self.right is not None:
            ret += self.right.__repr__(level+1)

        return ret

    def evaluate(self):
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == '/':
            return self.left.evaluate() / self.right.evaluate()

        #Boolean Logic
        elif self.value == '&':
            return self.left.evaluate() & self.right.evaluate()
        elif self.value == '|':
            return self.left.evaluate() | self.right.evaluate()
        elif self.value == '!':
            return not self.left.evaluate()
        else:
            return self.value

expr1 = exprnode('!', 
                 exprnode(val1))

expr2 = exprnode('|',
                 exprnode('&',
                          exprnode('&',
                                   exprnode(val1),
                                   exprnode(val2)),
                          exprnode('|',
                                   exprnode(val2),
                                   exprnode('&',
                                            exprnode(val1),
                                            exprnode('|',
                                                     exprnode(val2),
                                                     exprnode(val1))))),
                 exprnode('&',
                          exprnode(val1),
                          exprnode(val2)))


my_expr_and = exprnode('&',
    exprnode(val1),
    exprnode(val2))

my_expr_or = exprnode('|',
    exprnode('!',
        exprnode('&',
            exprnode(val1),
            exprnode(val2))),
    exprnode(val2))

my_expr_not = exprnode('!',
    exprnode(val1))

sep_str = "\n*------------------------*\n"
equiv = "\t\t= "

def main():

    print "\nval1 = %s\nval2 = %s" % (val1, val2)
    print sep_str
    print expr2.evaluate(), '\n', expr2
    
    return True

if __name__ == '__main__':
    main()
