import copy


class Copy_Shallow_Deep:
    def __init__(self) -> None:
        print("In Python, shallow copy and deep copy are two ways to create copies of objects, but they handle the copying process differently")


    def Shallow_Copy(self):
        """
        A shallow copy creates a new object, but it does not create copies of the nested objects within
        the original object. Instead, it only copies references to the nested objects. 
        This means that changes to the nested objects in the copied object will also affect the nested 
        objects in the original object.
        """
        """
        Changing an element in the nested list of shallow_copy also affects original_list because both 
        lists share references to the same nested lists.
        """
        import copy

        # Original list with nested lists
        original_list = [[1, 2, 3], [4, 5, 6]]

        # Create a shallow copy
        shallow_copy = copy.copy(original_list)

        # Modify the nested list in the shallow copy
        shallow_copy[0][0] = 'X'

        print("Original List:", original_list)
        print("Shallow Copy:", shallow_copy)
    

    def Deep_Copy(self):
        """
        A deep copy creates a new object and also recursively creates copies of all nested objects. 
        This means that the original object and the copied object are completely independent of each 
        other.
        """
        """
        Modifying the nested list in deep_copy does not affect original_list because they do not share 
        references to the nested lists.
        """
        # Using the copy module: The copy.deepcopy() function creates a deep copy of an object.
        import copy

        # Original list with nested lists
        original_list = [[1, 2, 3], [4, 5, 6]]

        # Create a deep copy
        deep_copy = copy.deepcopy(original_list)

        # Modify the nested list in the deep copy
        deep_copy[0][0] = 'X'

        print("Original List:", original_list)
        print("Deep Copy:", deep_copy)


    # Function to print memory addresses and contents
    
    def print_memory_info(self, label, obj):
        print(f"{label}:")
        print(f"  Object ID: {id(obj)}")
        for i, item in enumerate(obj):
            print(f"  Nested Object {i} ID: {id(item)}")
            for j, nested_item in enumerate(item):
                print(f"    Element {j} ID: {id(nested_item)}")
        print()
    

if __name__=='__main__':
    obj = Copy_Shallow_Deep()
    
    # Shallow copy
    # obj.Shallow_Copy()
    
    # Deep copy
    # obj.Deep_Copy()
    
    # ------------------------Print memory information------------------------------
    # Create a nested list
    original_list = [[1, 2, 3], [4, 5, 6]]

    # Perform a shallow copy
    shallow_copy = copy.copy(original_list)

    # Perform a deep copy
    deep_copy = copy.deepcopy(original_list)
    print("Original List:")
    obj.print_memory_info("Original List", original_list)

    print("Shallow Copy:")
    obj.print_memory_info("Shallow Copy", shallow_copy)

    print("Deep Copy:")
    obj.print_memory_info("Deep Copy", deep_copy)
    

    

"""
Shallow Copy:
Copies the outer object only.
Shares references to the nested objects.
Changes to nested objects in the copied object will affect the original object.

Deep Copy:
Copies the outer object and all nested objects.
Creates entirely independent copies of nested objects.
Changes to nested objects in the copied object do not affect the original object.
"""