# -*- coding: utf-8 -*-
"""成果物_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QAXImCGpqf2hnf98B7GQEtZKUQEO4qKp
"""

import random

X = int(input('所持金:'))
Y = int(input('最初の掛け金:'))
Z = int(input('目標金額:'))
N = int(input('人数:'))

W = 0
for i in range(N):
  while True:
    a = random.randrange(2)
    X -= Y

    if a == 0:
      X += 2*Y
    if X <= 0:
      print('所持金はなくなりました')
      break
    elif X < Y:
      print('掛け金が所持金を多いのでギャンブルできなくなりました')
      break

    elif X >= Z:
      print('目標金額に達成しました')
      W = W + 1
      break

print(N,'人中',W,'人が目標金額に達成しました')