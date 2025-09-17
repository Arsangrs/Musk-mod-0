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
            cls.escuela = nuevo_nombre   
	
	def __asistencia(self,diccionario):
		solucion = 0
		for numero_asistencias in diccionario.values():
			if numero_asistencias<4:
				solucion = 1
				return solucion
			elif numero_asistencias>=4 and numero_asistencias<8:
				solucion = 2
				return solucion				
		if solucion == 0:
			solucion = 3
			return solucion
				
	def resultado_asistencia(self,diccionario):
		return self.__asistencia(diccionario)

estudiante=Estudiante(5)
lista_notas=[1,2,3,5,4,8]
estudiante.media(lista_notas)
dic_resultado = {"matemáticas":3,"lengua":5,"física":8,"química":2,"dibujo":6,"inglés":9,"tecnología":4}
Estudiante.suspensos(dic_resultado)

Estudiante.actualizacion("Ilerna")
print(Estudiante.escuela)

estudiante=Estudiante(5)
print(estudiante.resultado_asistencia({"Enero":3,"Febrero":8,"Marzo":3,"Abril":5,"Mayo":2,"Junio":9}))    	
print(estudiante.resultado_asistencia({"Enero":5,"Febrero":8,"Marzo":6,"Abril":9,"Mayo":12,"Junio":20}))  
print(estudiante.resultado_asistencia({"Enero":10,"Febrero":11,"Marzo":13,"Abril":23,"Mayo":19,"Junio":15}))  	


