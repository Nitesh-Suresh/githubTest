#github

list_student_name=[]
list_student_grade=[]
list_parent_name=[]
list_parent_number=[]
list_school_name=[]
list_course_enquiry=[]
number_of_students=0
student_record=[]
list_of_words=[]
special_word=[]


f=open('C:\\Users\\Satiz\\Desktop\\POP\\Level 3\\Assignment\\project1.dat','r')
list_of_lines=f.readlines()

    
n=len(list_of_lines)
for i in range(n):
        student_record=list_of_lines[i].strip()
        list_of_words= student_record.split(' ')
        student_name=list_of_words[0]
        student_grade=(list_of_words[1])
        student_schools=list_of_words[2]
        student_course_enquiry=list_of_words[3]
        parent_name=list_of_words[4]
        phone_number=int(list_of_words[5])

        list_student_name.append(student_name)
        list_student_grade.append(student_grade)
        list_school_name.append(student_schools)
        list_course_enquiry.append(student_course_enquiry)
        list_parent_name.append(parent_name)
        list_parent_number.append(phone_number)


def add_new_enquiry():
    global number_of_students
    student_name=entry_student_name.get()
    student_grade=int(entry_student_grade.get())
    student_schools=entry_school_name.get()
    student_course_enquiry=entry_course_enquiry.get()
    parent_name=entry_parent_name.get()
    phone_number=int(entry_parent_phone.get())


    list_student_name.append(student_name)
    list_student_grade.append(student_grade)
    list_school_name.append(student_schools)
    list_course_enquiry.append(student_course_enquiry)
    list_parent_name.append(parent_name)
    list_course_enquiry.append(phone_number)

    number_of_students=number_of_students+1

    f=open('C:\\Users\\Satiz\\Desktop\\POP\\Level 3\\Assignment\\project1.dat','a')
    output_msg=""
    output_msg="\n"+f"{student_name} {student_grade} {student_schools} {student_course_enquiry} {parent_name} {phone_number}"
    f.write(output_msg)

    status_message=f"{student_name}, {student_grade}, {student_schools}, {student_course_enquiry}, {parent_name} and {phone_number} added sucessfully"
    label_status.configure(text=status_message)


def display_enquiers():
    for item in treeview_display_enquiries.get_children():
        treeview_display_enquiries.delete(item)

    f=open('C:\\Users\\Satiz\\Desktop\\POP\\Level 3\\Assignment\\project1.dat','r')
    list_of_lines=f.readlines()

    
    n=len(list_of_lines)
    for i in range(n):
            student_record=list_of_lines[i].strip()
            list_of_words= student_record.split(' ')
            student_name=list_of_words[0]
            student_grade=(list_of_words[1])
            student_schools=list_of_words[2]
            student_course_enquiry=list_of_words[3]
            parent_name=list_of_words[4]
            phone_number=int(list_of_words[5])

            list_student_name.append(student_name)
            list_student_grade.append(student_grade)
            list_school_name.append(student_schools)
            list_course_enquiry.append(student_course_enquiry)
            list_parent_name.append(parent_name)
            list_parent_number.append(phone_number)
    
    for i in range(n):
        treeview_display_enquiries.insert(parent='',index='end', values=list_of_lines[i])

def search_name():
    
    key_name=entry_search_name.get()

    if key_name.strip()=='':
        label_status.configure(text='To Search the value you have to enter the Name ')
        return


    for i in range(n):

        if list_student_name[i].lower().startswith(key_name.lower()):
            #list_of_words=f"{list_student_name[i]} {list_student_grade[i]} {list_school_name[i]} {list_course_enquiry[i]} {list_parent_name[i]} {list_parent_number[i]}"
            #print(list_of_words)
            treeview_display_enquiries.insert(parent='',index='end', values=list_of_lines[i])
            

def clear_enquiers():
    for item in treeview_display_enquiries.get_children():
        treeview_display_enquiries.delete(item)

