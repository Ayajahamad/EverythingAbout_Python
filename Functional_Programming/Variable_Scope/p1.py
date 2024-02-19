x = 'global'

def outer_func():
    x = 'enclosing'
    print(x) # Looks for 'x' in local namespace
    
    def inner_func():
        x = 'local'
        print(x)  # Looks for 'x' in local namespace

    inner_func()

outer_func()
print(x)  # Looks for 'x' in global namespace

print("Hello") # Builtin function - we can use anyware in the Script