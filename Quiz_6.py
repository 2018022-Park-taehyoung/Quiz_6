RRN = input("-를 제외한 주민번호를 입력하시오: ")
RRN_list = list(RRN)
last = int(RRN_list[-1])
del RRN_list[-1]
a = 2
sum = 0
if len(RRN) == 13:
    for number in RRN_list:
        element= int(number) * a
        if a < 9:
            a += 1
        else:
            a = 2
        sum += element
    result = 11 - (sum % 11)
    if result == last:
        print("유효한 주민번호입니다.")
    else:
        print("유효하지 않은 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