def asc_name():

    for i in range(n-1):
        for j in range(n-i-1):
            if list_student_name[j] > list_student_name[j+1]:

                temp=list_student_name[j+1]
                list_student_name[j+1]=list_student_name[j]
                list_student_name[j]=temp

                temp=list_student_grade[j+1]
                list_student_grade[j+1]=list_student_grade[j]
                list_student_grade[j]=temp

                temp=list_school_name[j+1]
                list_school_name[j+1]=list_school_name[j]
                list_school_name[j]=temp

                temp=list_course_enquiry[j+1]
                list_course_enquiry[j+1]=list_course_enquiry[j]
                list_course_enquiry[j]=temp

                temp=list_parent_name[j+1]
                list_parent_name[j+1]=list_parent_name[j]
                list_parent_name[j]=temp

                temp=list_parent_number[j+1]
                list_parent_number[j+1]=list_parent_number[j]
                list_parent_number[j]=temp
    
    for i in range(n):
        enquiry = []
        enquiry.append(list_student_name[i])
        enquiry.append(list_student_grade[i])
        enquiry.append(list_school_name[i])
        enquiry.append(list_course_enquiry[i])
        enquiry.append(list_parent_name[i])
        enquiry.append(list_parent_number[i])
        treeview_display_enquiries.insert(parent='',index='end', values=enquiry)

    '''
    for i in range(n):
    
            output_message=output_message + f"{list_student_name[i]} "
            output_message=output_message + f"{list_student_grade[i]} "
            output_message=output_message + f"{list_school_name[i]} "
            output_message=output_message + f"{list_course_enquiry[i]} "
            output_message=output_message + f"{list_parent_name[i]} "
            output_message=output_message + f"{list_parent_number[i]} "

            treeview_display_enquiries.insert(parent='',index='end', values=output_message[i])
    '''


    #print(output_message)
    
    #for i in range (n):
        #print(list_student_name[i])
        #output_message=f"{list_student_name[i]}"
        #treeview_display_enquiries.insert(parent='',index='end', values=output_message)'''
        #treeview_display_enquiries.insert(parent='',index='end', values=list_student_grade[i])

def dec_name():
    for i in range(n-1):
        for j in range(n-i-1):
            if list_student_name[j] < list_student_name[j+1]:

                temp=list_student_name[j+1]
                list_student_name[j+1]=list_student_name[j]
                list_student_name[j]=temp

                temp=list_student_grade[j+1]
                list_student_grade[j+1]=list_student_grade[j]
                list_student_grade[j]=temp

                temp=list_school_name[j+1]
                list_school_name[j+1]=list_school_name[j]
                list_school_name[j]=temp

                temp=list_course_enquiry[j+1]
                list_course_enquiry[j+1]=list_course_enquiry[j]
                list_course_enquiry[j]=temp

                temp=list_parent_name[j+1]
                list_parent_name[j+1]=list_parent_name[j]
                list_parent_name[j]=temp

                temp=list_parent_number[j+1]
                list_parent_number[j+1]=list_parent_number[j]
                list_parent_number[j]=temp
    for i in range(n):
        enquiry = []
        enquiry.append(list_student_name[i])
        enquiry.append(list_student_grade[i])
        enquiry.append(list_school_name[i])
        enquiry.append(list_course_enquiry[i])
        enquiry.append(list_parent_name[i])
        enquiry.append(list_parent_number[i])
        treeview_display_enquiries.insert(parent='',index='end', values=enquiry)

    


def delete_name():
    key_name=entry_search_name.get()

    if key_name.strip()=='':
        label_status.configure(text='To Delete the value you have to enter the Name ')
        return

    f=open('C:\\Users\\Satiz\\Desktop\\POP\\Level 3\\Assignment\\project1.dat','w') 

    for i in range(n):

        if list_student_name[i].lower().startswith(key_name.lower()):
            #list_of_words=f"{list_student_name[i]} {list_student_grade[i]} {list_school_name[i]} {list_course_enquiry[i]} {list_parent_name[i]} {list_parent_number[i]}"
            #print(list_of_words)

            list_of_lines.remove(list_of_lines[i])
        
    print(list_of_lines)
    
    for i in range(n):
        treeview_display_enquiries.insert(parent='',index='end', values=list_of_lines[i])

    

