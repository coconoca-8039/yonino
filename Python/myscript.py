# import module
# module.myfunc()
# print(module.myvariable)

from module import yourfunc
from module import myvariable
yourfunc()

import module
print(module.anotherfunc())

#非推奨
# 何がインポートされるかわからないから
#from module import *