
def calculate_sum(num):
    first_two = num[:-1]
    first_one = num[0]

    last_one = num[-1]
    last_two = num[-2:]

    sum0 = 0
    sum1 = int(first_two)+int(last_one)
    sum2 = int(first_one)+int(last_two)

    for i in num:
        sum0+=int(i)

    total = int(num)+sum1+sum2+sum0
    print("the total is :: ", total)

def main():
    num = input("Enter the number :: ")
    calculate_sum(num)

if __name__=="__main__":
    main()
