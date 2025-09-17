#Creo la clase
class Estudiante:
	#Inicializo
	def __init__(self,grade):
		self.grade = grade
	#creo un método que recoja una lista según lo introducido por teclado	
	
	def media(self,notas):			
		#Actualizo el valor de grade al valor de la media de notas
	
		grade = sum(notas)/len(notas)
		print("Tu media es: ",grade)
	@staticmethod
	def suspensos(diccionario):
		
		#obtengo un nuevo diccionario con los valores de la condición solicitada e imprimo
		dic_suspensos = {materias:notas for (materias,notas) in diccionario.items() if notas<5}
		print(dic_suspensos.keys())
	#Llamo a la función para sacar el valor de grade	
		
	@classmethod
	def actualizacion(cls,nuevo_nombre):	    
			#Introduzco en una nueva variable un nuevo nombre para la escuela    
            #print(escuela)
            #nueva_escuela = input("Escribe una escuela: ")
			#Le damos el valor a la variable escuela
            cls.escuela = nuevo_nombre   

estudiante=Estudiante(5)
lista_notas=[1,2,3,5,4,8]
estudiante.media(lista_notas)
dic_resultado = {"matemáticas":3,"lengua":5,"física":8,"química":2,"dibujo":6,"inglés":9,"tecnología":4}
Estudiante.suspensos(dic_resultado)

Estudiante.actualizacion("Ilerna")
print(Estudiante.escuela)

