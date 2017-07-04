#coding:utf-8

import csv

mylist = ['我饿','他们','ni','可以','不能','哈哈哈']
filename = 'b.csv'
print(type(mylist))
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(mylist)
