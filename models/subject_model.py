class SubjectModel:
    """
    {
          "id": "COMP101",
          "name": "Computer",
          "lecture": 4,
          "lab": true,
          "practical": [2, 2]
        }
    """
    def __init__(self,json:dict,**kwargs) -> None:
        if json is not None:
            self.id=json.get("id")
            self.name=json.get("name")
            self.lecture:int=int(str(json.get("lecture")))
            self.lab=json.get("lab")
            self.practical=json.get("practical")
        else:
            self.id=kwargs.get("id")
            self.name=kwargs.get("name")
            self.lecture:int=int(str(kwargs.get("lecture")))
            self.lab=kwargs.get("lab")
            self.practical=kwargs.get("practical")
    def __repr__(self) -> str:
        return f"{self.id} {self.name}\r\n"
