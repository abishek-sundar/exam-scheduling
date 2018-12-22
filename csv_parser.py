from csv import reader
class csv_parser:
    def __init__(self,_input):
        self.__input = _input
        self.__output = []

    def readFile(self):
        with open(self.__input) as parseCsv:
            text = reader(parseCsv, delimiter = ',')
            title = True
            for row in text:
                if title:
                    title = False
                else:
                    self.__output.append(row)
        return self.__output