Algoritmo Ejercicio_once
	Escribir "digite las tres notas de sus calificaciones parciales"
	Leer nota_uno, nota_dos, nota_tres
	Escribir "digite la calificacion del examen final: "
	Leer  examen
	Escribir "digite la nota del trabajo final"
	Leer trabajo_final
	nota_final<- (trabajo_final*15)+(examen*30)+((nota_uno+nota_dos+nota_tres/3)*55)/100
	Escribir "su nota final es: " nota_final
	
FinAlgoritmo
