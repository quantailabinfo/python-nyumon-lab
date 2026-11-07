# 第2回の練習問題: 解答例

# 問題1: 名前の部分は自分の名前に変えてください。
name = "山田太郎"
print(f"こんにちは、{name}さん")

# 問題2: 小数の計算で誤差が出ないよう、先に 110 をかけてから 100 で割ります。
price = 1200
print(price * 110 // 100)

# 問題3: // で「時間」を、% で「分」を求めます。
total = int(input("分の数は？ "))
hours = total // 60
minutes = total % 60
print(f"{hours}時間{minutes}分")
