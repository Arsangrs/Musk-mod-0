#Ejercicio 1

class Jet:
	def __init__(self, name, country):		
		self.name = name
		self.origin=country
		
'''first_item=Jet("F16", "USA")
print(first_item.name)'''
#Método para mostrar el atributo name de la clase
	def mostrar_atributo(self):
		print("El primer atributo es {}".format(self.name))

first_item=Jet("F16", "USA")

print(first_item.name)
