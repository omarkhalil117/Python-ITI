from math import sqrt
import json

#Ex1

students = {}

with open("students.txt", "r") as rs:
    for line in rs:
        newLine = line.strip().split()
        students.update({newLine[0] : int(newLine[1])})


summ = 0
for key,val in students.items():
    summ += val
    if(val < 60):
        print(f'Student {key} failed')
print(f'avrega = {summ/len(students)}')

with open('students.json', 'w') as ws :
    json.dump(students, ws)



################################################################

#Ex2

nums = [4,9,16,25,36]

res = list( map(lambda x:sqrt(x) , nums) )

d = {}

for i in range(len(nums)):
    d.update({nums[i]:res[i]})


with open('sqrt_of_numbers.json', 'w' , encoding='utf-8') as ws:
        json.dump(d, ws)

