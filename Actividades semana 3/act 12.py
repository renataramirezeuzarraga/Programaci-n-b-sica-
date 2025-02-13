#12. Encontrar el mayor entre tres números dados.

num1=float (input("Ingresa el primer número: "))
num2=float (input("Ingresa el segundo número: "))
num3=float (input("Ingresa el tercer número: "))

if num1>=num2 and num2>=num3:
    print (f"El mayor número es: ",num1)

elif num2>=num1 and num1>=num3:
      print (f"El mayor número es: ",num2)

else:
      print (f"El mayor número es: ",num3)