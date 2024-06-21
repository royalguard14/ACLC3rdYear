fullName = input("Enter FullName *Ex. Sollesa,Marie,A,Bautista: ")
fullNameArr =  fullName.split(",")

for i in fullNameArr:
    if len(i) == 1:
        middle_initial = i
        midnameIndx = fullNameArr.index(i)
        break

firstname = " ".join(fullNameArr[:midnameIndx])
lastname = " ".join(fullNameArr[midnameIndx + 1:])

print(f'''
Lastname : {lastname}
Firstname: {firstname}
Middle Initial: {middle_initial}.
    ''')

