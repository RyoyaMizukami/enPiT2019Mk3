#coding: utf-8
import random
import time

vending_count = 0
poem_list = ["信じるものは掬われる","時には立ち止まることも必要だよ","今日がこないと明日はこない！","やっぱ肉だゎ、、、、","完全無償の愛か死をくれる恋人さえいれば楽になる","時速60kmで走る車から手を出すとおっぱいの感触と同じ","私が持って行きます。でも、道を知りませんが……","「世界」、「世界」って、「世界」って言葉簡単に口にするんじゃねえ！！！","俺の胸で泣けよ","僕は君が好きだ","君は僕の天使さ！","シラフのくせに「幸せだ」なんて言う奴はとんでもない嘘つき野郎"]
poem_author = ["しやあ","広島大学 藤村ディエゴ","後醍醐天皇","今日のenpit","広島大学情報工学科藤村大吾9/7誕生日中2の頃の彼女の名前はゆうか","ひんぬーはすてーたす。","やっとむ","しゅうぞう","広島大学情報工学科藤村大吾","広島大学 ディエゴ","広島大学 ディエゴ","広島大学情報工学科藤村大吾9/7誕生日中2の頃の彼女の名前はゆうか"]
poem_vender = []

for i in range (len(poem_list)):
    poem_vender.append(poem_list[i] + " " + poem_author[i])

def vending_machine():
    global vending_count
    global n
    the_world(10,1)
    #print(poem_list[vending_count % len(poem_list)] + " " + poem_author[vending_count % len(poem_author)])
    kakugen_chosen = random.choice(poem_vender)
    print("＿" + ("人" * len(kakugen_chosen)) + "＿")
    print("＞" + kakugen_chosen + "＜")
    print("￣" + ("Y^" * len(kakugen_chosen)) + "￣")
    vending_count += 1
    uriage_keeper()
    print("ご利用ありがとうございました。")
    oturi_maker()
    return None

def oturi_maker():
    global n
    oturi = n - 100
    money_type = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    money_number = [0] * 10
    otulist = []
    oturi_message = "お釣りは"

    for i in range(10):
        money_number[i] += oturi // money_type[i]
        if money_number[i] != 0:
            otulist.append(str(money_type[i]) + "円" + str(money_number[i]) + "枚")
            oturi -= money_type[i] * money_number[i]
    for oturi in otulist:
        oturi_message += ""+oturi

    if n - 100 != 0:
        print(oturi_message + "で、合計" + str(n - 100) + "円です。")
    else: print("お釣りはありません。")


def admin_mode():
    global vending_count
    with open("uriage.txt") as f:
        uriage_data = int(f.readline())
    PASS = input("パスワードを入力してください。　")
    if PASS == "admin":
        print("現在の売上は" + str(uriage_data) + "円です。")
    else: print("パスワードが違います。やり直してください。")

def uriage_keeper():
    with open("uriage.txt") as f:
        uriage_data = int(f.readline())
    global vending_count
    with open("uriage.txt", mode = "w", encoding="utf-8") as f:
        f.write(str(uriage_data + 100))

def hikizan():
    global n
    while n < 100:
        ins_money = 100 - n
        moremoney = int(input("お金が" + str(ins_money) + "円不足しています。\n"))
        n += moremoney

# 関数名通り、時間をn回s秒止めてローディングっぽく.......とか表示する関数です(制限時間とかはありません)。
def the_world(n, s):
    for i in range(n):
        if i != n-1:
            print(".")
            time.sleep(s)
        else:
            print("今の貴方にぴったりの言葉はこれ！")
            time.sleep(s)

while True:
    print("-------------------")
    print("|                 |")
    print("|   POEM VENDER   |")
    print("|                 |")
    print("|  INSERT 100YEN  |")
    print("|                 |")
    print("-------------------")

    mode = int(input("モードを選択してください。\n 1:購入, 0:システム終了　"))
    if mode == 1:
        n = int(input("お金を投入してください。100円で格言が出てきます。\n"))
        if n >= 100:
           answer = input("本当に引きますか？(Y/n)")
           if answer == "Y":
               vending_machine()
           else:
               print("ありがとうございました。")
        else:
            hikizan()
            answer = input("本当に引きますか？(Y/n)")
            if answer == "Y":
                vending_machine()

    elif mode == -15825:
        admin_mode()
        continue
    elif mode == 0:
        break

"""    if n == "admin":
        admin_mode()
    try:
        n = int(n)
    except ValueError:
        print("お金を投入してください。")
        continue"""
