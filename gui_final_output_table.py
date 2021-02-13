import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk
from tkscrolledframe import ScrolledFrame
import csv
import random
from datetime import datetime

now = datetime.now()
now = now.strftime("%B %d, %Y  %H:%M:%S")

periods = int(input('Please enter the number of periods: '))
free_periods = 1                            #Makes sure a teacher gets atleast a free period if 1.
max_periods_teacher = periods - free_periods


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

def output_gui(section_no, teacher_no, section_teacher_object):
    root = tk.Tk()
    #root.attributes('-fullscreen', True)
    root.state('zoomed')
    root.title("Final time-table")

    #Section Timetable
    window = tk.Frame(root)
    l_section_title = tk.Label(window, text = "Section time-table: ",
                               font = ('Helvetica', 11, 'bold'))
    l_section_title.pack(anchor = 'w')

    sf_section = ScrolledFrame(window,width = 790, height = 960)
    sf_section.pack(side="left", expand=1, fill="both")
    sf_section.bind_arrow_keys(window)
    sf_section.bind_scroll_wheel(window)
    
    frame_section = sf_section.display_widget(tk.Frame)

    number_of_rows = section_no + 1
    number_of_columns = periods + 1

    l_section_names = []
    l_periods = []

    for section in section_teacher_object[0]:
        l_section_names.append(section.name)

    for i in range(periods):
        l_periods.append(str(i+1))

    tk.Label(frame_section, text = "Sections",
             font = ('Helvetica', 11, 'bold')).grid(row=0,column=0)

    for i in range(len(l_periods)):
        tk.Label(frame_section, text = l_periods[i],
                 font = ('Helvetica', 10, 'bold')).grid(row=0,column=i+1)

    for i in range(len(l_section_names)):
        tk.Label(frame_section, text = l_section_names[i],
                 font = ('Helvetica', 10, 'bold')).grid(row=i+1,column=0)


    frames_array_sec = []

    for i in range(section_no):
        sec = section_teacher_object[0][i]
        frames_array_sec.append([])
        for j in range(periods):
            frames_array_sec[i].append(tk.Frame(frame_section))
            frames_array_sec[i][j].grid(row=i+1,column=j+1)
            try:
                tk.Label(frames_array_sec[i][j],text = sec.Period[j][1]).grid(row=0,column=0)
                tk.Label(frames_array_sec[i][j],text = sec.Period[j][0]).grid(row=1,column=0)
            except:
                tk.Label(frames_array_sec[i][j],text = "-").grid(row=0,column=0)
            frames_array_sec[i][j].grid_columnconfigure(j, minsize=10)
            

    tkinter.ttk.Separator(frame_section, orient='vertical').grid(column=0, row=0, rowspan=number_of_rows, sticky='nsw')
    for i in range(number_of_columns):
        tkinter.ttk.Separator(frame_section, orient='vertical').grid(column=i, row=0, rowspan=number_of_rows, sticky='nse')

    tkinter.ttk.Separator(frame_section, orient='horizontal').grid(column=0, row=0, columnspan=number_of_columns, sticky='wen')
    for i in range(number_of_rows):
        tkinter.ttk.Separator(frame_section, orient='horizontal').grid(column=0, row=i, columnspan=number_of_columns, sticky='wes')

    window.pack(side = 'left')

    #Teacher-timetable

    window2 = tk.Frame(root)

    l_teacher_title = tk.Label(window2, text = "Teacher's time-table: ",
                               font = ('Helvetica', 11, 'bold'))
    l_teacher_title.pack(anchor = 'w')

    sf_teacher = ScrolledFrame(window2,width = 700, height = 960)
    sf_teacher.pack(side="left", expand=1, fill="both")
    sf_teacher.bind_arrow_keys(window)
    sf_teacher.bind_scroll_wheel(window)
    
    frame_teacher = sf_teacher.display_widget(tk.Frame)

    number_of_rows_t = teacher_no + 1
    number_of_columns = periods + 1

    l_teacher_names = []
    l_periods = []

    for teacher in section_teacher_object[1]:
        l_teacher_names.append(teacher.name)

    for i in range(periods):
        l_periods.append(str(i+1))

    tk.Label(frame_teacher, text = "Teachers",
             font = ('Helvetica', 11, 'bold')).grid(row=0,column=0)

    for i in range(len(l_periods)):
        tk.Label(frame_teacher, text = l_periods[i],
                 font = ('Helvetica', 10, 'bold')).grid(row=0,column=i+1)

    for i in range(len(l_teacher_names)):
        tk.Label(frame_teacher, text = l_teacher_names[i],
                 font = ('Helvetica', 10, 'bold')).grid(row=i+1,column=0)

    frames_array_teacher = []

    for i in range(teacher_no):
        tea = section_teacher_object[1][i]
        frames_array_teacher.append([])
        for j in range(periods):
            frames_array_teacher[i].append(tk.Frame(frame_teacher))
            frames_array_teacher[i][j].grid(row=i+1,column=j+1)
            try:
                tk.Label(frames_array_teacher[i][j],text = tea.Period[j][0]).grid(row=0,column=0)
                tk.Label(frames_array_teacher[i][j],text = tea.Period[j][1]).grid(row=1,column=0)
            except:
                tk.Label(frames_array_teacher[i][j],text = "-").grid(row=0,column=0)
            frames_array_teacher[i][j].grid_columnconfigure(j, minsize=10)

    tkinter.ttk.Separator(frame_teacher, orient='vertical').grid(column=0, row=0, rowspan=number_of_rows_t, sticky='nsw')
    for i in range(number_of_columns):
        tkinter.ttk.Separator(frame_teacher, orient='vertical').grid(column=i, row=0, rowspan=number_of_rows_t, sticky='nse')

    tkinter.ttk.Separator(frame_teacher, orient='horizontal').grid(column=0, row=0, columnspan=number_of_columns, sticky='wen')
    for i in range(number_of_rows_t):
        tkinter.ttk.Separator(frame_teacher, orient='horizontal').grid(column=0, row=i, columnspan=number_of_columns, sticky='wes')

    window2.pack(side = 'left')

    

    root.mainloop()

    



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
                        if teacher.no_of_classes < max_periods_teacher:
                            teacher.Period[period] = [section.name, subject]
                            section.Period[period] = [teacher.name, subject]
                            section.Subjects.remove(subject)
                            teacher.no_of_classes += 1
                            #print(f'Period: {period+1}, Section: {section.name}')
                            return True

