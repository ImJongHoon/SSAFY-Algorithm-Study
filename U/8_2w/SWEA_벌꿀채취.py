'''
dfs로 풀어야할 거 같은데
감이 안 잡히네 이거 어캄?
'''

import sys
sys.stdin = open('honey_input.txt', 'r')

T = int(input())


def search():

    # 인덱스로 꿀 리스트에 접근
    for idx, honey_list in enumerate(honey_board):
        for i in range(0, N-M+1):
            a_pick = honey_list[i:i+M]  # 첫 번째 일꾼이 고를 수 있는 꿀통 리스트
            # print(a_pick)




for tc in range(1, T+1):
    # 벌통의 크기 N / 선택할 수 있는 벌통 수 M / 꿀을 채취할 수 있는 최대 양 C
    N, M, C = map(int, input().split())
    honey_board = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, C, honey_board)
    max_honey_income = -1
    

    search()