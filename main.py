try :
    print("\n")
    while True :
        try :
            list_num = list(map(int, input("숫자를 공백으로 나눠 입력하세요.\n  : ").split()))
            if len(list_num) >= 2 :
                break
            else :
                print("\n\n오류! : 항목을 2개 이상 입력하세요.")
        except ValueError :
            print("\n\n오류! : 숫자를 입력하세요.")
    print("\n")
    while True :
        str_sign = input("부호(+, -, *, /, ^)를 입력하세요.\n  : ")
        if str_sign == "+" :
            int_a = sum(list_num)
            break
        elif str_sign == "-" :
            int_a = list_num[0]
            for sys_int_r1 in range(1, len(list_num) + 1) :
                int_a -= list_num[sys_int_r1]
        elif str_sign == "*" :
            int_a = list_num[0]
            for sys_int_r1 in range(1, len(list_num) + 1) :
                int_a *= list_num[sys_int_r1]
        else :
            print("\n\n오류! : 정해진 부호 중 하나를 입력하세요.")
except ZeroDivisionError :
    print("오류! : 알 수 없는 오류가 발생했습니다.")