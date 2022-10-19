from student import Students
class Addresses(Students):
    
    def setStudentID(self, StudentID):
        self.__studentID = StudentID
    def getStudentID(self): 
        return self.__studentID
#stdFirstName
    def setStdFirstName(self, StdFirstName):
        self.__stdFirstName = StdFirstName
    def getStdFirstName(self): 
        return self.__stdFirstName 
# -	stdLastName
    def setStdLastName(self, StdLastName):
        self.__stdLastName = StdLastName
    def getStdLastName(self): 
        return self.__stdLastName
# 	stdMarks
    def setStdMarks(self, StdMarks):
        self.__stdMarks = StdMarks
    def getStdMarks(self): 
        return self.__stdMarks 
#   stdAddress
    def setStdAddress(self, StdAddress):
        self.__stdAddress = StdAddress
    def getStdAddress(self): 
        return self.__stdAddress        