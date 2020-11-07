import csv

MyName = 'cacaox'

def hello():
    print(f'こんにちは、私は{MyName}です。\n貴方は何者ですか？')

def speak2():
  print(f'{UserName}さんですか・・・貴方の職業はなんですか？')

def goodbay():
  print(f'{UserJob}の{UserName}さん、さようなら！')


hello()
while True:
  UserName = str(input()).capitalize()
  break
speak2()
while True:
  UserJob = str(input()).capitalize()
  break
goodbay()

with open('test.csv', 'w') as csv_file:
  fieldnames = ['Name', 'Job']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'Name': UserName,'Job': UserJob})