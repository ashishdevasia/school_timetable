import tkinter as tk
import tkinter.messagebox as tkmb
import csv

section_data_empty = True


def ADD_Section_btn_click(dict_subs,sec_name):
    s = "Section " + str(sec_name) + " successfully created with subjects "
    write_str = str(sec_name)
    checkComma = False      #Also checks if there is atleast one subject
    for key in dict_subs:
        if dict_subs[key].get()==1:
            write_str = write_str + "," + key
            if not checkComma:
                s = s + key
                checkComma = True
            else:
                s = s + ", " + key
    if not checkComma:
        tkmb.showinfo("Error","No subjects selected!")
        window2.destroy()
        return
    with open('section_data.txt','a') as file:
        if not section_data_empty:
            file.write("\n" + write_str)
        else:
            file.write(write_str)
    tkmb.showinfo("Success",s)
    window2.destroy()
    window.destroy()
    main()


def ADD_btn_click():
    INPUT = l_sectionname_input.get("1.0", "end-1c")

    if INPUT == "":
        tkmb.showinfo("Error","Please enter a valid section name")
        return

    with open("section_data.txt",'r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        section_list = []
        for row in reader:
            section_list.append(row[0])
        if INPUT in section_list:
            tkmb.showinfo("Error","Section Already Exists! Please try again.")
            return
    
    global window2
    window2 = tk.Tk()
    window2.title("Details of Section " + str(INPUT))

    l_select_subjects = tk.Label(window2, text = "Select subjects for section " + str(INPUT))

    with open("subjects_list.txt", 'r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        sub_list = reader[0]

    list_check_btns = []
    dict_subs = {}
    for sub in sub_list:
        dict_subs[sub] = tk.IntVar(master=window2)

    for subject in sub_list:
        list_check_btns.append(tk.Checkbutton(window2, text = subject,
                                              variable = dict_subs[subject]))


    ADD_Section_btn = tk.Button(window2, height = 2,
                                width = 20,
                                text = "Confirm Subjects",
                                command = lambda: ADD_Section_btn_click(dict_subs,INPUT))

    l_select_subjects.pack()
    for btn in list_check_btns:
        btn.pack(anchor = 'w')
    ADD_Section_btn.pack()

    window2.mainloop()
    

#########################################################################

def main():
    global window
    window = tk.Tk()
    window.title("Add a Section")

    frame = tk.Frame(window)

    l_sectionname_prompt = tk.Label(text = "Enter the name of the section")
    global l_sectionname_input
    l_sectionname_input = tk.Text(window,height = 1,
                                  width = 25,
                                  bg = "light yellow")
    ADD_btn = tk.Button(window, height = 2,
                        width = 5,
                        text = "Add",
                        command = lambda:ADD_btn_click())

    l_existing_sections_title = tk.Label(window, text = "List of Sections Present:",
                                         font = ('Helvetica', 12, 'bold'))

    l_sections_list = []
    l_section_name_list = []

    try:
        with open('section_data.txt','r') as file:
            reader = csv.reader(file)
            reader = list(reader)
            global section_data_empty
            if len(reader) == 0:
                section_data_empty = True
            else:
                section_data_empty = False
            count = 0
            if len(reader) == 0:
                l_section_name_list.append(tk.Label(frame, text = "No sections exist yet!").grid(row=0,column=0,sticky='W'))
            for row in reader:
                count += 1
                sr_sec_name = row[0] + ": "
                sr = row[1]
                if len(row)>1:
                    for i in range(2,len(row)):
                        sr = sr + ", " + row[i]
                l_section_name_list.append(tk.Label(frame, text = sr_sec_name).grid(row=count,column=0,sticky='E'))
                l_sections_list.append(tk.Label(frame, text = sr).grid(row=count,column=1,sticky='W'))
    except:
        l_sections_list.append(tk.Label(frame, text = "There is some error (probably)!").grid(row=0,column=0,sticky='W'))


    frame.grid_columnconfigure(0, minsize=0)

    l_sectionname_prompt.pack()
    l_sectionname_input.pack()
    ADD_btn.pack()

    l_existing_sections_title.pack(anchor = 'w')

    frame.pack()

    window.mainloop()



main()
