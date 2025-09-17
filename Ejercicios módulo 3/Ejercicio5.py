#Creo la clase
class Estudiante:
	#Inicializo
	def __init__(self,nombre,edad,grado):
		self.nombre = nombre
		self.edad = edad
		self.grado = grado

	#Sobrecargo el método y cambio cantidad a string	
	def __str__(self):
		return self.nombre + " " + str(self.edad) + " " + self.grado

	#Método para mostrar los atributos de la clase	
	def mostrar_atributo(self):		
		print("{} de {} esta en el gradoa {}".format(self.nombre,self.edad,self.grado))


alumno1 = Estudiante("Paco",18,"Ingeniería informática")

#Mejor visualización con tecto
alumno1.mostrar_atributo()