#Creo la clase
class Estudiante:
	#Inicializo
	def __init__(self,grade,escuela):
		self.grade = grade
		self.escuela = escuela
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
	#Método de clase
	@classmethod
	def actualizacion(cls):	    
			#Introduzco en una nueva variable un nuevo nombre para la escuela    
            #print(escuela)
            nueva_escuela = input("Escribe una escuela: ")
			#Le damos el valor a la variable escuela
            escuela = nueva_escuela
            print(escuela)
            return escuela, cls
            
#LLamo a  la función	    
Estudiante.actualizacion()

def __asistencia():
	    #Creo las 2 listas solicitadas de mes y asistencias
    numero_asistencias = [1,2,3,4,5,6,7,8,9,10,11,12]
    mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    opcion1 = 1
    opcion2 = 2
    opcion3 = 3
    #Las junto con zip en un diccionario
    dic_asistencia = {mes:numero_asistencias for (mes,numero_asistencias) in zip(mes,numero_asistencias)}
    #print(dic_asistencia)
    #obtengo resultados en base a las condiciones solicitadas 
    for numero_asistencias in dic_asistencia.values():
		
	    if numero_asistencias<4:
		    print("Este mes tiene una asistencia de " + str(opcion1))
	    elif numero_asistencias>=4 and numero_asistencias<8:
		    print("Este mes tiene una asistencia de " + str(opcion2))
	    else:
		    print("Este mes tiene una asistencia de " + str(opcion3))			
    
__asistencia()
	
def getAsistencia(self):
    return self.__asistencia()

		
		