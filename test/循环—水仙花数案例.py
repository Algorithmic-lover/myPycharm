# 用户输入一三位数数值，判断是否为水仙花数，
# 水仙花数：百位3次方+十位3次方+个位3次方=数值本身

while True:
    # 1.用户输入
    data = input("输入一三位数：")
    # 2.判断数据是否合格
    data = int(data)
    if data < 100 or data > 999:
        print("输入无效！")
        exit()

    # 3.各位分解
    h = data // 100
    s = data % 100 // 10
    n = data - h * 100 - s * 10
    # 3.判断是否为水仙花数
    if data==(h ** 3 + s ** 3 + n ** 3):
        print("是水仙花数！")
    else:
        print("不是水仙花数！")

