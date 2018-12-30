import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import tensorflow as tf
import time
import random
import os
filename1 = "/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/data.txt"
filename2 = "/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp1_test_data"
filename3 = "/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp1_train_data"
def washdata(filename1,filename2,filename3):

    a = []
    for i in range(1,37):
        a.append(i)
    b = random.sample(a,6)
    for i in b:
        for j in a:
            if i == j:
                a.remove(i)

    lines = open(filename1,'r')
    f = open(filename2, 'w')
    for line in lines:
        tmpList1 = line.split(' ')
        for i in range(6):
            if str(tmpList1[0]) == str(b[i]):
                f.write(' '.join(tmpList1[0:7]))
    lines.close()
    f.close()
    print(a)
    print(b)

    g = open(filename3,'w')
    lines = open(filename1, 'r')
    for line in lines:
        tmpList2 = line.split(' ')
        for i in range(30):
            if str(tmpList2[0]) == str(a[i]):
                g.write(' '.join(tmpList2[0:7]))
    g.close()
    lines.close()

    



    return
washdata(filename1,filename2,filename3)








'''a = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp1_train_labels",'a')
for i in range(1,944):
    b="5\n"
    a.write(b)
a.close()'''
'''a = np.loadtxt("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp1_train_labels")
b = tf.one_hot(a,6,on_value=1.0,off_value=0.0)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    b = sess.run(b)
    np.savetxt("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/train_labels",b)'''


'''f = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/temp2_train_data",'r')
ff = open("/home/amyassient/PycharmProjects/HCNA-AI/WISDM_ar_v1.1/train_data",'w')

for i in range(1,854601):
    a = f.readline()
    if i % 100 != 0:
        a = a.replace('\n', " ")


    ff.write(a)
f.close()
ff.close()'''









