# 画面に自分の「学科名」「学年」「学籍番号」を出力してくださいねぇ
def print_self_infomation():
    print('ITスペシャリスト科', '2年', 's15008')

# 自分の年齢が80歳になるまであと何年かをけいさんしてくれめんす
def print_how_mary_years_to_80():
    age = 24
    print("80歳まであと", str(80 - age) + "年")

# 与えられた整数パラメータが「偶数」か「奇数」かを出力すて
def print_odd_or_even(target):
    print("偶数" if target % 2 == 0 else "奇数")

# randomモジュールを使用して0-50の整数をを生成し、25が出るまで「ほげ」と出か
def print_hoge():
    from random import randint
    while(randint(0, 50) != 25):
        print("ほげ")

# 100から1000までの偶数のみを表示してねぇ
def print_even_from_100_to_1000():
    for i in range(100, 1001, 2):
        print(i, end=" ")

if __name__ == '__main__':
    print_self_infomation()
    print_how_mary_years_to_80()
    print_odd_or_even(10)
    print_odd_or_even(13)
    print_hoge()
    print_even_from_100_to_1000()