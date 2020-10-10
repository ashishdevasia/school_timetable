import csv
import random
from datetime import datetime

now = datetime.now()
now = now.strftime("%B %d, %Y  %H:%M:%S")

periods = int(input('Please enter the number of periods: '))

section_teacher_object = [[],[]]

class Teacher:
    def __init__(self, name):
        self.name = name
        self.SC = []
        self.no_of_classes = 0
        self.Period = []
        for i in range(periods):
            self.Period.append([])

class Section:
    def __init__(self, name):
        self.name = name
        self.Subjects = []
        self.Period = []
        for i in range(periods):
            self.Period.append([])



def read_file(teacher_file,section_file):
    section_no = 0
    section_list = []
    teacher_no = 0
    teachers_list = []
    with open(section_file, 'r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        section_no = len(reader)
        for row in reader:
            section_name = row[0]
            subjects_list = row[1:]
            new_section = Section(section_name)
            new_section.Subjects = subjects_list
            section_list.append(new_section)
    with open(teacher_file, 'r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        teacher_no = len(reader)
        for row in reader:
            teacher_name = row[0]
            SC_list = []
            for i in range(1,(len(row)//2)+1):
                SC_list.append([row[(2*i)-1],row[2*i]])
            new_teacher = Teacher(teacher_name)
            new_teacher.SC = SC_list
            teachers_list.append(new_teacher)
    return section_no, section_list, teacher_no, teachers_list
            
def find_a_teacher(period, section, teachers_list):
    for subject in section.Subjects:
        for teacher in teachers_list:
            if not teacher.Period[period]:
                for SC in teacher.SC:
                    if (SC[0] == subject) and (SC[1] == section.name):
                        teacher.Period[period] = [section.name, subject]
                        section.Period[period] = [teacher.name, subject]
                        section.Subjects.remove(subject)
                        #print(f'Period: {period+1}, Section: {section.name}')
                        return True

def main(count, oldncc, actual_counter):
    section_no, section_list, teacher_no, teachers_list = read_file('teacher_data.txt','section_data.txt')

    for section in section_list:
        random.shuffle(section.Subjects)
    for teacher in teachers_list:
        random.shuffle(teacher.SC)
        
##    print("Sections: ")
##    for section in section_list:
##        print(section.name)
##        print(section.Subjects)
##    print("Teachers: ")
##    for teacher in teachers_list:
##        print(teacher.name)
##        print(teacher.SC)

    for i in range(periods):
        for section in section_list:
            find_a_teacher(i, section, teachers_list)
            
    no_class_counter = 0
    for section in section_list:
        for period in section.Period:
            if not period:
                no_class_counter += 1
    print(f'NCC: {no_class_counter}, AC: {actual_counter}')

    if(oldncc == 99756):
        section_teacher_object[0] = section_list
        section_teacher_object[1] = teachers_list
        same_ac = 0
    elif(no_class_counter < oldncc):
        section_teacher_object[0] = section_list
        section_teacher_object[1] = teachers_list
        same_ac = 0
    else:
        same_ac = actual_counter + 1
        

    if(no_class_counter == 0 or actual_counter > 512):
        with open('final_out.txt', 'w') as file:
            file.write("Date and Time: " + str(now) + "\n")
            line1 = "Timetable successfully generated!\nIterations: " + str(count+1) + "\n\nSection Timetable: "
            file.write(line1)
            for section in section_teacher_object[0]:
                file.write("\n\nClass: ")
                file.write(section.name)
                file.write("\n")
                for i in range(periods):
                    try:
                        l = "Period " + str(i+1) + ": " + str(section.Period[i][1]) + " by " + str(section.Period[i][0]) + "\n"
                        file.write(l)
                    except:
                        l = "Period " + str(i+1) + ": No class found!" + "\n"
                        file.write(l)
            file.write("\n\nTeachers timetable:\n")
            for teacher in section_teacher_object[1]:
                file.write("\n\nTeacher: ")
                file.write(teacher.name)
                file.write("\n")
                for i in range(periods):
                    try:
                        l = "Period " + str(i+1) + ": " + str(teacher.Period[i][1]) + " at section " + str(teacher.Period[i][0]) + "\n"
                        file.write(l)
                    except:
                        l = "Period " + str(i+1) + ": Free" + "\n"
                        file.write(l)

            
        for section in section_teacher_object[0]:
            print(section.name)
            for i in range(periods):
                try:
                    print(f'Period {i+1}: {section.Period[i][1]} by {section.Period[i][0]}')
                except:
                    print(f'Period {i+1}: No class found!')
        print('\n')
        for teacher in section_teacher_object[1]:
            print(teacher.name)
            for i in range(periods):
                try:
                    print(f'Period {i+1}: {teacher.Period[i][1]} at section {teacher.Period[i][0]}')
                except:
                    print(f'Period {i+1}: Free')
        print(f'\n\nSuccessfully completed in {count+1} iteration(s).\nActual Counter: {actual_counter}.')
        return

    if(no_class_counter != 0):
        section_no = 0
        section_list = []
        teacher_no = 0
        teachers_list = []
        count += 1
        main(count, min(no_class_counter, oldncc), same_ac)
        

    


    



##    #Period 1
##    #Section 1
##    job = find_a_teacher(0, section_list[0])
##    print(section_list[0].Period)
##    #Section 2
##    #find_a_teacher(0, section_list[1])
##    print(section_list[1].Period)
    









        





main(0,99756,0)
