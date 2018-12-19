from csv import reader
import numpy as np
class csv_parser:
    def __init__(self,input):
        self.input = input
        self.output = np.array([])

    def readFile(self):
        with open(input) as parseCsv:
            text = reader(parseCsv, delimeter = ',')
            bool title = True
            for row in text:
                if title:
                    title = False
                else:
                    self.output.append(row)
        return self.output