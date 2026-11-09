minutes = int(input("勉強できる時間は？(分) "))
morning = input("朝は得意？(y/n) ")
if minutes >= 60 and morning == "y":
    print("朝にじっくり型！")
elif minutes >= 60:
    print("夜にじっくり型！")
else:
    print("すきま時間型！")
