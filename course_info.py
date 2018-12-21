from csv_parser import csv_parser
class course_info(csv_parser):
    
    def __init__(self):
        csv_parser.__init__(self,"course.txt") 
        self.courseCount = 0 #holds number of courses in total
        self.courses = dict() #holds number of people taking a course
        self.students = dict() #holds all the courses taken by a student
        self.courseMatrix = dict() #holds a course x course matrix that holds the number of students taking both courses
        self.cNameToId = dict() #mapping of course name to ID
        self.cIdToName = [] #mapping of course ID to name
        self.disjointCourses = [] 
        #array of tuples holding courses that can be scheduled at the same time

    # @brief: populates courses dict, cNameToId, cIdToName, and courseMatrix.
    def parseCourses(self):
        coursesFile = self.readFile()
        self.courseCount = len(coursesFile)
        count = 0
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
        self.setDisjoint()

    def populateCourseMatrix(self,newCourse,student):
        for oldCourse in self.students[student]:
            key, diff = self.courseCompare(oldCourse,newCourse)
            if diff == False:
                continue
            if key in self.courseMatrix.keys():
                self.courseMatrix[key] = self.courseMatrix[key] + 1
            else:
                self.courseMatrix[key] = 1

    def setDisjoint(self):
        ids = self.cNameToId.values()
        mutuallyExclusive = []
        for course1 in ids:
            for course2 in ids:
                newKey, diff = self.courseCompare(course1,course2)
                if diff == False:
                    continue
                if newKey not in self.courseMatrix.keys():
                    self.courseMatrix[newKey] = 0
                    mutuallyExclusive.append(newKey)
        self.disjointClosure(mutuallyExclusive)
    
    def disjointClosure(self, disjointSet):
        for courses in disjointSet:
            inserted = False
            for disjointArray in self.disjointCourses:
                if courses[0] in disjointArray and courses[1] in disjointArray:
                    inserted = True
                    break
                if courses[1] in disjointArray:
                    self.checkOtherCourses(disjointArray,courses[0],disjointSet) 
                if courses[0] in disjointArray:
                    self.checkOtherCourses(disjointArray,courses[1],disjointSet)
                if (courses[0] in disjointArray and courses[1] in disjointArray):
                    inserted = True
            if not inserted:
                self.disjointCourses.append([courses[0],courses[1]])             
                    
    def checkOtherCourses(self, courseArray, checkCourse, mutuallyExclusive):
        for course in courseArray:
            key, diff = self.courseCompare(course,checkCourse)
            if diff == False:
                return True
            if key not in mutuallyExclusive:
                return False
        courseArray.append(checkCourse)
        return True

    def courseCompare(self, course1, course2):
        if course1<course2:
            return (course1,course2), True
        elif course2<course1:
            return (course2,course1), True
        else:
            return (0,0), False

