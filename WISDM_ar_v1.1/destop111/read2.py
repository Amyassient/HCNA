import os


ff1 = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp2_test_data",'r')
fff1 = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/test_data",'w')
for i in range(1,500000):
    c = ff1.readline()
    if i % 100 != 0:
        c = c.replace('\n'," ")
    fff1.write(c)
ff1.close()
fff1.close()

ff2 = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp2_train_data",'r')
fff2 = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/train_data", 'w')
for i in range(1, 1000000):
    c = ff2.readline()
    if i % 100 != 0:
        c = c.replace('\n', " ")
    fff2.write(c)
ff2.close()
fff2.close()