'''
chapter04_indexing -> main.py

문자열 인덱싱(indexing)
print(type("안녕하세요"))를 실행했을 때
<class 'str'> 나오는 것을 확인할 수 있습니다.
str이란 String의 줄임말로 '줄'이란 의미를 가지고 있음.
index란: 문자열을 구성하는 문자에 부여한 고유의 번호. 시작 번호는 0
01234
'''
# name = "정원재"
#
# print(name[0])
# print(name[1])
# print(name[2])
# # print(name[3])
# # print(name[4])
# print()
# print(name[-1])
# print(name[-2])
# print(name[-3])

'''
문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나
    문자열 추출할 때 사용하는 방법
    추출하고자 하는 단어난 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을
    추출하는 방법
    
형식 : a[시작인덱스:종료인덱스:증감값]
'''
# print(name[:2:])
# b='banana'
# print(b[:4:2]) #bn
#
'''
기본 예시

네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리를 출력하시오.
실행 예시
네 자리 숫자를 입력하세요 >>> 2024
맨 마지막 자리의 숫자는 4입니다.
맨 마지막 자리의 숫자는 4이고, 맨 마지막 자리의 숫자는 짝수입니다.

'''
#
# num = int(input("네 자리 숫자를 입력하세요 >>> "))
# print('멘 마지막 자리의 숫자는 %d입니다.' % num)
# if num % 2 == 0:
#     print('멘 마지막 자리의 숫자는 %d이고, 맨 마지막 자리의 숫자는 짝수입니다.')
# else:
#     print('맹')


















