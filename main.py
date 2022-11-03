class Automata:
    def __init__(self):
        self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.symbols = "+-*/=(),;!><}{"
        self.end_tokens = " \n"
        self.alphabet = self.letters + self.numbers + self.symbols + self.end_tokens
        self.reserveds = ["if", "else", "return", "void", "while", "int"]
        self.reserved_symbols = ["<=", "<", ">=", ">", "==", "!=", "+", "-", "*", "/", "=", ";", ",", "(", ")", "/*", "*/", "{", "}"]



    def init_state(self, file):
        token = ""

        while symbol := file.read(1):
            if symbol in self.end_tokens:
                token = ""
            elif symbol in self.letters:
                token += symbol
                return self.id_state(file, token)
            elif symbol in self.numbers:
                token += symbol
                return self.number_state(file, token)
            elif symbol in self.symbols:
                token += symbol
                return self.symbol_state(file, token)
            else:
                print("Token inválido: ", symbol)
                return False
        return True

    def id_state(self, file, token):
        symbol = file.read(1)
        if not symbol:
            # terminou o arquivo
            if token in self.reserveds:
                print ("Token reservado: ", token)
            else:
                print ("Token identificador: ", token)
            return self.init_state(file)
        elif symbol in self.letters or symbol in self.numbers:
            # continua o identificador
            token += symbol
            return self.id_state(file, token)
        else:
            if token in self.reserveds:
                print ("Token reservado: ", token)
            else:
                print ("Token identificador: ", token)
            file.seek(file.tell() - 1)
            return self.init_state(file)
    
    def number_state(self, file, token):
        symbol = file.read(1)
        if not symbol:
            # terminou o arquivo
            print ("Token número: ", token)
            return self.init_state(file)
        elif symbol in self.numbers:
            # continua o número
            token += symbol
            return self.number_state(file, token)
        else:
            print ("Token número: ", token)
            file.seek(file.tell() - 1)
            return self.init_state(file)

    def symbol_state(self, file, token):
        symbol = file.read(1)
        if not symbol:
            # terminou o arquivo
            print ("Token símbolo: ", token)
            return self.init_state(file)
        elif token + symbol in self.reserved_symbols:
            # continua o símbolo
            token += symbol
            return self.symbol_state(file, token)
        else:
            print ("Token símbolo: ", token)
            file.seek(file.tell() - 1)
            return self.init_state(file)

def main():
    # abrir arquivo
    file_name = "sample.c"
    # state = 0
    with open(file_name, 'r') as file:
        """
        char = file.read(1)
        if state == 0:
            if char == 'r':
                state = 1 # estado do return ou id
            elif char == 'i':
                state = 2 # estado do if ou int ou id
            elif char == 'w':
                state = 3 # estado do while ou id
            elif char == 'v':
                state = 4 # estado do void ou id
            elif char == 'e':
                state = 5 # estado do else ou id
            elif char == '+':
                state = 6 # estado do +
            elif char == '-':
                state = 7 # estado do -
            elif char == '*':
                state = 8 # estado do *
            elif char == '/':
                state = 9 # estado do /
            elif char == '=':
                state = 10 # estado do = ou ==
            elif char == '<':
                state = 11 # estado do < ou <=
            elif char == '>':
                state = 12 # estado do > ou >=
            elif char == '!':
                state = 13 # estado do ! ou !=
            elif char == ';':
                state = 14 # estado do ;
            elif char == ',':
                state = 15 # estado do ,
            elif char == '(':
                state = 16 # estado do (
            elif char == ')':
                state = 17 # estado do )
            elif char == "{":
                state = 18 # estado do {
            elif char == "}":
                state = 19 # estado do }
            elif char == " ":
                state = 0
            elif char == "\n":
                state = 0
        elif state == 1:
            if char == 'e':
                state = 20 # estado do return
            else:
                state = 21 # estado do id
        elif state == 2:
            if char == 'f':
                state = 22 # estado do if
            elif char == 'n':
                state = 23 # estado do int
            else:
                state = 21 # estado do id
        elif state == 3:
            if char == 'h':
                state = 24 # estado do while
            else:
                state = 21 # estado do id
        elif state == 4:
            if char == 'o':
                state = 25 # estado do void
            else:
                state = 21 # estado do id
        elif state == 5:
            if char == 'l':
                state = 26 # estado do else
            else:
                state = 21
        elif state == 6:
            state = 0 # volta para o estado inicial
"""
        automata = Automata()
        if automata.init_state(file):
            print("Aceito")
        else:
            print("Rejeitado")

if __name__ == "__main__":
    main()
