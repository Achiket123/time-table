
import models;
import json;
import random

from models.class_model import ClassModel;

decoder =json.JSONDecoder()
file =open("data/data.json","r")
data = decoder.decode(s=file.read())
file.close()


listofSubjects = [models.subject_model.SubjectModel(x) for x in data["subjects"]];
listofTeachers = [models.teacher_model.TeacherModel(x) for x in data["teachers"]];
listofClasses = [models.class_model.ClassModel(x) for x in data["classes"]];

# Populating Data using random function for first class
# print(listofSubjects)
# print(listofTeachers)
# print(listofClasses)
def populating_with_random_data(class_matrix):
    for dayInt,day in enumerate(class_matrix):
        # gets random subject
        for _classInt,_class in enumerate(day):
            randomNum = random.randint(0,len(listofSubjects)-1);
            subject   = listofSubjects[randomNum]
            if(_class==1):
                class_matrix[dayInt][_classInt]=subject;
                listofSubjects[randomNum].lecture-=1;
    print(class_matrix)
def populating_classes(listofClasses:list[ClassModel]):
    for _classInt,classes in enumerate(listofClasses):
        populating_with_random_data(listofClasses[_classInt].class_matrix)
        print(listofClasses[_classInt].class_matrix)
def main():
    populating_classes(listofClasses)
if __name__ =="__main__":
    main()
