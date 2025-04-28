'''
for i in range(1,10):
    print(i)

    
#5 table
for i in range(1,11):
    print(i,"* 5 = ",i*5)
'''


#get number for a & b. print the number between a& b.
'''
a = int(input("A:"))
b = int(input("B:"))
for i in range(a+1,b):
    print(i)
'''

#Odd & Even

'''
evenCount = 0
oddCount = 0
for i in range(1, 11):
    if(i%2 == 0):
        evenCount = evenCount+1;
        print("EVEN")
    else:
        oddCount = oddCount+1;
        print("ODD")
print(evenCount)
print(oddCount)

'''

#forloop with list
'''
sum = 0
avg = 0
list = []
for i in range(10):
    num = int(input("Enter num"+ str(i+1)+":"))
    list.append(num)
    sum = sum + num
    print("SUM: ", sum)

print(list)
print("AVG: ", sum/10)
'''

#Nested For loop
'''
for i in range(1, 5):
    print("WEEK: ", i)
    for j in range(1, 8):
        print("DAY: ", j)
'''
# COunt the numbers divisible by 3 & 5 (1 - 100)
'''
count = 0
for i in range(1, 100):
    if(i % 3 == 0 and i % 5 == 0):
        print(i)
        count = count + 1;
print("COUNT: ",count)

'''      
# STAR Pattern

'''
count = int(input("Enter any number"))
for i in range(1,count+1):
    print()
    for j in range(1,i+1):
        print(j,end="")


'''

count = int(input("Enter any number"))

for i in range(1,count+1):
    print()
    for j in range(1, count-i):
        print(" ",end="")







    
    
