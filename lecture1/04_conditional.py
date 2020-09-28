#!/usr/bin/env python3

x = int(input("x: "))
y = int(input("y: "))

#if y > 0:
#    if x > 0:
#        print(1)
#    else:
#        print(2)
#else:
#    if x > 0:
#        print(4)
#    else:
#        print(3)


# Вариант ветвления с логическими операциями

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("Чёт ты попутал с координатами.")
