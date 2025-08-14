
print ("Programa que indica si un año es bisiesto o no ")

año =int(input("\nIngresa el año que desea consultar: "))

if ((año %4 == 0 and año %100!=0) or año %400==0):
	print ('\n',año, " es un año bisiesto")
else:
	print ('\n',año," no es un año bisiesto")

