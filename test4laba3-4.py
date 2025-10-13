'''a = int(input('Это високосный год? Введите год '))
if a%400==0 or a%4 == 0 and a%100 != 0:
  print('да')
else:
  print('нет')'''  # 1 способ

a = int(input('Это високосный год? Введите год '))
if a%4 == 0:
  if a%100 == 0:
    if a%400 == 0:
      print("да")
    else:
      print("нет")
  else:
    print("да")
else:
  print("нет")  # 2 способ