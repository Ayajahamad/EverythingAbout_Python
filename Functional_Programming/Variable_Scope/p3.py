# Making Local Variable to Global - Using Global keyword
def outer():
    def Inner():
        global z
        z = 10
    Inner()
outer()
print(z)