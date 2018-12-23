from room_info import room_info
from course_info import course_info
import sys
class allocRoom(course_info, room_info):
    def __init__(self):
        room_info.__init__(self)
        course_info.__init__(self)
        self.parseCourses()
        self.storeClasses()
        self.numberOfDays = 14
        self.roomTimeSlot = dict()
        self.populateRoomTime()

    def populateRoomTime(self):
        for room in self.roomDict.keys():
            self.roomTimeSlot[room] = []
            for i in range (0,self.numberOfDays):
                self.roomTimeSlot[room].append([sys.maxsize,sys.maxsize,sys.maxsize])
        
        
    
    