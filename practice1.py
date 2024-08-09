#to import a function -->import math.h -->example print(math.sqrt(25))
#you can alias the function name by -->import math as m -->print(m.sqrt(23))
# if you are not intrested to write math you can write this line -->from math import * -->example print(sqrt(25))
# you can use sqrt like this -->from math import sqrt as s
#you can write -->from math  import gcd,lcm only these are used


a=0
b=20
a,b=b,a
print(a,b)

#assign multiple values in sinble line
age , name, cgpa=18 , "pavan sir" ,6.5
print(age,name,cgpa, sep='\n') # when you want to print in next line use sep='\n'
A=B=C=0
print(A,B,C)

#bool
print(bool(0))
print(bool(1))
print((bool("")))

list_of_boolean_values=[True ,True, True,False]
print(any(list_of_boolean_values))  #any returns if atleast one value is true
print(all(list_of_boolean_values)) # all returns ture if all the values in it are true

list_boolean=[0,0,0,1,[],'']
print(any(list_boolean))
print(all(list_boolean))

#conditional statements
c=100
b=50
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

# to take input
    n=int(input("enter a number: "))
    print("even" if n%2==0 else "odd") #single line if else statement

string ="123"
number=int(string)
print(number)
binart_string="1011"
print(int(binart_string,2))
octal_string="124"
hex_string="AA"
print(int(octal_string,8))
print(int(hex_string,16))

n1=23
n2=67
n3=170
print(bin(n1)) #gives binary string
print(oct(n2)) #gives octal sting
print(hex(n3))# gives hexa string

#loops concept
#for loop and while loop

#while loop  -intilization ,condition,updation
i=1
while i<=5:
    print(i,end=" ")  # to print in same line
    i+=1
# to  get the length of a give integer convert into string and use length function
number=123
s=str(number)
print(len(s))

# for loops
name=['surekha', 'reddy' ,'geetha' , 'sri']
for x in name:     #value based loops
    print(x)
string="hello world"
for x in string:
    print(x,'-->',ord(x))

#range
r=range(20)
print(r)
# to see numbers in range use list or tuple or for
print(list(r))
print(tuple(r))
for x in range(1,10,2): # using step but last number is not included
    print(x, end=' ')

# to use range to print in reverse order start end step is required
for x in range(20,10,-1):
    print(x)
# to print 1 to  n you need to include n+1

# to print a to b
a,b=map(int,input().split())
for i in range(a,b+1): # to take input two integers at a same time
    print(i,end=' ')

print(sep="\n")
for x in range(b,a,-1):
    print(x , end=' ')

 # importing functions
 

    