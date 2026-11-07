price = int(input("合計金額は？ "))
people = int(input("人数は？ "))
each = price // people
rest = price % people
print(f"1人 {each} 円")
print(f"あまり {rest} 円")
