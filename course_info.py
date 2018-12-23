from csv_parser import csv_parser
class course_info(csv_parser):
    
    def __init__(self):
        csv_parser.__init__(self) 
        self.courseCount = 0 #holds number of courses in total
        self.courseEnrollmentNum = dict() #holds number of people taking a course
        self.studentsTook = dict() #holds all the courses taken by a student
        self.courseMatrix = dict() #holds a course x course matrix that holds the number of students taking both courses
        self.cNameToId = dict() #mapping of course name to ID
        self.cIdToName = [] #mapping of course ID to name
        self.disjointCourses = [] 
        #array of tuples holding courses that can be scheduled at the same time

    # @brief: populates courses dict, cNameToId, cIdToName, and courseMatrix.
    def parseCourses(self):
        coursesFile = self.readFile("course.txt")
        self.courseCount = len(coursesFile)
        count = 0
        for row in coursesFile:
            student = row[1].strip()
            course = row[0].strip()
            if course in self.courseEnrollmentNum.keys():
                self.courseEnrollmentNum[course] = self.courseEnrollmentNum[course] + 1
            else:
                self.courseEnrollmentNum[course] = 1
                self.cNameToId[course] = count
                self.cIdToName.append(course)
                count = count + 1
            if student in self.studentsTook.keys():
                self.studentsTook[student].append(self.cNameToId[course])
                self.__populateCourseMatrix(self.cNameToId[course],student)
            else:
                self.studentsTook[student] = [self.cNameToId[course]]
        self.__setDisjoint()

    def __populateCourseMatrix(self,newCourse,student):
        for oldCourse in self.studentsTook[student]:
            key, diff = self.__courseCompare(oldCourse,newCourse)
            if not diff:
                continue
            if key in self.courseMatrix.keys():
                self.courseMatrix[key] = self.courseMatrix[key] + 1
            else:
                self.courseMatrix[key] = 1

    def __setDisjoint(self):
        ids = self.cNameToId.values()
        mutuallyExclusive = []
        for course1 in ids:
            for course2 in ids:
                newKey, diff = self.__courseCompare(course1,course2)
                if not diff:
                    continue
                if newKey not in self.courseMatrix.keys():
                    self.courseMatrix[newKey] = 0
                    mutuallyExclusive.append(newKey)
        self.__disjointClosure(mutuallyExclusive)
    
    def __disjointClosure(self, disjointSet):
        for courses in disjointSet:
            inserted = False
            for disjointArray in self.disjointCourses:
                if courses[0] in disjointArray and courses[1] in disjointArray:
                    inserted = True
                    break
                if courses[1] in disjointArray:
                    self.__checkOtherCourses(disjointArray,courses[0],disjointSet) 
                if courses[0] in disjointArray:
                    self.__checkOtherCourses(disjointArray,courses[1],disjointSet)
                if courses[0] in disjointArray and courses[1] in disjointArray:
                    inserted = True
            if not inserted:
                self.disjointCourses.append([courses[0],courses[1]])             
                    
    def __checkOtherCourses(self, courseArray, checkCourse, mutuallyExclusive):
        for course in courseArray:
            key, diff = self.__courseCompare(course,checkCourse)
            if not diff:
                return True
            if key not in mutuallyExclusive:
                return False
        courseArray.append(checkCourse)
        return True

    def __courseCompare(self, course1, course2):
        if course1<course2:
            return (course1,course2), True
        elif course2<course1:
            return (course2,course1), True
        else:
            return (0,0), False

