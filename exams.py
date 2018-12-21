from course_info import course_info
from room_info import room_info

courseInfo = course_info()
roomInfo = room_info()

courseInfo.parseCourses()
roomInfo.storeClasses()