import tkinter as tk
from tkinter import ttk

root_window=tk.Tk()
root_window.geometry('1400x800')
root_window.configure(background='Yellow')

label_heading= tk.Label(
    master= root_window,
    text="Enquiry Management System",
    font=('Arial',20,'bold','underline'),
    background='red',
    foreground='white'
)

label_frame_display_enquieries= tk.LabelFrame(
    master=root_window,
    text="Display Enquiries",
    font=('Arial',15,'italic'),
    background='royalblue',
    foreground='white'
)

label_frame_input= tk.LabelFrame(
    master=root_window,
    text="Enter Data",
    font=('Arial',15,'italic'),
    background='royalblue',
    foreground='white'
)

label_frame_operation= tk.LabelFrame(
    master=root_window,
    text="Operations",
    font=('Arial',15,'italic'),
    background='royalblue',
    foreground='white'
)

button_display_enquiers=tk.Button(
    master=label_frame_operation,
    text='Display All Enquiers',
    font=('Arial',15,'italic'),
    background='chocolate',
    foreground='black',
    command=display_enquiers
)

button_clear_all_enquiers=tk.Button(
    master=label_frame_operation,
    text='Clear All Enquiers',
    font=('Arial',15,'italic'),
    background='chocolate',
    foreground='black',
    command=clear_enquiers
)

button_asc=tk.Button(
    master=label_frame_operation,
    text='Acending Names',
    font=('Arial',15,'italic'),
    background='chocolate',
    foreground='black',
    command=asc_name
)

button_dec=tk.Button(
    master=label_frame_operation,
    text='Decending Names',
    font=('Arial',15,'italic'),
    background='chocolate',
    foreground='black',
    command=dec_name
)

treeview_display_enquiries=ttk.Treeview(
    master=label_frame_display_enquieries,
    columns=(1,2,3,4,5,6),
    show='headings',
    height=5
)

treeview_display_enquiries.heading(1, text="Student Name")
treeview_display_enquiries.heading(2, text="Student Grade")
treeview_display_enquiries.heading(3, text="School Name")
treeview_display_enquiries.heading(4, text="Course Required")
treeview_display_enquiries.heading(5, text="Parent Name")
treeview_display_enquiries.heading(6, text="Parent Phone no")

label_frame_input_student_details=tk.LabelFrame(
    master=label_frame_input,
    text="Student Details",
    font=('Arial',15,'italic'),
    background='crimson',
    foreground='white'
)

label_frame_input_parent_details=tk.LabelFrame(
    master=label_frame_input,
    text="Parent Details",
    font=('Arial',15,'italic'),
    background='crimson',
    foreground='white'
)

label_frame_button_operation=tk.LabelFrame(
    master=label_frame_input,
    width=200,
    height=50,
    text="Operations",
    font=('Arial',15,'italic'),
    background='crimson',
    foreground='white'
)
""" label_frame_input_student_details.grid(row=0,column=0,padx=5,pady=10)
label_frame_input_parent_details.grid(row=0,column=2,padx=5,pady=10) """

label_frame_button_operation.pack(side=tk.RIGHT,fill='both',expand='yes',padx=5,pady=10)
label_frame_input_student_details.pack(side=tk.LEFT,fill='both', expand='yes',padx=5,pady=10)
label_frame_input_parent_details.pack(side=tk.LEFT,fill='both', expand='yes',padx=5,pady=10)


