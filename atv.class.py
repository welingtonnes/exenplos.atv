class carro:
  pneus = 4 # atributo de classe
  def __init__ (self, marca, modelo):
        self.marca = modelo
        self.modelo = modelo

carro1 = carro("Ford", "Fiesta")
carro2 = carro("Honda", "Civic")

print(carro1.pneus)
print(carro2.pneus)

print(carro.pneus)