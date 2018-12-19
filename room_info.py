from csv_parser import csv_parser
import numpy as np
class room_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self,"classes.txt")
        classCount = 0
        classArray = np.array([])

    def storeClasses(self):
        self.classArray = self.readFile()
        self.classCount = self.classArray.size




