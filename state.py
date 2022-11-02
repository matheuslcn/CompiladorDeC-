class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, destination):
        self.transitions[symbol] = destination

    def next_state(self, symbol):
        return self.transitions.get(symbol, None)
