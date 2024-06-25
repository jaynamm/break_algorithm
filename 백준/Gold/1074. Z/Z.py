def z_order(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)

    if r < half and c < half:
        # 1사분면
        return z_order(n - 1, r, c)
    elif r < half and c >= half:
        # 2사분면
        return half * half + z_order(n - 1, r, c - half)
    elif r >= half and c < half:
        # 3사분면
        return 2 * half * half + z_order(n - 1, r - half, c)
    else:
        # 4사분면
        return 3 * half * half + z_order(n - 1, r - half, c - half)


# 입력
N, r, c = map(int, input().split())

# 출력
print(z_order(N, r, c))
