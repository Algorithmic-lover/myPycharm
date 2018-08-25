# 九九乘法表
# @slx
# 循环的使用

for i in range(1,10):
    for j in range(1,i+1):
        result=i*j
        print("{0}*{1}={2}" .format(j,i,result),end="\t")   #\t—table
    print("")

