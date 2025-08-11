##### [ 계산기 API ]
##### CalculatorAPI in python by Napple7724 on August 5, 2025
##### Version : release 1.2
#################################################################
## 실행하기 전 "README.md"와 "LICENSE.md"를 읽어주세요.
## Please read "README.md" and "LICENSE.md" before running.


def calc_api(list_num_api) :
    from time import sleep
    from random import uniform
    while True :
        sleep(uniform(0.03, 0.1))
        print("부호(+, -, *, /, ^)를 입력하세요.")
        sleep(uniform(0.01, 0.3))
        str_sign = input("  : ")
        int_a = list_num_api[0]
        if str_sign == "+" :
            int_a = sum(list_num_api)
        elif str_sign == "-" :
            for sys_int_r1 in range(1, len(list_num_api)) :
                int_a -= list_num_api[sys_int_r1]
        elif str_sign == "*" :
            for sys_int_r1 in range(1, len(list_num_api)) :
                int_a *= list_num_api[sys_int_r1]
        elif str_sign == "/" :
            try :
                for sys_int_r1 in range(1, len(list_num_api)) :
                    int_a /= list_num_api[sys_int_r1]
            except ZeroDivisionError :
                print("\n")
                sleep(uniform(0.01, 0.3))
                print("오류! : 0으로 나눌 수 없습니다.")
                continue
        elif str_sign == "^" :
            for sys_int_r1 in range(1, len(list_num_api)) :
                int_a **= list_num_api[sys_int_r1]
        else :
            print("\n")
            sleep(uniform(0.01, 0.3))
            print("오류! : 정해진 부호 중 하나를 입력하세요.")
            continue
        break
    print("\n")
    sleep(uniform(0.01, 0.3))
    return int_a