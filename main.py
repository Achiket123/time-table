
import models;
import json;
import random;

decoder =json.JSONDecoder()
file =open("data/data.json","r")
data = decoder.decode(s=file.read())
file.close()
#class Matrix
class_maatrix = [
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,1,1,-1,-1]
];

listofSubjects = [models.subject_model.SubjectModel(x) for x in data["subjects"]];
listofTeachers = [models.teacher_model.TeacherModel(x) for x in data["teachers"]];
listofClasses = [models.class_model.ClassModel(x) for x in data["classes"]];

# Populating Data using random function for first class
def populating_with_random_data(class_matrix):
    for dayInt,day in enumerate(class_matrix):
        # gets random subject
        for _classInt,_class in enumerate(day):
            randomNum = random.randint(0,len(listofSubjects)-1);
            subject   = listofSubjects[randomNum]
            if(_class==1):
                class_matrix[dayInt][_classInt]=subject;
                listofSubjects[randomNum].lecture-=1;
                