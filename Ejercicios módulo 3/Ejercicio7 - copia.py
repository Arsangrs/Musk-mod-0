
#Creo la clase
class Estudiante:
	
	#Inicializo
	def __init__(self,grade):
		
		self.grade = grade
		
	#creo un método que recoja una lista según lo introducido por teclado	
	def media(self,notas):
			
		#Actualizo el valor de grade al valor de la media de notas
		#estudiante = "Pepe"
		grade = sum(notas)/len(notas)
		print("Tu media es: ",grade)

	#Llamo a la función para sacar el valor de grade	
estudiante=Estudiante(5)
lista_notas=[1,2,3,5,4,8]
estudiante.media(lista_notas)


