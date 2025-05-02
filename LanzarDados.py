import random
import sys

class Dado:
    def __init__(self):
        self.valor = None
        self.lanzar()

    def lanzar(self):
        self.valor = random.randint(1, 6)

    def __repr__(self):
        return str(self.valor)

class ManoDados:
    def __init__(self, num_dados=5):
        self.dados = [Dado() for _ in range(num_dados)]

    def lanzar(self, indices=None):
        if indices is None:
            indices = range(len(self.dados))
        for i in indices:
            self.dados[i].lanzar()

    def mostrar(self):
        # ⬇️  Ya no mostramos el número de dado, solo su valor
        return ' '.join(f"[{dado.valor}]" for dado in self.dados)

def pedir_indices():
    entrada = input(
        "¿Qué dados vuelves a tirar? (posiciones 1-5 separadas por espacio/coma, Enter = ninguno): "
    )
    if not entrada.strip():
        return []
    partes = [p.strip() for p in entrada.replace(',', ' ').split()]
    indices = []
    for p in partes:
        if p.isdigit():
            n = int(p)
            if 1 <= n <= 5:
                indices.append(n - 1)
    return list(dict.fromkeys(indices))       # quita duplicados

def juego():
    mano = ManoDados()

    print("\n=== PRIMER LANZAMIENTO ===")
    print(mano.mostrar())

    for intento in range(2, 4):               # lanzamientos 2 y 3
        indices = pedir_indices()
        if indices:
            mano.lanzar(indices)
        print(f"\n=== LANZAMIENTO {intento} ===")
        print(mano.mostrar())

    print("\n>>> Resultado final:", mano.mostrar())

def menu():
    while True:
        print("\n======= MENÚ =======")
        print("1) Lanzar dados")
        print("2) Salir")
        opcion = input("Selecciona una opción (1/2): ").strip()
        if opcion == '1':
            juego()
        elif opcion == '2':
            print("Hasta la próxima.")
            sys.exit()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
