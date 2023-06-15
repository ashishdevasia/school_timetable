teacher_subject_class = {}

while True:
    teacher_name = input("Enter Teacher's Name: ")
    if not teacher_name:
        break
    teacher_subject_class[teacher_name] = {}
    while True:
        subject = input("Enter Subject's Name: ")
        if not subject:
            break
        classes_str = input("Enter Classes (comma separated): ")
        classes = [x.strip() for x in classes_str.split(",")]
        teacher_subject_class[teacher_name][subject] = classes

output_list = []
for teacher_name, subject_class_dict in teacher_subject_class.items():
    output_list.append([teacher_name])
    for subject, classes_list in subject_class_dict.items():
        for cls in classes_list:
            output_list[-1] += [subject, cls]

with open("teacher_data.txt", "w") as file:
    file.write("\n".join([",".join(line) for line in output_list]))
