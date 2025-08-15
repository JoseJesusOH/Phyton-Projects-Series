
print ("Programa que calcula la comision por ventas")
print ("")

venta= float(input("Ingrese la cantidad vendida en el mes: "))

if venta>=50000:
	comision=venta*0.1
else:
	if venta>=10000:
		comision=venta*0.075
	else:
		if venta>=5000:
			comision=venta*0.05
		else:
			if venta>=1000:
				comision=venta*0.025
			else:
				comision=0

print ("\nLa comisión por la venta es de: ${0:.2f}\n".format(comision))
