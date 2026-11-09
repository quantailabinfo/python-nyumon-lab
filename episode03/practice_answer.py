# 第3回の練習問題: 解答例

# 問題1: 2で割った余りが0なら偶数です。
number = int(input("整数は？ "))
if number % 2 == 0:
    print("偶数です")
else:
    print("奇数です")

# 問題2: 条件は上から順に判定されるので、小さい年齢から調べます。
age = int(input("年齢は？ "))
if age <= 12:
    print("500円")
elif age <= 64:
    print("1800円")
else:
    print("1200円")

# 問題3: 「雨でない」は、rain が "n" と等しいことで判定します。
temperature = int(input("気温は？ "))
rain = input("雨ですか？(y/n) ")
if temperature >= 20 and rain == "n":
    print("半袖でOK")
else:
    print("上着を持っていこう")
