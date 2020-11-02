n = int(input()) - 3
s = list(map(str, input().split()))
cnt = 0
for i in range(n):
  if s[i] == 'A' and s[i+1] == 'B' and s[i + 2] == 'C':
    cnt += 1
print(cnt)