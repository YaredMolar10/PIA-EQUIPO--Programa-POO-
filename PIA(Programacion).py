print("PROGRAMA 1 (Descuento)---------------------------------------------------------------------------------------------------")
class Tres_programas:
    
    def __init__(self, compra):
        self.compra = compra
        self.pagar = 0
    
    def descuento_clientes(self):
        if self.compra < 500:
            self.pagar = self.compra 
            print("No tiene descuento")
            print(f"Monto a pagar: {self.pagar}")
            
        elif self.compra >= 500 and self.compra <=1000:
            descuento = self.compra * 0.05
            self.pagar = self.compra - descuento
            print(f"Tiene desucento del %5. Usted ahorro: {descuento}")
            print(f"Monto a pagar: {self.pagar}")
            
        elif self.compra >= 1000 and self.compra <=7000:
            descuento = self.compra * 0.11
            self.pagar = self.compra - descuento
            print(f"Tiene descuento del %11. Usted ahorro: {descuento}")
            print(f"Monto a pagar: {self.pagar}")
            
        elif self.compra >=7000 and self.compra <=15000:
            descuento = self.compra * 0.18
            self.pagar = self.compra - descuento
            print(f"Tiene descuento del %18. Usted ahorro: {descuento}")
            print(f"Monto a pagar: {self.pagar}")
            
        elif self.compra >15000:
            descuento = self.compra * 0.25
            self.pagar = self.compra - descuento
            print(f"Tiene descuento del %25. Usted ahorro: {descuento}")
            print(f"Monto a pagar: {self.pagar}") 

# Crear una lista con los valores de compra para cada corrida
compras = [3500, 6850, 375.80, 690.50, 12350, 25314.18, 3750, 14200.50, 895.80, 1318.50]

# Crear y ejecutar una instancia de Tres_programas para cada compra
for i, compra in enumerate(compras, start=1):
    print(f"Corrida numero {i}")
    corrida = Tres_programas(compra)
    corrida.descuento_clientes()
    print()


print("Programa 2(DINOSUARIOS)-----------------------------------------------------------------------------------")

class Tres_Programas:
    contador = 1  

    def __init__(self, nom, pes, lon):
        self.nom = nom
        self.pes = pes
        self.lon = lon

    def dinosaurios(self):
        self.peskil = self.pes * 1000
        self.lonmet = self.lon * 0.3047
        print(f"{Tres_Programas.contador}. Dinosaurio: {self.nom}, Peso: {self.pes}, Longitud: {self.lon}, Peso en kilos: {self.peskil}, Longitud en metros: {self.lonmet}")
        Tres_Programas.contador += 1  
    
#tabla 1.6

plateosaurus = Tres_Programas("PLATEOSAURUS", 5, 30)
diplojocus = Tres_Programas("DIPLOJOCUS", 15, 90)
brachiosaurus = Tres_Programas("BRACHIOSAURUS", 50, 80)
brontosaurus = Tres_Programas("BRONTOSAURUS", 25, 70)
tryanmosaurus = Tres_Programas("TRAYNMOSAURUS", 8, 30)

plateosaurus.dinosaurios()
diplojocus.dinosaurios()
brachiosaurus.dinosaurios()
brontosaurus.dinosaurios()
tryanmosaurus.dinosaurios()
print("Programa 3-(Gasolina)----------------------------------------------------------------------------------------")



class Tres_programas:
    contador = 1  # Atributo de clase para llevar la cuenta de las corridas

    def __init__(self, gal):
        self.gal = gal

    def gasolina(self):
        self.total = self.gal * 3.785 * 8.20
        print(f"{Tres_programas.contador}. Galones: {self.gal}, TOTAL: {self.total}")
        Tres_programas.contador += 1  # Incrementar el contador


corrida1 = Tres_programas(10.38)
corrida2 = Tres_programas(15.90)
corrida3 = Tres_programas(8.40)
corrida4 = Tres_programas(9.66)
corrida5 = Tres_programas(19.90)

corrida1.gasolina()
corrida2.gasolina()
corrida3.gasolina()
corrida4.gasolina()
corrida5.gasolina()


print("------------------------------------------------------------------------------------------------------------")