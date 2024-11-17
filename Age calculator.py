import datetime
from tkinter import *
from PIL import Image, ImageTk

# Initialize Tkinter root
root = Tk()
root.geometry("800x600")
root.title("Age Calculator")

# Load and display image
image1 = Image.open("D:/Semester 2/python 2 preethi madam/s.png")  # Ensure this path is valid
test = ImageTk.PhotoImage(image1)
label1 = Label(root, image=test)
label1.image = test
label1.place(x=100, y=100)

# Function to calculate age
def calculateAge():
    name = nameEntry.get()
    birthdate = datetime.date(
        int(YearEntry.get()), int(MonthEntry.get()), int(dateEntry.get())
    )
    person = Person(name, birthdate)
    age = person.age()

    # Display the result
    textArea = Text(master=root, height=2, width=50)
    textArea.place(x=100, y=500)
    answer = f"Hey {name}, you are {age} years old!"
    textArea.insert(END, answer)

# Person class for age calculation
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )
        return age

# UI Elements
Label(root, text="Name", font=23).place(x=200, y=250)
Label(root, text="Year", font=23).place(x=200, y=300)
Label(root, text="Month", font=23).place(x=200, y=350)
Label(root, text="Day", font=23).place(x=200, y=400)

nameEntry = Entry(root, width=30, bd=3)
nameEntry.place(x=300, y=250)
YearEntry = Entry(root, width=30, bd=3)
YearEntry.place(x=300, y=300)
MonthEntry = Entry(root, width=30, bd=3)
MonthEntry.place(x=300, y=350)
dateEntry = Entry(root, width=30, bd=3)
dateEntry.place(x=300, y=400)

Button(
    root, text="Calculate Age", font=20, bg="Grey", width=11, height=2, command=calculateAge
).place(x=300, y=450)

# Run the application
root.mainloop()
