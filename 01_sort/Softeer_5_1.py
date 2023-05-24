import sys
input = sys.stdin.readline
"""
### Softeer : 인증평가 5차 기출 - 성적 평가

[https://softeer.ai/practice/info.do?idx=1&eid=1309&sw_prbl_sbms_sn=169357](https://softeer.ai/practice/info.do?idx=1&eid=1309&sw_prbl_sbms_sn=169357)

list를 활용하면 시간초과 걸리니까, 적절하게 딕셔너리 사용해야함.
"""

def solution():
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(3)]
    sum = [0] * (n)
    rank = []
    tot_rank = []

    for sc in score:
        rank_dict = dict()
        idx = 0
        answer = []
        for s in sorted(sc, reverse=True):
            idx += 1
            if not s in rank_dict:
                rank_dict[s] = idx

        for i in range(len(sc)):
            answer.append(rank_dict[sc[i]])
            sum[i] += sc[i]

        print(*answer)

    rank_dict = {}
    idx = 0
    answer = []
    for s in sorted(sum, reverse=True):
        idx += 1
        if not s in rank_dict:
            rank_dict[s] = idx

    for i in range(len(sum)):
        answer.append(rank_dict[sum[i]])

    print(*answer)

solution()