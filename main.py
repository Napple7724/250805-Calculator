##### [ 계산기 ]
##### Calculator in python by Napple7724 on August 5, 2025
##### Version : release 1.1
#################################################################
## 실행하기 전 "README.md"와 "LICENSE.md"를 읽어주세요.
## Please read "README.md" and "LICENSE.md" before running.
from time import sleep
from random import uniform
print("Loading...")
sleep(uniform(0.3, 0.5))
while True :
    try :
        print("\n\n[ 계산기 ]\nCalculator in python by Napple7724 on August 5, 2025\nVersion : release 1.1\n")
        sleep(uniform(0, 0.1))
        while True :
            try :
                list_num = list(map(int, input("숫자를 공백으로 나눠 입력하세요.\n  : ").split()))
                if len(list_num) >= 2 :
                    break
                else :
                    print("\n\n오류! : 항목을 2개 이상 입력하세요.")
            except ValueError :
                print("\n\n오류! : 숫자를 입력하세요.")
            sleep(uniform(0, 0.1))
        print("\n")
        while True :
            sleep(uniform(0, 0.1))
            str_sign = input("부호(+, -, *, /, ^)를 입력하세요.\n  : ")
            int_a = list_num[0]
            if str_sign == "+" :
                int_a = sum(list_num)
            elif str_sign == "-" :
                for sys_int_r1 in range(1, len(list_num)) :
                    int_a -= list_num[sys_int_r1]
            elif str_sign == "*" :
                for sys_int_r1 in range(1, len(list_num)) :
                    int_a *= list_num[sys_int_r1]
            elif str_sign == "/" :
                try :
                    for sys_int_r1 in range(1, len(list_num)) :
                        int_a /= list_num[sys_int_r1]
                except ZeroDivisionError :
                    print("\n\n오류! : 0으로 나눌 수 없습니다.")
                    continue
            elif str_sign == "^" :
                for sys_int_r1 in range(1, len(list_num)) :
                    int_a **= list_num[sys_int_r1]
            else :
                print("\n\n오류! : 정해진 부호 중 하나를 입력하세요.")
                continue
            break
        print(f"\n\n  = {int_a}")
    except KeyboardInterrupt :
        print("\n\n종료합니다.")
        quit()
    except :
        print("\n\n오류! : 알 수 없는 오류가 발생했습니다.")
    print("\n")
    try :
        while True :
            sleep(uniform(0, 0.1))
            str_q = input("계속 하시겠습니까? (Y/N)\n  : ")
            if str_q == "Y" or str_q == "y" :
                sleep(uniform(0, 0.1))
                print("\n\n다시 시작합니다.")
                sleep(uniform(0, 0.1))
                break
            if str_q == "N" or str_q == "n" :
                sleep(uniform(0, 0.1))
                print("\n\n종료합니다.")
                sleep(uniform(0, 0.1))
                quit()
            else :
                print("\n\n오류! : 정해진 문자 중 하나를 입력하세요.")
    except KeyboardInterrupt :
        print("\n\n종료합니다.")
        quit()