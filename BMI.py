height = input("請輸入身高，單位cm:")
weight = input("請輸入體重，單位Kg:")
height = int(height)
weight = int(weight)
height = height/100
BMI = weight / height / height
if BMI < 18.5:
    print("你的BMI值為", BMI, "太輕啦")
elif BMI >= 18.5 > 24:
    print("你的BMI值為", BMI, "很正常喔")
elif BMI >= 24 > 27:
    print("你的BMI值為", BMI, "有點重喔")
elif BMI >= 27 > 30:
    print("你的BMI值為", BMI, "輕度肥胖了!")
elif BMI >= 30 > 35:
    print("你的BMI值為", BMI, "中度肥胖中")
elif BMI >= 25:
    print("你的BMI值為", BMI, "重度肥胖，該減肥啦")
