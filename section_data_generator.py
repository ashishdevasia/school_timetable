output_list = []

while True:
    class_names = input("Enter Class Names (comma separated): ")
    if not class_names:
        break
    class_names_list = [x.strip() for x in class_names.split(",")]
    subjects = ",".join([x.strip() for x in input("Enter Subjects (comma separated): ").split(",")])
    for class_name in class_names_list:
        output_list.append(f"{class_name},{subjects}")

with open("section_data.txt", "w") as file:
    file.write("\n".join(output_list))
