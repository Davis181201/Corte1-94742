# -*- coding: utf-8 -*-
"""sesion_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x2Q-lM9JmIMUE8VfxissRatiKRwHM9RY
"""

print('¿Que operación desea realizar?:\n')
print('1. Imprimir numeros impares hasta el valor proporcionado. ')
print('2. Calcular numero factorial. ')
print('3. Saber si un numero es primo.')


d = input('¿Que opcion va a escoger? ')




if d == '1':
  n = int(input("Introduce un número entero positivo: "))
  for n in range(1, n+1, 2):
    print(n, end=", ")



elif d == "2":
  n=int(input("Numero Factorial : "))
  f=1
  for i in range(1,n+1):
    f*=i
  print("El Numero Factorial de ",n, "es ",f)



elif d == "3":
  num=int(input("Ingrese un Numero :"))
  if num > 1:
    contador=0
    for i in range(2,num):
      r=num % i
      
      if r ==0:
        contador+=1
    if contador ==0:
      print("El Numero",num, "Es primo \n")
    else:
      print("El Numero",num, "No es primo \n")
  
  print("Los Numeros Primos anteriores al asignado son :")
  for num in range(1,num):
    if num > 1:
      contador = 0
      i = 2
      while i < num and contador==0:
        r=num%i
        if r ==0:
          contador+=1
        i+=1
      if contador==0:
        print("los Numeros primos anteriores son",num)


else:
  print("El Numero ingresado no es valido")