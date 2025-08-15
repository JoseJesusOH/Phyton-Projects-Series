from Mesa import Mesa
from MesaRectangular import MesaRectangular
from MesaRedonda import MesaRedonda

mesas_disponibles = [
    MesaRectangular(50.0, 1.0, 1.0, 30.0), 
    MesaRectangular(70.0, 1.0, 1.2, 40.0), 
    MesaRectangular(100.0, 1.2, 1.5, 50.0),
    MesaRedonda(50.0, 0.50, 200.0),
    MesaRedonda(70.0, 0.60, 250.0),
    MesaRedonda(100.0, 0.75, 500.0)
]

for i, mesa in enumerate(mesas_disponibles):
    print("--------------------------------------------------------")
    print(f"Mesa {i+1}: {mesa}")
    print(f"Area de cubierta: {mesa.calculaArea()}")
    print(f"Costo de mesa: {mesa.calculaCosto()}\n")
