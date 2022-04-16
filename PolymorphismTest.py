from tkinter import *
root = Tk()
root.title("Polymorphism Test")
root.geometry("600x500")

percentage_grade_3_label = Label()

percentage_grade_5_label = Label()

percentage_grade_10_label = Label()

class grade3():
    def __init__(self, language_arts,mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        percentage_grade_3_label["text"] = total_marks / 200
        
class grade5():
    def __init__(self, language_arts,mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        percentage_grade_5_label["text"] = total_marks / 300
        
class grade10():
    def __init__(self, language_arts,mathematics,social_studies,science,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.science = science
        self.foreign_language = foreign_language
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.science + self.foreign_language
        total_marks_with_100 = total_marks * 100
        percentage_grade_10_label["text"] = total_marks / 500
        
        
        
        
        
object_grade_3 = grade3(40,50)
button_g3 = Button(root,text="Tap here For Grade 3", command = object_grade_3.percentage())
        
object_grade_5 = grade5(40,50,80)
button_g5 = Button(root,text="Tap here For Grade 5", command = object_grade_5.percentage())
        
object_grade_10 = grade10(47,51,74,25,89)
button_g10 = Button(root,text="Tap here For Grade 10", command = object_grade_10.percentage())


button_g3.pack(padx=5,pady=5)
percentage_grade_3_label.pack()

button_g5.pack(padx=5,pady=5)
percentage_grade_5_label.pack()

button_g10.pack(padx=5,pady=5)
percentage_grade_10_label.pack()






root.mainloop()
