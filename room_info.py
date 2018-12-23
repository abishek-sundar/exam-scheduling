from csv_parser import csv_parser
class room_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self)
        self.classCount = 0
        self.roomDict = dict()
        
    def storeClasses(self):
        roomMatrix = self.readFile("classes.txt")
        for roomArray in roomMatrix:
            room = roomArray[0]
            size = int(roomArray[1])
            self.roomDict[room] = size   
        self.classCount = len(self.roomDict)




