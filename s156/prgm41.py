import csv
with open("csv3.csv",newline="")as csvfile:
    d=csv.DictReader(csvfile)
    print("ROLL NO STUDENT NAME")
    print("___________________")
    for i in d:
        print(i['ROLLNO'],i['STUDENTNAME'])