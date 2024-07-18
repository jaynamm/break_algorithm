def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA

n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:] # 진실을 아는 사람들
parent = list(range(n + 1)) # 1-indexed

# 파티 정보를 저장합니다
parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for i in range(len(party) - 1):
        union(parent, party[i], party[i + 1])


# 진실을 아는 사람들과 연결된 모든 사람들을 찾습니다
truth_root = {find(parent, t) for t in truth}

# 모든 파티를 검사하여 거짓말할 수 있는 파티 수를 계산합니다
lie_possible = 0
for party in parties:
    if not any(find(parent, p) in truth_root for p in party):
        lie_possible += 1

print(lie_possible)
