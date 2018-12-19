from csv_parser import csv_parser
class course_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self,"course.txt")
        self.courseCount = 0
        self.courses = dict()
        self.students = dict()
        self.courseMatrix = dict()
        self.cNameToId = dict()
        self.cIdToName = []
        
    def populateCourses(self):
        coursesFile = self.readFile()
        self.courseCount = len(coursesFile)
        count = 0;
        for row in coursesFile:
            student = row[1].strip()
            course = row[0].strip()
            if course in self.courses:
                self.courses[course] = self.courses[course] + 1
            else:
                self.courses[course] = 1
                self.cNameToId[course] = count
                count = count + 1
                self.cIdToName.append(course)
            if student in self.students:
                self.students[student].append(self.cNameToId[course])
                self.populateCourseMatrix(self.cNameToId[course],student)

            else:
                self.students[student] = [self.cNameToId[course]]
        self.setDisjointToZero()

    def populateCourseMatrix(self,newCourse,student):
        for oldCourse in self.students[student]:
            if (oldCourse < newCourse):
                newKey = (oldCourse, newCourse)
            elif newCourse < oldCourse:
                newKey = (newCourse, oldCourse)
            else:
                continue
            if newKey in self.courseMatrix.keys():
                self.courseMatrix[newKey] = self.courseMatrix[newKey] + 1
            else:
                self.courseMatrix[newKey] = 1

    def setDisjointToZero(self):
        ids = self.cNameToId.values()
        for course1 in ids:
            for course2 in ids:
                if course1 < course2:
                    newKey = (course1,course2)
                elif course2 < course1:
                    newKey = (course2,course1)
                else:
                    continue
                if newKey not in self.courseMatrix.keys():
                    self.courseMatrix[newKey] = 0

