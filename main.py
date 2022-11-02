from automata import *
from state import *

def main():
    # abrir arquivo
    file_name = input("Digite o nome do arquivo: ")
    file = open(file_name, "r")

    # criar estados
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")

    # criar transicoes
    q0.add_transition("0", q0)
    q0.add_transition("1", q1)

    q1.add_transition("0", q0)
    q1.add_transition("1", q2)

    q2.add_transition("0", q0)
    q2.add_transition("1", q2)

    # criar automato
    automata = Automata("01", q0, [q2])

    # verificar se o automato aceita o arquivo
    if automata.accepts(file):
        print("Aceito")
    else:
        print("Rejeitado")

    # fechar o arquivo
    file.close()

if __name__ == '__main__':
    main()