import random
import math
YES = ['yes', 'y', 'YES', 'Yes']

def f_level_check(x1, x2, oper):
    x1 = int(x1)
    x2 = int(x2)
    if '+' in oper:
        result = (x1 + x2)
        return result
    elif '-' in oper:
        result = (x1 - x2)
        return result
    elif '*' in oper:
        result = (x1 * x2)
        return result


def f_level():
    mark = 0
    for _ in range(5):
        x1 = random.randint(2, 9)
        x2 = random.randint(2, 9)
        oper = ['+', '-', '*']
        sign = random.choice(oper)
        print('{} {} {}'.format(x1, sign, x2))
        result = f_level_check(x1, x2, sign)
        user = user_input()
        if result == user:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
    print("Your mark is {}/5.Would you like to save the result? Enter yes or no.".format(mark))
    user = input()
    if user in YES:
        result_save(1, mark)
        return
    else:
        return


def result_save(level, mark):
    if level == 1:
        level = 'in level 1 (simple operations with numbers 2-9).'
    elif level == 2:
        level = 'in level 2 (integral squares of 11-29)'
    print('What is your name?')
    user = input()
    result = '{name}: {mark}/5 {lvl}'.format(name=user, mark=mark, lvl=level)
    file = open('results.txt', 'a')
    file.write(result)
    file.close()
    print('The results are saved in "results.txt".')


def s_level():
    mark = 0
    for _ in range(5):
        x = random.randint(11, 29)
        print(x)
        result = int(math.pow(x, 2))
        user = user_input()
        if result == user:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
    print("Your mark is {}/5.Would you like to save the result? Enter yes or no.".format(mark))
    user = input()
    if user in YES:
        result_save(2, mark)
        return
    else:
        return


def main():
    while True:
        print("""
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
        """)
        user = input()
        if user == '1':
            f_level()
            break
        elif user == '2':
            s_level()
            break
        else:
            print('Incorrect format')
            continue


def user_input():
    while True:
        user = input()
        try:
            int(user)
            return int(user)
        except ValueError:
            print('Incorrect format')
            continue


if __name__ == '__main__':
    main()
