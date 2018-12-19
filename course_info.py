from csv_parser import csv_parser
class course_info(csv_parser):
    def __init__(self):
        csv_parser.__init__(self,"course.txt")
        courseCount = 0
        courses = dict()

    def populateCourses(self):
        matrixCourses = self.readFile()
        self.courseCount = matrixCourses.size
        for row in matrixCourses:
            self.courses[row[0]] = (row[1], row[2])


