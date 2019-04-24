print("Вас приветствует калькуптер сделанный Малой Корпорации Leva_net")
from math import *
flag=1
def multiply_chisel():
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    print("Результатом умножения будет:",a*b)
def vozved_v_stepen():
    a=int(input("Введите число для возведения его в степень "))
    b=int(input("Введите степень для числа "))
    print("Результатом возведения в степень будет:",a**b)
def delenie():
    a=int(input("Введите делимое "))
    b=int(input("Введите делитель "))
    print("Результатом деления будет:",a/b)
def summa():
    a=int(input("Введите первое число "))
    b=int(input("Введите добавляемое число "))
    print("Результатом суммы будет: ",a+b)
def raznost():
    a=int(input("Введите первое число "))
    b=int(input("Введите отнимаемое число "))
    print("Результатом суммы будет: ",a-b)
def discount():
    a=int(input("Введите целое число "))
    b=int(input("Введите какой процент от числа вы хотите взять "))
    print("Процент ",b," от числа ",a," равен",a/100*b)
def koren():
    a=int(input("Введите число от которого вы хотите взять корень "))
    print("Корень числа ",a," равен",sqrt(a))
def cosCH():
    a=int(input("Введите число "))
    print("cos числа:",cos(a))
def sinCH():
    a=int(input("Введите число "))
    print("cos числа:",sin(a))
    
while flag==1:
    
    c=input("Введите знак математического действия:")
    if c=="-^":
        koren()
    if c=="sin":
        sinCH()
    if c=="cos":
        cosCH()
    if c=="%":
        discount()
    if c=="^":
        vozved_v_stepen()
    if c=="*":
        multiply_chisel()
    elif c=="/":
        delenie()
    elif c=="+":
        summa()
    elif c=="-":
        raznost()
    print("Хотите завершить работу? если да, то нежно жмякните на 2")
    n=int(input("Введите 2 или любой другой символ, чтобы продолжить "))
    if n==2:
        flag+=1
        print("Спасибо, что использовали мой калькулятор для ваших бизнес-идей!")
    
