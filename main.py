
def main():
    # abrir arquivo
    file_name = input("Digite o nome do arquivo: ")
    file = open(file_name, "r")
    lines = file.readlines()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "+-*/=(),;!><"
    alphabet = letters + numbers + symbols + " " + "\n"
    state = 0
    token = ""
    reserveds = ["if", "else", "return", "void", "while", "int"]
    reserved_symbols = ["<=", "<", ">=", ">", "==", "!=", "+", "-", "*", "/", "=", ";", ",", "(", ")", "/*", "*/"]
    
    # uma das ideias do roberto
    for line in lines:
        tokens = line.split()
        for token in tokens:
            if token in reserveds:
                print("Reservada: ", token)
            elif token in reserved_symbols:
                print("Simbolo: ", token)
            else:
                continue
                


if __name__ == '__main__':
    main()