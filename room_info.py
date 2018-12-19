from csv_parser import csv_parser
class room_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self,"classes.txt")
        self.classCount = 0
        self.classArray = []

    def storeClasses(self):
        roomMatrix = self.readFile()
        for roomArray in roomMatrix:
            for room in roomArray:
                self.classArray.append(room)
        self.classCount = len(self.classArray)




