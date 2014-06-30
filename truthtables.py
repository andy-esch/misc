'''
truthtables.py
This script turns a logical expression written in the form a,b,c,... = T/F (binary) 
variable, and & = AND, v = OR, ~ = NOT, X = XOR, etc.

'''

import numpy as np
import re

def take_input():
    '''
    Take in logical expression of format 'q|(p&r)'
    '''
    print "Enter your logical expression below. Example: p|!q"
    logical_exp = raw_input("Enter logical expression (i.e., p|q): ")
    print "Your logical expression is \'%s\'" % logical_exp

def separate_values(logexp, debug=False):
    '''
    Take in logical expression (string) and output all subexpressions as a list
    '''
    nlogexp = logexp

    # Convert operators to more usable forms
    nlogexp = re.sub('\&','A',nlogexp)  # AND
    nlogexp = re.sub('\|','O',nlogexp)   # OR
    nlogexp = re.sub('!','N',nlogexp)   # NOT
    nlogexp = re.sub('X','X',nlogexp)   # XOR
    if debug:
        print "new logexp = %s" % nlogexp

    # find all values
    subexps = re.findall('[a-z]',nlogexp)
    if debug:
        print "subexps = %s" % subexps

    # find NOT expressions
    subexps += re.findall('N[a-z]',nlogexp)
    if debug:
        print "subexps(NOT) = %s" % subexps

    # find AND or OR expressions
    subexps += re.findall('N?[a-z][AO]N?[a-z]',nlogexp)
    if debug:
        print "subexps(NOT,AND,OR) = %s" % subexps

    # find expressions within and adjacent to parentheses
    subexps += re.findall('\(.*\)',nlogexp)
    if debug:
        print "subexps(NOT,AND,OR, and ()) = %s" % subexps

    # find all operators
#    operators = re.findall('[A-Z]',nlogexp)

    return subexps

def make_truth_table(values):

    # find out the number of variables
    cnt = len([1 for x in values if len(x) == 1])

    # find out the number of combinations. E.g., p&q -> N{p,q,p&q} = 3, p&~q -> N{p,q,~q,p&~q} = 4, etc.
    numcombos = len(values)

    # Create variables
    # Pattern: t1: 1:2^(n-1) is T, 2^(n-1)+1:2^n is F
    #          t2: 1:2^(n-2) AND 2^(n-1):
    # 
    # 1. Start loop that goes through all entries of values
    # for x in values:
    #     # 2. Find operator, whether binary, unary, or unity (i.e., no operator)
    #     op = re.match('A|O|N',x)
    #     # 3. With if/elses, match operator with operation (logical_not(), logical_or(), and logical_and())
    #     if op == 'A':
    #         # 4. Perform operation
    #     if op == 'O':
    #         # 4. Perform operation
    #     if op == 'N':
    #         # 4. Perform operation
    #     if op == '':
    #         # 4. Perform operation

        # 5. Populate table with results of calculation

    # ** Print out table
    # create header    
    print '\t'.join(values)
    print "\t".join(["-"*len(x) for x in values])

    # Move this into loop above
    # Populate T/F values
    for x in (np.arange(2**cnt,0,-1)-1):
        TF_vals = get_TF_from_string(x,cnt)
        print '\t'.join(TF_vals)

    return True

def get_TF_from_string(num,length):
    "Convert 2^n combinations to all T/F combinations"

    bin_num = np.binary_repr(num,length)

    bin_num = re.sub('0','F',bin_num)
    bin_num = re.sub('1','T',bin_num)

    return bin_num

def translate_to_forumula(logexp):
    # Need this?
    return True

def help():
    print r'This script takes in a logical expression and outputs it\'s truth table'
    print r'Dictionary:'
    print r'    & = AND/^'
    print r'    | = OR/v'
    print r'    ~ = NOT'

    return True

def TF_gen_test(n):
    ncombos = 2**n
    # Create matrix of proper size
    tvals = np.zeros((ncomb,n), dtype=bool)

    for i in (np.arange(ncombos,0,-1)-1):
        tvals[ncombos - i - 1] = [int(x) for x in np.binary_repr(i,n)]

    print tvals

