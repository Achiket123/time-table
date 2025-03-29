from models.class_model import ClassModel


class Schedules:
    def __init__(self,id,teacherID,subjectID,classID,period) -> None:
        self.id=id
        self.teacherID=teacherID
        self.subjectID=subjectID
        self.classID=classID
        self.period=period

class ScheduleModel:
    """
    Schedule Model
    [
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,-1,-1],
    
    ]
    """
    def __init__(self,id,clas:ClassModel,periods:int,schedules) -> None:
        self.id = id;
        self.clas = clas;
        self.periods =periods;
        self.schedule = schedules;