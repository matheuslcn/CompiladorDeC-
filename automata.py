class Automata:
    def __init__(self, alphabet, initial_state, final_states):
        self.initial_state = initial_state
        self.final_states = final_states
        self.alphabet = alphabet

    # Verificar se o automato aceita o arquivo
    def accepts(self, file):
        current_state = self.initial_state
        while True:
            symbol = file.read(1)
            if not symbol:
                break
            if symbol not in self.alphabet:
                return False
            current_state = current_state.next_state(symbol)
            if current_state is None:
                current_state = self.initial_state
        return current_state in self.final_states