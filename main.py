import csv

total_data = 0
total_clean_data = 0
class_0 = 0
clean_class_0 = 0
class_1 = 0
clean_class_1 = 0
clean_data = []
with open('diabetest.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Pregnancies':
            continue

        total_data = total_data + 1         # hitung jumlah data
        if row[8] == '1' :
            class_1 = class_1 + 1           # hitung jumlah data class 1
        else :
            class_0 = class_0 + 1           # hitung jumlah data class 0

        if row[1] != '0' and row[2] != '0' and row[3] != '0' and row[4] != '0' and row[5] != '0' and row[6] != '0' and row[7] != '0':       # cek data clean
            clean_data.append(row)
            total_clean_data = total_clean_data + 1
            if row[8] == '1' :
                clean_class_1 = clean_class_1 + 1           
            else :
                clean_class_0 = clean_class_0 + 1


    print("total data = ", total_data)
    print("total class 1 = ", class_1)
    print("total class 0 = ", class_0)
    print("===========================")
    print("total clean data = ", total_clean_data)
    print("total clean class 1 = ", clean_class_1)
    print("total clean class 0 = ", clean_class_0)
    
    for x in clean_data :
        print(x)

