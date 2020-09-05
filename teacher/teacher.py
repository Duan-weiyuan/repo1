import random
break_or_no = 0
file = open("id_and_pw.txt", "a+")
while True:
    id = input("请输入你的账号(注册账号请输入“zc”): ")
    if id == "zc":
        new_id = input("请输入账号")
        while True:
            new_pw = input("请输入密码")
            verify_pw = input("请再次输入密码")
            if new_pw == verify_pw :
                print("注册成功！")
                print("--------------------------------------")
                file.write(new_id+new_pw+"\n")
                file.close()
                id = input("请输入你的账号(注册账号请输入“zc”): ")
                break
            else:
                print("密码错误，请重新输入")
    pw = input("请输入你的密码： ")
    lod_id_and_pw = id + pw+"\n"
    file = open("id_and_pw.txt", "a+")
    file.seek(0, 0)
    for id_pw in file:
        if id_pw == lod_id_and_pw:
            print("登陆成功")
            print("-------------------------------------------")
            break_or_no = 1

    if break_or_no == 1:
        break

    print("账号或密码错误请重新输入")

random_num = random.choice(range(10))

def caishuzi():
    step = 0
    while True:
        step = step +1
        s = int(input("请输入一个0-9之间的数字： "))
        if s == random_num:
            print("你真是一条小蛔虫！")
            break
        elif s > random_num:
            print("大了大了！")
        elif s<random_num:
            print("小了小了")
    goal = 11-step
    print("你的得分是"+str(goal))

while True:
    caishuzi()
    con_or_stop = int(input("输入1继续，输入2退出"))
    if con_or_stop == 2:
        print("-----------------------游戏结束---------------------------------")
        break

