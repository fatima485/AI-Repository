import csv
with open("Student.csv","w",newline="")as f:
    data_handler = csv.writer(f,delimiter = ",")
    data_handler.writerow(["Name","Age","RollNo"])
    data_handler.writerow(["Fatima","20","cs-009"])
    data_handler.writerow(["Wajeeha","20","cs-017"])
    data_handler.writerow(["maheen","20","cs-016"])
    data_handler.writerow(["Name","Age","RollNo"])
    data_handler.writerow(["Name","Age","RollNo"])
#Delimeter: when we are storing then delimeter shows identification that says that change the cell means jahan comma nazar aye cell change kardo
#newline: jab data end hoga tou new line per shift karjaye ga

#now I want to manipulate data : read, writing , matching ,equating

with open("Student.csv","r") as f :
    data_handler = csv.reader(f)
    for data in data_handler:
        #print(data)
        if data[0]=="Fatima":
            print("Yes the person is in the list")
        else:
            print("The person is not")
