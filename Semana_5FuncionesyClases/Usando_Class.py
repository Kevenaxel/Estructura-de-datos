class Coche:
    def __init__(self, gasolina):        
        self.gasolina = gasolina
        print("Tenemos", self.gasolina, "Galones")
        
    def arrancar(self):
        if self.gasolina > 0:
            print("El coche arranca")
        else:
            print("No hay Gasolina, no arranca")
            
            
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print(("Conduciendo queda...", self.gasolina, "Galones"))
        else:
            print("No se mueve, no tiene Gasolina")
            
            
mi_carro = Coche(3)
mi_carro.arrancar()
mi_carro.conducir()