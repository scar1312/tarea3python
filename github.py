# Curso: Fundamentos de Tecnología Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Scarlett Fuentes

def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas."""
    return sum(notas) / len(notas)


def main():
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    print(f"El promedio es: {promedio:.2f}")

    if promedio >= 70:
        print("Aprobado")
    else:
        print("Reprobado")


if __name__ == "__main__":
    main()