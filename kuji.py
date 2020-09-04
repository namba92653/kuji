import numpy.random as random

a=random.randint(1,101)

if a == 1:
    str = "大大吉"

elif 2<=a and a<= 20:
    str = "大吉"

elif 21<=a and a<= 50:
    str = "吉"

elif 51<=a and a<= 65:
    str = "中吉"

elif 66<=a and a<=80:
    str = "小吉"

elif 81<=a and  a<=90:
    str = "末吉"

elif 91<=a and  a<=97:
    str = "凶"

else:
    str = "大凶"

print(str)
