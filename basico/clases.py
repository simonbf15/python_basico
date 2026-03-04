#clases

class persona:
    def __init__(self, nombre, apellido, altura, edad, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.edad = edad
        self.peso = peso

    def imprimir_datos(self):
        print(f'{self.nombre +' ' + self.apellido} tiene {self.edad} años, mide {self.altura} y pesa {self.peso} kilos')
        
    def comer(self):
        print(f'{self.nombre} esta comiendo')
    



#persona1 = persona('simon','barrale',1.71, 22, 63)
#persona1.imprimir_datos()
#persona1.comer()

#creo otra instancia de la clase persona
#persona2 = persona('john', 'doe', 1.51, 25, 75)
#persona2.imprimir_datos()
#persona2.comer()