class Jet:
	def __init__(self, name, country):		
		self.name = name
		self.origin=country	
	#Método para mostrar los atributos de la clase		
	def mostrar_atributo(self):
		print("El nombre del avión es {} y se fabrica en {}".format(self.name,self.origin))	

first_item=Jet("F16", "USA")
second_item=Jet("SU33", "Russia")
third_item=Jet("AJS37", "Sweden")
fourth_item=Jet("Mirage2000", "France")
fifth_item=Jet("F14", "USA")
sixth_item=Jet("Mig29", "USSR")
seventh_item=Jet("A10", "USA")

#Llamada al método para mostrar los atributos de la variable solicitada
second_item.mostrar_atributo()

