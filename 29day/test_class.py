class Test(object):
  def __init__(self, num):
    self.num = num

  def number(self):
    print(f'入力された番号は{self.num}です')

test = Test(6)
test.number()
