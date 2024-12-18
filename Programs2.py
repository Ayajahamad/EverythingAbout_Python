class python_Programs:
    # 1. Strong number founder
    def strong_Number_Founder(self,num):
        n = str(num)
        total = 0
        for i in n:
            sum = 1
            for j in range(1,int(i)+1):
                sum*=j
            total+=sum
        if total==num:
            print(f"Entered number {num} is a strong Number..!")
        else:
            print(f"Entered number {num} is Not a strong number..!")
            
    # 2. Generate a strong numbers from 1 to n.
    def strong_Numbers(self,num):
        for i in range(1,num+1):
            str_number = str(i)
            sum = 0
            for j in str_number:
                fact = 1
                for k in range(1,int(j)+1):
                    fact*=k
                sum+=fact
                
            if sum==i:
                print(i)
    
    # 3. List all the prime number from 1 to n.
    def prime_number_Generator(self,target):
        for i in range(1,target+1):
            count = 0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count==2:
                print(i)
    
    # 4. List all the Amstrong Numbers from 1 to n.
    def amstrong_number_Generator(self,target):
        for i in range(1,target+1):
            sum = 0
            str_num = str(i)
            length = len(str_num)
            sqr = 0
            for j in str_num:
                sqr+=int(j)length
            sum+=sqr
            
            if i == sum:
                print(i)

    # 5. Find and list fctorial of the Numbers from 1 to n.
    def factorial_Generator(self,target):
        for i in range(1,target+1):
            fact = 1
            for j in range(1,i+1):
                fact*=j
            print(f"Factorial of a number {i} is {fact}")
            
    # 6. Find the largest world in a sentence.        
    def largest_World(self,s):
        spl = s.split()
        w = sorted(spl,key=len)
        world = w[-1]
        print(world)
        
    # 7. Find the palindrome words in a sentence.
    def palindrome_word(self,s):
        P_lst = []
        spl = s.split()
        for w in spl:
            if w == w[::-1]:
                if w not in P_lst:
                    P_lst.append(w)
        print(P_lst)
        
    # 8. Program to sort the words in Alphabetic order.
    def sort_world(self,s):
        sorted_words = []
        spl = s.split()
        print(spl)
        for w in spl:
            s = sorted(w)
            s1="".join(s)
            sorted_words.append(s1)
        print(sorted_words)

    # 9.Input: l1 = [2,4,3], l2 = [5,6,4]
        # Output: [7,0,8]
        # Explanation: 342 + 465 = 807.
    def add_two_numbers(self,num1,num2):
        l1 = num1[::-1]
        l2 = num2[::-1]
        s = ''.join(str(x)for x in l1)
        s1 = ''.join(str(x)for x in l2)
        add = int(s)+int(s1)
        l = str(add)
        rev = l[::-1]
        res = [int(i) for i in rev]
        print(res)
        
        
if __name__=='__main__':
    obj = python_Programs()
    
    # num = int(input("Enter a Number :: "))
    # obj.strong_Number_Founder(num)
    
    # num = int(input("Enter the target Number To list strong Numbers :: "))
    # obj.strong_Numbers(num)
    
    # num = int(input("Enter the target number to Generate prime Numbers :: "))
    # obj.prime_number_Generator(num)
    
    # num = int(input("Enter the target number to Generate Amstrong Numbers :: "))
    # obj.amstrong_number_Generator(num)
    
    # num = int(input("Enter the target number to Generate Factorial:: "))
    # obj.factorial_Generator(num)
    
    # s = "Hello this is Something new world"
    # obj.largest_World(s)
    
    # s = "Palindrome words are mam soos and mam sdsds soos mamamam"
    # obj.palindrome_word(s)
    
    # s = "palindrome words are mam soos and mam sdsds soos mamamam"
    # obj.sort_world(s)
    
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]
    # obj.add_two_numbers(l1,l2)
    
   