def solution(N, K):
    if N == 1:
        print("\nat the beginning: 1\n")
        return 0

    if K > 0 and N % 2 == 0 and N > 2:
        round = 1 + solution(N // 2, K - 1)
        print("after the {}. round: {} (all-in)".format(round, N))
    else:
        round = 1 + solution(N - 1, K)
        print("after the {}. round: {} (he bet 1)".format(round, N))

    return round
