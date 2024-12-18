# Python program to 
# demonstrate accessing of
# variables of nested functions

def f1():
    f1.s = 'I love GeeksforGeeks'
    
    def f2():
        f1.s = 'Me too'
        print(f1.s)
        
    f2()
    print(f1.s)

# Driver's code
f1()