def create_temp_files():
    with open("teacher_data.txt",'r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        with open("teacher_data_temp.txt",'w') as file2:
            file2.write(reader[0][0])
            for k in range(1,len(reader[0])):
                file2.write("," + reader[0][k])
            for i in range(1,len(reader)):
                file2.write("\n"+reader[i][0])
                for j in range(1,len(reader[i])):
                    file2.write("," + reader[i][j])
            

def rearrange_teachers(teachers_list):
    for i in range(0,len(teachers_list)-1):
        for j in range(i+1,len(teachers_list)):
            if teachers_list[i].no_of_classes > teachers_list[j].no_of_classes:
                teachers_list[i],teachers_list[j] = teachers_list[j],teachers_list[i]

    with open("teacher_data_temp.txt",'w') as file:
        file.write(teachers_list[0].name)
        for v_sc in teachers_list[0].SC:
            file.write("," + v_sc[0] + "," + v_sc[1])
        for i in range(1,len(teachers_list)):
            file.write("\n" + teachers_list[i].name)
            for v_sc in teachers_list[i].SC:
                file.write("," + v_sc[0] + "," + v_sc[1])
                
        

def main(count, oldncc, actual_counter):
    section_no, section_list, teacher_no, teachers_list = read_file('teacher_data_temp.txt','section_data.txt')

    

    for section in section_list:
        random.shuffle(section.Subjects)
    for teacher in teachers_list:
        random.shuffle(teacher.SC)

    list_random_pick = []               #To pick a period
    for i in range(periods):
        list_random_pick.append(i)
    #random.shuffle(list_random_pick)
    for section in section_list:
        random.shuffle(list_random_pick)
        for i in list_random_pick:
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
        rearrange_teachers(teachers_list)
    elif(no_class_counter < oldncc):
        section_teacher_object[0] = section_list
        section_teacher_object[1] = teachers_list
        same_ac = 0
        rearrange_teachers(teachers_list)
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
        output_gui(section_no, teacher_no, section_teacher_object)
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
    



def running_main(ec):
    if ec <= 5:
        try:
            main(0,99756,0)
        except:
            running_main(ec+1)
    else:
        print("Error!")


create_temp_files()
#main(0,99756,0)
running_main(0)


        






