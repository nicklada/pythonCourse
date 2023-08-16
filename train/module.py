import self
from param import selectBiggest

Gopher  = self.ITshnik('Yarik', 28)
Gopher.speak()

Tester = self.ITshnik('Ladka', 29)
Tester.speak()

older = selectBiggest(Gopher.age, Tester.age)
print('Старшему из айтишников -  {} лет'.format(older))