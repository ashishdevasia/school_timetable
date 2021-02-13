import csv

with open("teacher_data.txt",'r') as file:
    reader = csv.reader(file)
    reader = list(reader)
    for i in range(0,len(reader)-1):
        for j in range(i+1,len(reader)):
            if len(reader[i])>len(reader[j]):
                reader[i],reader[j] = reader[j],reader[i]

    with open("teachers_rearranged.txt",'w') as file2:
        file2.write(reader[0][0])
        for k in range(1,len(reader[0])):
            file2.write("," + reader[0][k])
        for i in range(1,len(reader)):
            file2.write("\n"+reader[i][0])
            for j in range(1,len(reader[i])):
                file2.write("," + reader[i][j])
                
    

