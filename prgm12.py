class Box:
    def __init__(self, currName, currRollNum, currDBMSmarks, currOSmarks):
        self.name = currName
        self.rollnumber = currRollNum
        self.DBMSmarks = currDBMSmarks
        self.OSmarks = currOSmarks
student1 = Box("shiv", 34, 89, 76)
print(student1.name)
print(student1.rollnumber)
print(student1.DBMSmarks)
print(student1.OSmarks)
