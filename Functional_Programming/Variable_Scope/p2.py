# Changing the Scope values in another Scope

x = 10

def Outer():
    def Enclose():
        global x # Changing the global value in local Scope = global -keyword
        x = x+2
        y = 10
        print("X value in Enclose : ", x)
        def Inner():
            nonlocal y # Changing the Enclosed scope value in local = nonlocal -keyword
            y = y+5
            print("X value in Inner : ", x)
            print("Y value in Inner : ", y)
        Inner()
    Enclose()
Outer()
print("X value in Global : ", x)