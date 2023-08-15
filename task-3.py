
f = open("C:/Meet/Internship-5th Sem/batch2/bhulo bhale biju badhu maa baap ne bhulsho nai.txt","r")

a = list([])

sum = 0

b = f.readlines()

for i in b:
    c = i.split("->")
    d = int(c[0])
    sum += d
    
print(f"Sum : {(sum-40)/20}")