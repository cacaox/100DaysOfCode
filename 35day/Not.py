x = int(input())
if x == 0:
  print(1)
else:
  print(0)

#2  こちらの方が4byte重いが、実行時間は2ms早い
x = int(input())
if x is not 1:
  print(1)
else:
  print(0)