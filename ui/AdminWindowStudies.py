from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.AdminWindowStudyEdit import study_overview_edit
from ui.AdminWindowStudyView import study_over_view
from ui.AdminWindowStudyCreateNew import create_study
from tkinter.messagebox import askquestion
from ui.SignOut import sign_out
from functools import partial


def admin_window_studies(window,return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "An Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 150, y = 15)

	create_data_text = Button(text = "Create new studies", fg = "#e6b800", font="Arial 12", width = 15, cursor = get_handcursor(), highlightbackground =  "#006386", command = partial(create_study,window,return_function))
	create_data_text.place(x=20, y = 80, height = 40)

	header_label1 = Label(window, text = "#",fg = "#e6b800", font="Arial 10 bold", width = 3,bg ="#006386")
	header_label1.place(x=10, y = 125, height=30)
	header_label2 = Label(window, text = "Title",fg = "#e6b800", font="Arial 10 bold", width = 15,bg ="#006386")
	header_label2.place(x=40, y = 125, height=30)
	header_label3 = Label(window, text = "Description",fg = "#e6b800", font="Arial 10 bold", width = 15,bg ="#006386" )
	header_label3.place(x=180, y = 125, height=30)
	header_label4 = Label(window, text = "Action",fg = "#e6b800", font="Arial 10 bold", bg ="#006386" )
	header_label4.place(x=320, y = 125, width=165, height=30)

	studies = ["abc","def","ghi","jkl","mno"]
	descriptions = ["abcdefghi","abcdefghi","abcdefghi","abcdefghi","abcdefghi"]
	num_pos_y = 158
	#initial_num = 0
	y_position = 160
	for i in range (len(studies)):
		number_label = Label(window, text = (i + 1),fg = "#00293c", font = "Arial 13", height = 2, width = 3 )
		number_label.place(x = 10, y = num_pos_y, height=30)
		#initial_num += 1
		course_label = Label(window, text = studies[i],fg = "#00293c", font = "Arial 13", height = 2, width = 15)
		course_label.place(x = 40, y = num_pos_y, height=30)

		desc_label = Label(window, text = descriptions[i],fg = "#00293c", font = "Arial 13",  height = 2, width = 15)
		desc_label.place(x = 180 , y = num_pos_y, height=30)

		bg_label = Label(window)
		bg_label.place(x=320, y= num_pos_y, width = 165, height=30)
		num_pos_y += 30

		view_button = Button(window, text = "View",font = "Arial 10", fg = "#006386", bg = "#ccd9ff",highlightbackground = "#ccd9ff",cursor = get_handcursor(), width = 4, relief = FLAT,command = partial(study_over_view, window, return_function))
		view_button.place(x= 330, y = y_position, height=26)

		edit_button = Button(window, text = "Edit",font = "Arial 10", fg = "#006386",bg = "#fff2cc",highlightbackground = "#fff2cc",cursor = get_handcursor(), width = 4, relief = FLAT,command = partial(study_overview_edit, window, return_function))
		edit_button.place(x= 380, y = y_position, height=26)

		def confirm_deletion():
			askquestion(title="Delete Data", message= "Do you want to process?", icon = "warning")

		delete_button = Button(window, text = "Delete",font = "Arial 10", fg = "#006386",bg = "#ffcccc",highlightbackground = "#ffcccc",cursor = get_handcursor(), width = 5, relief = FLAT, command = confirm_deletion)
		delete_button.place(x= 430, y = y_position, height=26)
		y_position += 30

	go_back(window, return_function)
	sign_out(window)

"""
	create_pic = Image.open("images/create-w.png")
	create_pic = create_pic.resize((30,30), Image.ANTIALIAS)
	create_image =ImageTk.PhotoImage(create_pic)
	create_image.icon = create_image
	create_data = Button(window, image = create_image, cursor = get_handcursor())
	create_data.place(x=20, y = 80)
"""