def test():
    # Separate values tests
    assert separate_values('a') == ['a']
    assert separate_values('!b') == ['b','Nb']
    assert separate_values('a&b') == ['a','b','aAb']
    assert separate_values('a|b') == ['a','b','aOb']
    assert separate_values('a&!b') == ['a','b','Nb','aANb']
    assert separate_values('a|!b') == ['a','b','Nb','aONb']
    assert separate_values('(p|q)&(w&x)') == ['p', 'q', 'w', 'x', 'pOq', 'wAx','(pOq)A(wAx)']

    # Test 
    assert get_TF_from_string(0,1) ==    'F'
    assert get_TF_from_string(1,1) ==    'T'
    assert get_TF_from_string(2,2) ==   'TF'
    assert get_TF_from_string(3,2) ==   'TT'
    assert get_TF_from_string(4,3) ==  'TFF'
    assert get_TF_from_string(5,3) ==  'TFT'
    assert get_TF_from_string(6,3) ==  'TTF'
    assert get_TF_from_string(7,3) ==  'TTT'
    assert get_TF_from_string(8,4) == 'TFFF'
    
    # postfix_exec(tests)
    assert postfix_exec([True,True,'|']) == True
    assert postfix_exec([True,False,'|']) == True
    assert postfix_exec([False,True,'|']) == True
    assert postfix_exec([False,False,'|']) == False

    assert postfix_exec([True,True,'&']) == True
    assert postfix_exec([True,False,'&']) == False
    assert postfix_exec([False,True,'&']) == False
    assert postfix_exec([False,False,'&']) == False

    assert postfix_exec(['!',True,False,'|']) == False
        
    return True

if  __name__ == '__main__':

    print "Passed test? %s" % test()

    logexp = raw_input("Enter a logical expression (e.g., q&!p -- q or NOT p): ")

    if logexp == '':
        logexp = 'p|q'
        print "\n*** No expression entered. Using sample input ", logexp, "\n"

    vals = separate_values(logexp) # Separate into sub expressions
    make_truth_table(vals) # evaluate sub expressions and full expression


# Take in expression, break up using list(expr)
# 
# e = ['a', '&', 'b'] translate to ['&','a','b']
def infix_to_pretfix(e):
    "Translates an infix string to a postfix list"
#   a&b: [a,&,b] -> [a,b,&]
#   a|!c: [a,|,!,c]  -> [a,c,!,|]
#   
# Basic Idea:
#   expr = 'a&b'
#   ops = ['&','|','!']
#   temp = []
#   for x in expr:
#       if x in ops:
#           temp.append(x)
#
#
#
    bin_ops = ['|','&']
    un_ops = ['!']
    operands = []
    op = None

    prefix = []
    temp = None

    for x in e:
        if x in bin_ops and temp != None:
            prefix.append(x)
            prefix.append(temp)
            temp = None
        elif len(prefix) == len(e) - 1:
            prefix.append(x)
        else:
            temp = x
    
    return prefix

#    for x in e:
#        if x in bin_ops:
#            op = x
#        else:
#            operands.append(x)
#
#    operands.append(op) # In potfix notation
#    return operands

def postfix_exec(e, debug=False):
    "Take in broken up expression (list(expr)) in postfix order, and evaluate it as T/F"
    stack = []
    bin_ops = ['&', '|']    # binary operators
    un_ops = ['!']          # unary operators

    for x in e:
        if x not in bin_ops and x not in un_ops:
            stack.append(x)
            if debug: print "Stack = ",stack
        else:
            if len(stack) == 2: # if binary operator
                second = stack.pop()
                first = stack.pop()
                if x == '&':
                    result = np.logical_and(first,second)
                    if debug: print "in &"
                elif x == '|':
                    result = np.logical_or(first,second)
                    if debug: print "first = %s, second = %s, f|s = %s" % (first, second, np.logical_or(first,second))
                    if debug: print "in |, result = %s" % result
                else:
                    print "*** Error, neither & nor | was in the expression"
                    break
                stack.append(result)
            elif len(stack) == 1: # if unary operator
                first = stack.pop()
                result = np.logical_not(first)
                stack.append(result)

            else:
                print "*** Error, stack is empty."
    
    if debug: print "Final result: postfix(%s) = %s" % (e, stack)

    if len(stack) == 1:
        return stack[0]
    else:
        print "*** Error: stack is empty, no value is being returned"
        return None

# Look into tokenization? https://docs.python.org/2/library/tokenize.html




