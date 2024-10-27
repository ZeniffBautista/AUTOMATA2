class MooreAutomata:
    def __init__(self):
        self.state = 'S0'
    
    def process(self, input_stream):
        output_stream = []
        for symbol in input_stream:
            if self.state == 'S0':
                if symbol == '0':
                    output_stream.append('0')
                else:
                    self.state = 'S1'
                    output_stream.append('1')
            elif self.state == 'S1':
                if symbol == '0':
                    self.state = 'S0'
                    output_stream.append('0')
                else:
                    self.state = 'S2'
                    output_stream.append('0')
            elif self.state == 'S2':
                output_stream.append('0')
                self.state = 'S0'
        return ''.join(output_stream)

automata = MooreAutomata()
input_stream = "110111010111"
output_stream = automata.process(input_stream)
print(f"Input: {input_stream}")
print(f"Output: {output_stream}")