#Student Name
label_student_name=tk.Label(
    master=label_frame_input_student_details,
    text='Enter Student Name:',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_student_name=tk.Entry(
    master=label_frame_input_student_details,
    font=('Arial',15,'italic')
)

label_student_name.grid(row=0,column=0,padx=5,pady=10)
entry_student_name.grid(row=0,column= 1,padx=5,pady=10)

#Student Grade
label_student_grade=tk.Label(
    master=label_frame_input_student_details,
    text='Enter Student Grade:',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_student_grade=tk.Entry(
    master=label_frame_input_student_details,
    font=('Arial',15,'italic')  
)

label_student_grade.grid(row=2,column=0,padx=5,pady=10)
entry_student_grade.grid(row=2,column=1,padx=5,pady=10)

#Student School name
label_school_name=tk.Label(
    master=label_frame_input_student_details,
    text='Enter School Name:',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_school_name=tk.Entry(
    master=label_frame_input_student_details,
    font=('Arial',15,'italic')  
)

label_school_name.grid(row=3,column=0,padx=5,pady=10)
entry_school_name.grid(row=3,column=1,padx=5,pady=10)


#Student Course Enquiry
label_course_enquiry=tk.Label(
    master=label_frame_input_student_details,
    text='Enter Course Name',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_course_enquiry=tk.Entry(
    master=label_frame_input_student_details,
    font=('Arial',15,'italic') 
)

label_course_enquiry.grid(row=4,column=0,padx=5,pady=10)
entry_course_enquiry.grid(row=4,column=1,padx=5,pady=10)

#Parent Name
label_parent_name=tk.Label(
    master=label_frame_input_parent_details,
    text='Enter Parent Name:',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_parent_name=tk.Entry(
    master=label_frame_input_parent_details,
    font=('Arial',15,'italic') 
)

label_parent_name.grid(row=0,column=0,padx=5,pady=10)
entry_parent_name.grid(row=0,column= 1,padx=5,pady=10)

#parent number
label_parent_phone=tk.Label(
    master=label_frame_input_parent_details,
    text='Enter Parent phone no:',
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

entry_parent_phone=tk.Entry(
    master=label_frame_input_parent_details,
    font=('Arial',15,'italic') 
)

label_parent_phone.grid(row=2,column=0,padx=5,pady=10)
entry_parent_phone.grid(row=2,column=1,padx=5,pady=10)

label_status= tk.Label(
    master= label_frame_input_parent_details,
    text="Sucess Message",
    font=('Arial',15,'bold'),
    background='darkslategrey',
    foreground='white'  
)

label_status.grid(rowspan=4,columnspan=3, padx=5,pady=10)



#button_Add
button_add_details=tk.Button(
    master=label_frame_button_operation,
    width=15,
    height=1,
    text='Add the details',
    font=('Arial',15,'italic'),
    background='chocolate',
    foreground='white',
    command=add_new_enquiry
)

label_name= tk.Label(
    master= label_frame_button_operation,
    text="Name:",
    font=('Arial',15,'italic'),
    background='darkslategrey',
    foreground='white'
)

button_add_details.grid(row=1,columnspan=3,padx=5,pady=10)
label_name.grid(row=2,column= 0,padx=5,pady=10)

entry_search_name=tk.Entry(
    master=label_frame_button_operation,
    font=('Arial',15,'italic')
)

entry_search_name.grid(row=2,column= 1,padx=5)

#button_Search
button_search_details=tk.Button(
    master=label_frame_button_operation,
    width=10,
    height=1,
    text='Search Name',
    font=('times',15,'roman'),
    background='chartreuse',
    foreground='Black',
    command=search_name
)

button_search_details.grid(row=3,column=0,padx=5,pady=10)




#button_delete
button_delete_details=tk.Button(
    master=label_frame_button_operation,
    width=10,
    height=1,
    text='Delete',
    font=('times',15,'roman'),
    background='chartreuse',
    foreground='Black',
    command=delete_name
)

button_delete_details.grid(row=3,column=1,padx=5,pady=10)

label_heading.pack()

label_frame_display_enquieries.pack(fill='both', expand='yes', padx=10,pady=10)
label_frame_input.pack(fill='both', expand='yes', padx=10,pady=10)
label_frame_operation.pack(fill='both', expand='yes', padx=10,pady=10)

button_clear_all_enquiers.grid(row=0,column=0, padx=10, pady=10)
button_display_enquiers.grid(row=0,column=1, padx=10, pady=10)
button_asc.grid(row=0,column=2, padx=10, pady=10)
button_dec.grid(row=0,column=3, padx=10, pady=10)

treeview_display_enquiries.pack(fill='both', expand='yes', padx=20,pady=20)

tk.mainloop()