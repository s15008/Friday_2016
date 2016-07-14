# -*- coding: utf-8 -*-

def getCalendar(year, month):
    DAYS_SUBTRACT = [0, 3, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]    #月の日数の31からの差分

    daysOfMonth = 31 - DAYS_SUBTRACT[month - 1]
    if leap_year(year) and month == 2: daysOfMonth += 1 #うるう年処理
    cale = [i + 1 for i in range(daysOfMonth)]  #日数を生成
    cale = [0] * ((get_day_of_week(year, month, 1) - 1 + 7) % 7) + cale #月始めの曜日分0でうめる
    add_hip = (7 * (len(cale) // 7 + 1) - len(cale)) % 7    #カレンダーが7行に揃うように0でうめる
    cale = cale + [0] * add_hip
    return [cale[i:i+7] for i in range(0, len(cale), 7)]    #テストの為にわざわざリストを分割しました。

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

'''
Using Zeller's congruence
@return
    0: SUN  1: MON  2: TUE  3: WED
    4: THU  5: FRI  6: SAT
'''
def get_day_of_week(year, month, date):
    if month <= 2:
        month += 12
        year -= 1

    j = year // 100
    k = year % 100
    m = month
    q = date

    return (q + (((m + 1) * 26) // 10) + k + (k // 4) + (j // 4) - (2 * j)) % 7

if __name__ == '__main__':
    print(getCalendar(2016, 7))
    '''
    for i in range(12):
        c = getCalendar(2016, 1 + i)
        print(i + 1, "月")
        for i in range(len(c)):
            print("{:>3}".format(c[i]), end="")
            if (i + 1) % 7 == 0:
                print()
        print()
    '''