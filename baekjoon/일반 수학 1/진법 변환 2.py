# https://www.acmicpc.net/problem/2745
# # 문제
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
# # 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.
# # 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.
# # 예제 입력 1
# 60466175 36
# # 예제 출력 1
# ZZZZZ
import string

data = string.digits + string.ascii_uppercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return data[r]
    else:
        return convert(q, base) + data[r]


s = input()
num, base = s.split(" ")

print(convert(int(num), int(base)))
