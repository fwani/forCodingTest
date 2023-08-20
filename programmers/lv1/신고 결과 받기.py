# https://school.programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict


def solution(id_list, report, k):
    reported_users = defaultdict(set)
    for user_report in report:
        user, reported_user = user_report.split(" ")
        reported_users[reported_user].add(user)
    block_user = []
    alarm = defaultdict(int)
    for reported_user, report_user in reported_users.items():
        if len(report_user) >= k:
            block_user.append(reported_user)
            for user in report_user:
                alarm[user] += 1

    answer = []
    for user in id_list:
        answer.append(alarm[user])
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
               2))  # [2,1,1,0]
print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))  # [0,0]
