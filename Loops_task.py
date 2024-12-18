class Loops_task:
    
    # 1. Print Numbers from 1 to 10.
    def print_numbers(self):
        for i in range(1,11):
            print(i)
            
    # 2. Sum of Numbers from 1 to 100.
    def sum_Numbers(self,num):
        sum = 0
        for i in range(1,num+1):
            sum+=i
        return sum
    
    # 3. Factorial of a Number.
    def factorial_Num(self,num):
        fact = 1
        for i in range(num,0,-1):
            fact*=i
        print(f"factorial of a number {num} is {fact}")
        
    # 4. Fibonacci Sequence up to N terms.
    def fibonacci(self,n): 
        fib = []
        a = 0
        b = 1
        if n<=1:
            print(n)
        else:
            for i in range(n-1):
                temp = a+b
                a = b
                b = temp
                fib.append(temp)
            print(f"Fibonacci Sequence of number {n} is {b} : Series {fib}")
        
    
    # 5. Check the prime number.
    def prime_Number(self,n):
        count = 0
        for i in range(1,n+1):
            if n%i == 0:
                count+=1
        if count == 2:
            print(f"Entered number {n} is a Prime Number..!")
        else:
            print(f"Entered number {n} is a Not a Prime Number..!")
    
     # 6. Print a Multiplication Table.

    def multiplication_Table(self,n):
        for i in range(1,11):
            print(f"{n} X {i} = {n*i}")       


    # 7. Reverse a String.
    def reverse_String(self,inp):
        rev = ""

        for i in range(len(inp)-1,-1,-1):
            rev+=inp[i]
 
        print(f"Reverse of '{inp}' is '{rev}'")



    # 8. Count Vowels in a string.
    def vowel_Counter(self,str1):
        count = 0
        str_ovel = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in str1:
            if i in vowels:
                count+=1
                str_ovel.append(i)
            
        print(f"The String '{str}'' Have {count} Vowels those are, {str_ovel}")


    # 9. Print a pattern (e.g, Pyramid)
    def pattern(self,n):
        for i in range(1,n+1):
            print(i*'*')
        
    

    # Another pattren
    def pyramid(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(' ', end='')
            for k in range(2 * i + 1):
                print('*', end='')
            print()
     
    def pyramid(self,n):
        for i in range(n,0,-1):
            for j in range(n-i):
                print(' ', end='')
            for k in range(2*i-1):
                print('*', end='')
            print()
            
    # Reverse Pyramid pattern
    def pyramid1(self,n):
        for i in range(n,0,-1):
            print(" " * (n-i),end="")
            print("*"*(i))
 

    # 10. Generate a List of Squares.
    def list_Square(self):
        lst = []
        num = int(input("Enter a length of the list :: "))
        for i in range(1,num+1):
           j = int(input(f"Enter number {i} : "))
           lst.append(j)

        square_lst = []
        for i in lst:
            i = ii
            square_lst.append(i)
        print(f"Entered lst is {lst} and Squared List is {square_lst}")
        
        # With list_comprehension method
        square_list_Comprehention = [xx for x in lst]
        print(f"Squared Using list_comprehension {square_list_Comprehention}")


if __name__ == '__main__':
       obj = Loops_task()
       
       #obj.print_numbers()
       
       # print(obj.sum_Numbers(100))
       
       # num = int(input("Enter the number to find the factorial :: "))
       # obj.factorial_Num(num)
               
       # n = int(input("Enter the Sequence of A number :: "))
       # obj.fibonacci(n)

       # n = int(input("Enter a number to check Prime or Not :: "))
       # obj.prime_Number(n)
        
       # num = int(input("Enter a number to print Multiplication table :: "))
       # obj.multiplication_Table(num)
       
       # inp = input("Enter a String : ")
       # obj.reverse_String(inp)
        
       # str1 = input("Enter a string to count the Vowels :: ")
       # obj.vowel_Counter(str1)
       
       # n = int(input("Enter the number :: "))
       # obj.pattern(n)
       
       # obj.pyramid(5)
       # obj.pyramid1(5)
    
       # obj.list_Square()