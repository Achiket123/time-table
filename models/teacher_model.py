class TeacherModel:
    """
    {
    "id": "T4",
    "name": "Sunil Sharma Sir",
    "subject": "Chemistry",
    "subjectID": "CHEM101"
    },
    """
    def __init__(self, json_data:dict, **kwargs) -> None:
        if json_data is not None:
            self.name = json_data.get("name")
            self.id = json_data.get("id")
            self.subject = json_data.get("subject")
            self.subjectID = json_data.get("subjectID")
        else:
            self.name = kwargs.get("name")
            self.id = kwargs.get("id")
            self.subject = kwargs.get("subject")
            self.subjectID = kwargs.get("subjectID")
        self.numberOfLectures = 0
    def __repr__(self) -> str:
        return f"{self.id} {self.name}\r\n"
