import random

f = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/random",'w')
a = []
for i in range(1,37):
    a.append(i)
b = random.sample(a,6)
for i in b:
    for j in a:
        if i == j:
            a.remove(i)
for i in range(30):
    f.write(str(a[i]))
    f.write(" ")
for i in range(6):
    f.write(str(b[i]))
    f.write(" ")
f.close()


