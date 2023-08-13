


f = open("C:/Meet/Internship-5th Sem/batch2/bhulo bhale biju badhu maa baap ne bhulsho nai.txt","r")



# if (f):
#     print("Success")
# else:
#     print("Not")

a = list([])

sum = 0

b = f.readlines()

for i in b:
    c = i.split()
    # print(c[0])
    d = int(c[0])
    sum += d
    
print(f"Sum : {sum}")
    
# print(a)
    

# c = b.split()

# a = b.

# print(b)
# for i in b:
#     print(b)