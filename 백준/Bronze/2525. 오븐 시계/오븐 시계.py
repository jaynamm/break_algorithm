hour, minute = map(int, input().split())
t = int(input())

if 0 <= minute and (minute + t) < 60:
    print(hour, minute + t)
elif (minute + t) >= 60:
    hour += (minute + t) // 60
    if hour > 23:
        print((hour - 24), (minute + t) % 60)
    else:
        print(hour, (minute + t) % 60)