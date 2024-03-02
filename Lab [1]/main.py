# print("Hello World")


# Ex 1
# num = int(input("Enter Number"))

# if(num >= 20 and num <= 50):
#     print("In range")

# else :
#     print("not in range")

#Ex 2
# def clacArea(x,y):
#     return x*y

# def calcPer(x,y):
#     return (x+y)*2

# print( clacArea(0,12) )
# print( calcPer(7,10) )

# #Ex 3 
# def concat1(str1,str2):
#     return str1 + ' ' + str2

# def concat2(str1,str2):
#     return "{0} {1}".format(str1,str2)

# print( concat1("My","Name is "))
# print( concat2("My","Name is "))

# #Ex 4
# def squareList(lis):
#     res = []
#     for el in lis :
#         res.append(el**2)
#     return res

# print( squareList([1,2,5,6]) )

# #Ex 5 
# def mergeDict(d1,d2):

#     for key,val in d2.keys(),d2.values():
#         d1[key]=val
#     return d1

# dict1 = {"Name":"Ali" , "Age":20}
# dict2 = {"Name":"Ahmed" , "Age":20}

# print( mergeDict(dict1,dict2))

#Ex 6
def mergeList(list1,list2):
    
    for item in list2:
        list1.append(item)
    return list1

print( mergeList( [2,4,5] , [9,14,20]))

#Ex 7
mydict = {
    "name": "jone",
    "email": "jane@outlook.com",
    "age": 25,
    "job": "engineer", "address": "cairo, Egypt"
        }

def findKeys(key):
    return key in mydict.keys()

print( findKeys('job'))
print( findKeys('card_number'))

#Ex 8
sum = 0

for i in range(101):
    sum+=i

print(sum)

#Ex 9
def checkNum(num):
    if num == 0:
        print('Zero')
    elif(num%2 == 0):
        print("Even")
    else:
        print('Odd')

checkNum(0)
checkNum(3)
checkNum(4)

#Ex 10
def reverseString(str):
    res=''
    for i in range(len(str)-1,0-1,-1):
        res+= str[i]
    return res


print( reverseString('abcde') )    


#Ex 11
def palindrome(str):
    res = True
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            res = False
    return res

print( palindrome('abba'))
print( palindrome('acbba'))

#EX 12
ls = [2,5,4,7,8,11]
def squareOdd(lis):
    for i in range(len(lis)-1):
        if lis[i]%2 == 0:
            lis.pop(i)
        else:
            lis[i] *= lis[i]
    return lis

print( squareOdd(ls) )

#Ex 13
def checkPrime(num):
    res = True
    for i in range(2,num):
        if num%i == 0:
            res = False
    return res

print( checkPrime(13) )
print( checkPrime(6) )


# #Ex 14
def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

print( factorial(5) )

# #Ex 15
ar = [2,8,11,9]

def square(num):
    return num**2

def multiOperations(ls):
    res = []
    res.append(sum(ls))
    res.append(min(ls))
    res.append(max(ls))
    res.append(list(map(square,ls)))
    return res

print( multiOperations(ar) )