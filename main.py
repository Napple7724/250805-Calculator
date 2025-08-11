##### [ 계산기 ]
##### Calculator in python by Napple7724 on August 5, 2025
##### Version : release 2.2
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
        print("\n")
        sleep(uniform(0.01, 0.3))
        print("[ 계산기 ]")
        sleep(uniform(0.01, 0.3))
        print("Calculator in python by Napple7724 on August 5, 2025")
        sleep(uniform(0.01, 0.3))
        print("Version : release 2.2")
        sleep(uniform(0.01, 0.3))
        print("실행중에는 [^C] 키를 눌러 종료할 수 있습니다.")
        sleep(uniform(0.01, 0.3))
        print()
        sleep(uniform(0.03, 0.1))
        while True :
            try :
                print("숫자를 공백으로 나눠 입력하세요.")
                sleep(uniform(0.01, 0.3))
                list_num = list(map(int, input("  : ").split()))
                if len(list_num) >= 2 :
                    break
                else :
                    print("\n")
                    sleep(uniform(0.01, 0.3))
                    print("오류! : 항목을 2개 이상 입력하세요.")
            except ValueError :
                print("\n")
                sleep(uniform(0.01, 0.3))
                print("오류! : 숫자를 입력하세요.")
            sleep(uniform(0.03, 0.1))
        print("\n")
        sleep(uniform(0.01, 0.3))
        print(f"\n\n :: {calc_api(list_num)}")
    except KeyboardInterrupt :
        print("\n")
        sleep(uniform(0.01, 0.3))
        print("종료합니다.")
        break
    except :
        print("\n")
        sleep(uniform(0.01, 0.3))
        print("오류! : 알 수 없는 오류가 발생했습니다.")
        break
    print("\n")
    sleep(uniform(0.01, 0.3))
    try :
        while True :
            sleep(uniform(0.03, 0.1))
            print("계속 하시겠습니까? (Y/N)")
            sleep(uniform(0.01, 0.3))
            str_q = input("  : ")
            if str_q == "Y" or str_q == "y" :
                sleep(uniform(0.03, 0.1))
                print("\n\n")
                sleep(uniform(0.01, 0.3))
                print("다시 시작합니다.")
                sleep(uniform(0.03, 0.1))
                break
            if str_q == "N" or str_q == "n" :
                sleep(uniform(0.03, 0.1))
                print("\n")
                sleep(uniform(0.01, 0.3))
                print("종료합니다.")
                sleep(uniform(0.03, 0.1))
                sys_exit()
            else :
                print("\n")
                sleep(uniform(0.01, 0.3))
                print("오류! : 정해진 문자 중 하나를 입력하세요.")
    except KeyboardInterrupt :
        print("\n")
        sleep(uniform(0.01, 0.3))
        print("종료합니다.")
        break
    # except :
    #     print("\n")
    #     sleep(uniform(0.01, 0.3))
    #     print("오류! : 알 수 없는 오류가 발생했습니다.")
    ## 해당 부분을 코드에 삽입할 경우 원인을 알 수 없는 오류 발생