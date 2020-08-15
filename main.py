periods = int(input('Please enter the number of periods: '))

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

section_no = 0
section_list = []
teacher_no = 0
teachers_list = []

def find_a_teacher(period, section):
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

def main():
    section_no = int(input(f'Please enter the number of sections: '))
    for i in range(section_no):
        print(f'Enter the name of section {i+1} and press ENTER.')
        section_name = input()
        subjects_list = []
        print(f'Enter the name of each subject and press ENTER. Simply press ENTER if there is nothing left.')
        while(True):
            sub = input()
            if sub:
                subjects_list.append(sub)
            else:
                new_section = Section(section_name)
                new_section.Subjects = subjects_list
                section_list.append(new_section)
                break
    teacher_no = int(input(f'Please enter the number of teachers: '))
    for i in range(teacher_no):
        print(f'Enter the name of teacher {i+1} and press ENTER.')
        teacher_name = input()
        SC_list = []
        while(True):
            print(f'Enter a subject {teacher_name} would be teaching and press ENTER. Simply press ENTER if there is nothing left.')
            sub = input()
            if sub:
                print(f'Enter the name of each class {teacher_name} would be teaching {sub} and press ENTER. Simply press ENTER if there is nothing left.')
                while(True):
                    cl = input()
                    if cl:
                        sub_and_class = [sub, cl]
                        SC_list.append(sub_and_class)
                    else:
                        break
            else:
                new_teacher = Teacher(teacher_name)
                new_teacher.SC = SC_list
                teachers_list.append(new_teacher)
                break

##    print("Sections: ")
##    for section in section_list:
##        print(section.name)
##        print(section.Subjects)
##    print("Teachers: ")
##    for teacher in teachers_list:
##        print(teacher.name)
##        print(teacher.SC)
##
    for i in range(periods):
        for section in section_list:
            find_a_teacher(i, section)


    



    for section in section_list:
        print(section.name)
        for i in range(periods):
            try:
                print(f'Period {i+1}: {section.Period[i][1]} by {section.Period[i][0]}')
            except:
                print(f'Period {i+1}: No class found!')

    for teacher in teachers_list:
        print(teacher.name)
        for i in range(periods):
            try:
                print(f'Period {i+1}: {teacher.Period[i][1]} at section {teacher.Period[i][0]}')
            except:
                print(f'Period {i+1}: Free')


##    #Period 1
##    #Section 1
##    job = find_a_teacher(0, section_list[0])
##    print(section_list[0].Period)
##    #Section 2
##    #find_a_teacher(0, section_list[1])
##    print(section_list[1].Period)
    









        





main()
