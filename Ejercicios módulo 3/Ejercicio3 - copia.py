
class Jet:
	def __init__(self, name, country, quantity=0):		
		self.name = name
		self.origin = country	
		self.quantity = quantity

	#Sobrecargo el método y cambio cantidad a string	
	def __str__(self):
		return self.name + " " + self.origin + " " + str(self.quantity)

	#Método para mostrar los atributos de la clase	
	def mostrar_atributo(self):		
		print("El nombre del avión es {} y se fabrica en {} y hay {}".format(self.name,self.origin,self.quantity))

	'''def quantity(self):
		print("Hay una cantidad de "+ str(self.quantity))'''

first_item=Jet("F16", "USA")
second_item=Jet("SU33", "Russia")
third_item=Jet("AJS37", "Sweden")
fourth_item=Jet("Mirage2000", "France", 87)
fifth_item=Jet("F14", "USA",35)
sixth_item=Jet("Mig29", "USSR")
seventh_item=Jet("A10", "USA")

#Le doy los valores indicados a las variables indicadas, se le asigna el paramétro por el constructor.
#fourth_item.quantity = 35
#fifth_item.quantity = 87

#Muestro en terminal
first_item.mostrar_atributo()
second_item.mostrar_atributo()
third_item.mostrar_atributo()
fourth_item.mostrar_atributo()
fifth_item.mostrar_atributo()
sixth_item.mostrar_atributo()
seventh_item.mostrar_atributo()