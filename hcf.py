# Enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))
a = numberLargest
b = numberSmallest
# Using Euclid's Algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ", numberLargest)
LCM = (a*b) // numberLargest
print("LCM is : ", LCM)
