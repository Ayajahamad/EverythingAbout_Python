# 6. Accept a english Alphabet from User chek it is a consonent or ovel.
inp = input("Enter a Single Character Here :: ")

if inp in "aeiouAEIOU":
    print(f"Entered Character '{inp}' is Ovel")
else:
    print(f"Entered Character '{inp}'is Consonent")