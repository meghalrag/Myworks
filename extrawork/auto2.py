import os
import re

with open('data.txt', 'r', 1) as f:
    li = f.readlines()
    print(li)
    data = input('enter:')
    for i in li:
        if data == str(i).strip():
            flag = 1
            break
    if flag == 0:
        print('item not detected')
        exit()
    else:
        print('item detected')
    dat=data.split('.')
    x=re.findall(str(dat[2]),str(li))
    print(len(x))