n = int(input())
s = list(map(str, input().split()))
cnt = 0
for i in range(n - 3):
  if s[i] == 'A' and s[i+1] == 'B' and s[i + 2] == 'C':
    cnt += 1
print(cnt)