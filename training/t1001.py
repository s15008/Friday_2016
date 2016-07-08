# 与えられた2つのパラメータの合計を2倍したものが60を超えているかどうか
def check_sum_2times_over_60(par1, par2):
    return (par1 + par2) * 2 > 60

# 与えられた金額に消費税率8％を含めた値が5000を超えているかどうか
def tax_inclued(cost):
    return (cost * 1.08) > 5000

# 与えられたスコアを80以上なら'A'、60以上80未満なら'B'、45以上60未満なら'C'、45未満は'F'と返す
def judge_rank(score):
    if score >= 80: return 'A'
    elif score >= 60: return 'B'
    elif score >= 45: return 'C'
    else: return 'F'

# 与えられた数値の階乗を返す。ただし再帰は使用禁止
def factorial(num):
    sum = 1
    for i in range(0, num):
        sum *= i + 1
    return sum

# 与えられた数値の2の累乗を返す。再起使用禁止。便利な演算子利用禁止
def power_of_two(num):
    sum = 1
    while num > 0:
        sum *= 2
        num -= 1
    return sum

if __name__ == '__main__':
    print(check_sum_2times_over_60(25, 6))
    print(tax_inclued(100))
    print(judge_rank(30))
    print(judge_rank(50))
    print(judge_rank(65))
    print(judge_rank(80))
    print(factorial(10))
    print(power_of_two(8))