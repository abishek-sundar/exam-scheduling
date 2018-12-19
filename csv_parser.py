from csv import reader
import numpy as np
class csv_parser:
    def __init__(self,_input):
        self.input = _input
        self.output = []

    def readFile(self):
        with open(self.input) as parseCsv:
            text = reader(parseCsv, delimiter = ',')
            title = True
            for row in text:
                if title:
                    title = False
                else:
                    self.output.append(row)
        return self.output