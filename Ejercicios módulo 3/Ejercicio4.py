#Creo la clase
class Nobel:
	#Inicializo
	def __init__(self,category,year,winner):
		self.category = category
		self.year = year
		self.winner = winner

	#Sobrecargo el método y cambio cantidad a string	
	def __str__(self):
		return self.category + " " + str(self.year) + " " + self.winner

	#Método para mostrar los atributos de la clase	
	def mostrar_atributo(self):		
		print("El premio de la {} en el año {} fue para {}".format(self.category,self.year,self.winner))


np2005 = Nobel("Peace",2005,"Muhammad Yunus")

print(np2005.category,np2005.year,np2005.winner)

#Mejor visualización con tecto
np2005.mostrar_atributo()