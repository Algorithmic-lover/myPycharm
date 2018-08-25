# 体脂率的计算，功能分析：1.输入身高、体重、年龄等。2.数据处理：体脂率计算。3.输出给用户.

# @slx
# 输入
# 身高
pHeight = input("请输入身高（cm）:")
pHeight = float(pHeight)
# if 0<pHeight<300
#     return
# else
#     pHeight=float(pHeight)
# 体重
pWeight = input("请输入体重（kg）:")
pWeight = float(pWeight)
# 年龄
pAge = input("年龄：")
pAge = int(pAge)
# 性别
pSex = input("性别（男：1；女：0）：")
pSex = int(pSex)

# 体脂率计算
# BM=体重/（身高*身高）
# 体脂率=1.2*BMI+0.23*年龄-5.4-10.8*性别
BMI = pWeight / (pHeight * pHeight)
TZL = 1.2 * BMI + 0.23 * pAge - 5.4 - 10.8 * pSex

# 判断体脂率
# 男正常：15%-18%; 女：25%-28%
minTZL = 0.15 + 0.10 * (1 - pSex)
maxTZL = 0.18 + 0.01 * (1 - pSex)
result = minTZL < TZL < maxTZL  #布尔型

# 输出结果
print("是否符合标准：",result)  #输出为ture 或 false
