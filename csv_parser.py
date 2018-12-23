from csv import reader
class csv_parser:
    def __init__(self):
        pass
        
    def readFile(self,input):
        output = []
        with open(input) as parseCsv:
            text = reader(parseCsv, delimiter = ',')
            title = True
            for row in text:
                if title:
                    title = False
                else:
                    output.append(row)
        return output