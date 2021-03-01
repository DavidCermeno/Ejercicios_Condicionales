# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:48:47 2021

@author: Licht
"""
# Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

camisa = float(input('Digite el número de camisas: '))
pcamisa = 25000
desc1 = (camisa * pcamisa) * 0.70
desc2 = (camisa * pcamisa) * 0.90
if camisa >= 3:
    print(f'EL total a pagar con descuento es de: {desc1}')
else:
    print(f'El total a pagar con descuento es de: {desc2}')

# En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

totalcompra = float(input('Digite total de compra: '))
numazar = int(input('Digite número escogido por el cliente 1 a 100: '))
desc1 = totalcompra * 0.85
desc2 = totalcompra * 0.80
if numazar < 74:
    print(f'El valor total a pagar con descuento es de: {desc1}')
else:
    print('El valor total a pagar con descuento es de: {desc2}')

# Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente

fianza = float(input('Digite valor de la fianza: '))
pago1 = fianza * 0.03
pago2 = fianza * 0.02
if fianza < 50000:
    print(f'El valor de la cuota a pagar es de: {pago1}')
else:
    print(f'El valor de la cuota a pagar es de: {pago2}')

# Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

contpromedio = float(input('Digite valor de la contaminación promedio: '))
gandiaria = 500000
perdida = (gandiaria * 7) * 0.50
if contpromedio <= 170:
    print('No hay sanción ni multa.')
else:
    print(f'Sanción a parar fábrica y por un valor de: {perdida}')

# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.

devauto = float(input('Digite devaluación del auto anualmente: '))
incterreno = float(input('Digite incremento del terreno anualmente: '))
auto = devauto * 3
terreno = (incterreno * 3) * 0.50
if devauto < terreno:
    print('Comprar el auto')
else:
    print('Comprar el terreno')


# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000

comprapc = int(input('Digite el número de computadoras compradas: '))
uprecio = 11000
if comprapc < 5:
    print('El valor a pagar es de: ', (comprapc * uprecio) * 0.90)
elif comprapc >= 5 and comprapc < 10:
    print('El valor total a pagar es de: ', (comprapc * uprecio) * 0.80)
else:
    print('El valor total a pagar es de: ', (comprapc * uprecio) * 0.60)

# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.

precioprod = float(input('Digite precio del producto: '))
marcaprod = input('Digite marca del producto: ')
marcaprod = "NOSY"
pt = precioprod + (precioprod * 0.16)

if precioprod < 2000:
    pf = pt
elif precioprod >= 2000 and marcaprod == "NOSY":
    desc = precioprod * 0.85
    pf = desc + (desc * 0.16)
else:
    desc = precioprod * 0.90
    pf = desc + (desc * 0.16)
print(f'El precio a pagar es de: {pf}')


# Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.

piezas = int(input('Ingrese el número de piezas: '))
vpiezas = float(input('Ingrese el valor de las piezas: '))
total = piezas * vpiezas
if total > 500000:
    invertir = total * 0.55
    prestamo = total * 0.30
    credito = total * 0.15
else:
    invertir = total * 0.70
    prestamo = 0
    credito = total * 0.30
interes = credito * 0.20
print(f'La cantidad a inveritr es de: ${invertir}')
print(f'La cantidad del préstamo es de: ${prestamo}')
print(f'La cantidad del crédito es de: ${credito}')
print(f'La cantidad de los intereses es de: ${interes}')


# Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume

num1 = float(input('Digite primer número: '))
num2 = float(input('Digite segundo número: '))
if num1 == num2:
    total = num1 * num2
elif num1 > num2:
    total = num1 - num2
else:
    total = num1 + num2

print(f'El resultado es: {total}')

# Leer tres números diferentes e imprimir el número mayor de los
# tres.

num1 = float(input('Digite el primer número: '))
num2 = float(input('Digite el segundo número: '))
num3 = float(input('Digite el tercer número: '))

if num1 > num2 and num1 > num3:
    mayor = num1
elif num1 < num2 > num3:
    mayor = num2
else:
    mayor = num3

print(f'El número mayor es: {mayor}')
















