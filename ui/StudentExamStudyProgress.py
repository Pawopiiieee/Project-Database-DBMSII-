from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial
import ui.StudentExamResult


def student_studyProgress(window, return_function): #this is going to show personal data
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Progress", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	name_label = Label(window, text = "Lastname Firstname", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	name_label.place(x=20, y = 100)

	study_label = Label(window, text = "Study", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	study_label.place(x=20, y = 130)

	study_label = Label(window, text = "Start Year", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	study_label.place(x=20, y = 160)

	AcademicYear_label = Label(window, text = "Academic Year ", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	AcademicYear_label.place(x=20, y = 190)

	totalCredits_label = Label(window, text = "Total Credits ", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	totalCredits_label.place(x=20, y = 220)

	earnedCredits_label = Label(window, text = "Earned Credits ", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	earnedCredits_label.place(x=20, y = 250)

	avgGP_label = Label(window, text = "Average Grade Point ", fg = "#006386", font = "Arial 10  bold", bg ="#EBEBE9")
	avgGP_label.place(x=20, y = 280)

	return_course = Button(window,text = "Return to Exam Result", fg = "#2E4053", font = "Arial 12  bold", highlightbackground ="#48C9B0", height = 1,width = 20,borderwidth=2,cursor = get_handcursor(), relief="groove", command = partial(ui.StudentExamResult.student_results,window, return_function))
	return_course.place(x = 150, y = 550)



	go_back(window, return_function)
	sign_out(window)