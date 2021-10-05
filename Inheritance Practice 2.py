# Importing from files / inheritance 2

from InheritancePractice1 import Chef
from InheritancePractice1 import ChineseChef
from InheritancePractice1 import ChineseChef2

myChef1 = Chef()
myChef1.make_salad()
myChef1.make_special()

myChef2 = ChineseChef()
myChef2.make_friedrice()
myChef2.make_special()

myChef3 = ChineseChef2()
myChef3.make_friedrice()
myChef3.make_special()
