student={
    "name":"rumaan",
    "age":21,
    "gender":"male",
    "phonenum":7788

}
print(student)
print(student["age"])

for i in student:
    print(i)
for i in student:
    print(student[i])

for i in student.keys():
    print(i)
for i in student.values():
    print(i)
for i in student.items():
    print(i)