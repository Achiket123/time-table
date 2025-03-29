class ClassModel:
    """
    {
      "class": "1",
      "subjects": ["COMP101", "CHEM101", "SSE101", "DT101", "CSS101", "MATH101"]
    }
    also needs to have a default matrix
    """
    def __init__(self,json:dict,**kwargs) -> None:
        self.class_matrix = class_maatrix = [
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,-1,-1]
        ];
        if(json is not None):
            self.id = json.get("id")
            subjects = json.get("subjects")
            if subjects is not None:
                self.subjects = [[x,0] for x in subjects]
            else:
                self.subjects = []

        else:
            self.id = kwargs.get("id")
            self.subjects = [ [x,0] for x in kwargs.get("subjects")]
        self.scheduleModel = None;

    def __repr__(self) -> str:
        return str(self.class_matrix)
