Algoritmo Ejercicio_diecisiete
	Escribir "escriba las velocidades 1 y 2 en km/h: "
	Leer v_uno, v_dos
	Escribir "escriba la distancia entre ellos en Km: "
	Leer distancia
	velocidad<-v_uno-v_dos
	Si velocidad = 0 Entonces
		tiempo<- distancia/(abs(velocidad)+1)
	SiNo
		tiempo<- distancia/(abs(velocidad))
	Fin Si
	tiempo<-(tiempo*60)

	Escribir "se encuentran en " tiempo " minutos"
	
FinAlgoritmo
