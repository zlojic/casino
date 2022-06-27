def solution(N, K):
    if K == 0 or N <= 2:
        return N - 1

    if N % 2 == 0:
        round = 1 + solution(N // 2, K - 1)
    else:
        round = 1 + solution(N - 1, K)

    return round
