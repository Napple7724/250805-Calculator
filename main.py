##### [ 계산기 ]
##### Calculator in python by Napple7724 on August 5, 2025
##### Version : release 2.1.1
#################################################################
## 실행하기 전 "README.md"와 "LICENSE.md"를 읽어주세요.
## Please read "README.md" and "LICENSE.md" before running.


from calc_api import calc_api  ## calc_api.py

from sys import exit as sys_exit
from time import sleep
from random import uniform

print("Loading...")
sleep(uniform(0.3, 0.5))
while True :
    try :
        print("\n\n[ 계산기 ]\nCalculator in python by Napple7724 on August 5, 2025\nVersion : release 2.1.1\n")
        sleep(uniform(0.03, 0.1))
        while True :
            try :
                list_num = list(map(int, input("숫자를 공백으로 나눠 입력하세요.\n  : ").split()))
                if len(list_num) >= 2 :
                    break
                else :
                    print("\n\n오류! : 항목을 2개 이상 입력하세요.")
            except ValueError :
                print("\n\n오류! : 숫자를 입력하세요.")
            sleep(uniform(0.03, 0.1))
        print("\n")
        print(f"\n\n :: {calc_api(list_num)}")
    except KeyboardInterrupt :
        print("\n\n종료합니다.")
        break
    except :
        print("\n\n오류! : 알 수 없는 오류가 발생했습니다.")
    print("\n")
    try :
        while True :
            sleep(uniform(0.03, 0.1))
            str_q = input("계속 하시겠습니까? (Y/N)\n  : ")
            if str_q == "Y" or str_q == "y" :
                sleep(uniform(0.03, 0.1))
                print("\n\n다시 시작합니다.")
                sleep(uniform(0.03, 0.1))
                break
            if str_q == "N" or str_q == "n" :
                sleep(uniform(0.03, 0.1))
                print("\n\n종료합니다.")
                sleep(uniform(0.03, 0.1))
                sys_exit()
            else :
                print("\n\n오류! : 정해진 문자 중 하나를 입력하세요.")
    except KeyboardInterrupt :
        print("\n\n종료합니다.")
        break