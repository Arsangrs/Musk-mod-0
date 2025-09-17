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

	#Método estático con decorador @staticmethod
	@staticmethod
	def suspensos():
		#Creo las 2 listas solicitadas
		notas = [3,5,6,6,8,2,5]
		materias = ["matemáticas","lengua","física","química","dibujo","inglés","tecnología"]
		#Las junto con zip en un diccionario
		dic_asignaturas = {materias:notas for (materias,notas) in zip(materias,notas)}
		#print(dic_asignaturas)
		#obtengo un nuevo diccionario con los valores de la condición solicitada e imprimo
		dic_suspensos = {materias:notas for (materias,notas) in dic_asignaturas.items() if notas<5}
		print(dic_suspensos)
	suspensos()