a, b, c = map(int, input().split())

dice = [0] * 7

for n in a, b, c:
    dice[n] += 1

cnt = max(dice)

if cnt == 3:
    print(10000 + (dice.index(cnt) * 1000))
elif cnt == 2:
    print(1000 + (dice.index(cnt) * 100))
elif cnt == 1:
    for i in range(6, 1, -1):
        if dice[i] == 1:
            print(i * 100)
            break