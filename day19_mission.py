def transfer(c, n):
    """
    n을 입력받아서 c진수로 바꾸는 함수
    :param c: 10진법에서 바꿀 진수
    :param n: 바꿀 숫자
    :return: c진법으로 바꾼 수
    """

    if c > n : # 나머지가 나올때
        print(number_char[n],end='')
    else:
        transfer(c, n//c)
        print(number_char[n%c],end='')
#전역변수 설정
number_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

if __name__ == "__main__" :

    en_num = int(input('10진수 입력 -->'))

    print(f'2진수 : ',end='')
    transfer(2, en_num)
    print()
    print(f'8진수 : ',end='')
    transfer(8, en_num)
    print()
    print(f'16진수 : ',end='')
    transfer(16, en_num)
    print()