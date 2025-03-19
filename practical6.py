class RecursiveDescentParser:
    def __init__(self, grammar, start_symbol, input_string):
        self.grammar = grammar
        self.start_symbol = start_symbol
        self.input = input_string
        self.position = 0

    def parse(self):
        if self._parse_symbol(self.start_symbol) and self.position == len(self.input):
            return True
        else:
            return False

    def _parse_symbol(self, symbol):
        if symbol in self.grammar:
            for production in self.grammar[symbol]:
                saved_position = self.position  
                if self._parse_production(production):
                    return True
                self.position = saved_position
            return False
        else:
            if self.position < len(self.input) and self.input[self.position] == symbol:
                self.position += 1
                return True
            return False

    def _parse_production(self, production):
        if production == ['']:
            return True
        for symbol in production:
            if not self._parse_symbol(symbol):
                return False
        return True


grammar = {
    'S': [['(', 'L', ')'], ['a']],
    'L': [['S', 'L\'']],
    'L\'': [[',', 'S', 'L\''], ['']]
}

parser = RecursiveDescentParser(grammar, 'S', "(a)")
print(parser.parse())

parser = RecursiveDescentParser(grammar, 'S', "(a,(a,a))")
print(parser.parse())

parser = RecursiveDescentParser(grammar, 'S', "(a,a)")
print(parser.parse())