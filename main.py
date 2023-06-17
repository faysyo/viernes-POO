from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("----------Herencia alumno--------------")
    al1 = Alumno("Jose", 19, "5562578682", "ICO")
    print(al1)
    print(Alumno.descripcion)
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)

    al2.dormir()

    print("----------herencia profe--------------")
    profe1 = Profesor("Jesus", 30 + 16, 420120982,"Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("----------Herencia ayudante profe----------------")
    ayudante = AyudanteProfesor("Adrian", 20, "42012456", "ICO0", 45265, "Ing. Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")


main()