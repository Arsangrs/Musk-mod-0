
#Creo la clase
class Estudiante:
	#Inicializo
	def __init__(self,grade):
		self.grade = grade
	#creo un método que recoja una lista según lo introducido por teclado	
	def media():
		notas = []
		while True:
			
			nota = int(input("Pon tu nota del 0 al 10 o usa cualquier otro número para salir: "))
			#Condición para salir del bucle en caso de que na nota no esté entre los parámetros indicados
			if nota > 10 or nota <0:
				break
			#Recojo la lista
			notas.append(nota)			
			
		#Actualizo el valor de grade al valor de la media de notas
		grade = sum(notas)/len(notas)
		print("Tu media es: ",grade)
	#Llamo a la función para sacar el valor de grade	
	media()


#Creo la clase
class Estudiante:
	#Inicializo
	def __init__(self,grade):
		self.grade = grade
	#creo un método que recoja una lista según lo introducido por teclado	
	def media():
		notas = []
		#Lo mismo pero usando try/except para controlar que se introduzca un número
		while True:
			try:
				nota = int(input("Pon tu nota del 0 al 10 o usa cualquier otro número para salir: "))
				#Condición para salir del bucle en caso de que na nota no esté entre los parámetros indicados
				if nota > 10 or nota <0:
					break
				#Recojo la lista
				notas.append(nota)
			#Excepción en caso de que no se ponga un número
			except ValueError:
				print("Inserta un número.")
		#Actualizo el valor de grade al valor de la media de notas
		grade = sum(notas)/len(notas)
		print("Tu media es: ",grade)
	#Llamo a la función para sacar el valor de grade	
	media()