def demander_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Erreur : Entrez un nombre valide.")

def demander_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez l'opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Erreur : Opération invalide. Veuillez entrer une opération valide.")

def calculer_resultat(nombre1, nombre2, operation):
    if operation == '+':
        return nombre1 + nombre2
    elif operation == '-':
        return nombre1 - nombre2
    elif operation == '*':
        return nombre1 * nombre2
    elif operation == '/':
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            print("Erreur : Division par zéro.")
            return None

def main():
    print("Calculatrice simple")

    nombre1 = demander_nombre()
    nombre2 = demander_nombre()
    operation = demander_operation()

    resultat = calculer_resultat(nombre1, nombre2, operation)

    if resultat is not None:
        print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}.")

if __name__ == "__main__":
    main()
    