class PredictiveParser:
    def __init__(self):
        self.parse_table = {
            'A': {'b': 'B', 'f': 'B', 'c': 'C', 'e': 'C'},
            'B': {'b': 'bB', 'f': 'f'},
            'C': {'c': 'cC', 'e': 'e'}
        }
        self.stack = []
        self.input = ""
    
    def parse(self, input_str):
        self.input = input_str + '$'
        self.stack = ['$', 'A']
        
        index = 0
        while len(self.stack) > 0:
            top = self.stack[-1]
            current_input = self.input[index]
            
            if top == current_input:
                self.stack.pop()
                index += 1
            elif top in self.parse_table and current_input in self.parse_table[top]:
                self.stack.pop()
                production = self.parse_table[top][current_input]
                for symbol in reversed(production):
                    if symbol != 'ε':
                        self.stack.append(symbol)
            else:
                return False
        
        return index == len(self.input)

parser = PredictiveParser()
input_str = input("Enter a string to parse: ")
if parser.parse(input_str):
    print(f"The string '{input_str}' is accepted by the grammar.")
else:
    print(f"The string '{input_str}' is not accepted by the grammar.")
