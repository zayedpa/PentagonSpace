import copy
student={
"name":"rumaan",
"age":21,
"gender":"male",
"address":{
    "resi":"banglore",
    "permanent":"peraje"
},
"phnum":{
    "mobile":2233,
    "land":7878
}
}
print(student)

s1=student

student["age"]=23
print(s1)
print(student)

s2=student.copy()
student["age"]=25
print(s2)
print(student)

s3=copy.deepcopy(student)
s3["phnum"]["mobile"]=8888
print(student)
print(s3)
