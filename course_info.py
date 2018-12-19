from csv_parser import csv_parser
class course_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self,"course.txt")
        self.courseCount = 0
        self.courses = dict()

    def populateCourses(self):
        matrixCourses = self.readFile()
        self.courseCount = len(matrixCourses)
        for row in matrixCourses:
            self.courses[row[0]] = (row[1], row[2])


