class Iterator:
    """
    An iterator is an object that allows you to traverse through a collection of items, one at a time. 
    In Python, iterators follow a specific protocol defined by two methods:
    __iter__(): Returns the iterator object itself. This is used in the iteration process to get the iterator.
    __next__(): Returns the next item in the sequence. When there are no more items, it raises the StopIteration exception to signal that the iteration is complete.
    """
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Usage
itr = Iterator(5)
# for number in itr:
#     print(number)
print(next(itr))

class Generator:
    pass


class itr_gen:   
    def iterator_concept(self,itr):
    # An iterator is an object that implements two key methods
    #   iter(object): Returns an iterator for the given object.
    #   next(iterator): Returns the next item from the iterator.    
        itr = iter(itr)
        print(itr)
        print(next(itr))
        print(next(itr,'No more item'))
        print(next(itr,'No more item'))
        print(next(itr,'No more item'))
        print(next(itr,'No more item'))
        print(next(itr,'No more item'))
        
    def generator_concept(self):
        # A generator is a special type of iterator that is defined with a function containing one or 
            # more yield expressions. Unlike standard functions that return a single value, generators use 
            # yield to return a series of values lazily, one at a time.
        yield 1
        yield 2
        yield 3
        yield 4




obj = itr_gen()

# itr = [2,3,4,5]
# obj.iterator_concept(itr)
    
# # Generator call
gen = obj.generator_concept()
# print(next(gen))
# print(next(gen))    
# print(next(gen))    
# print(next(gen))    
# print(next(gen,'no value'))   