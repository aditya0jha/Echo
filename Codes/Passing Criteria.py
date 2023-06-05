total_marks = int(input("Enter your total marks:"))
percentage = total_marks/600*100
if total_marks>600:
    print("Invalid Entry")
else:
    print('Percentage:',percentage)
if percentage>=0 and percentage<35:
    print("FAIL")
if percentage>=35 and percentage<50:
    print("Passed in Third Class")
if percentage>=50 and percentage<60:
    print("Passed in Second Class")
if percentage>=60 and percentage<85:
    print("Passed in First Class")
if percentage>=85 and percentage<=100:
    print("Distinction")