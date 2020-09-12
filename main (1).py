from tkinter import *
from tkinter import messagebox, ttk
from random import *
import tkinter as tk



def taskdo(name, unique):

    def show_tasks():
        app_4 = tk.Toplevel(app,bg='#0A0A0A')
        app_4.geometry('1290x500')

        trans_label = Label(
            app_4, text="All Task Entries", font=('bold', 30, 'italic'),fg='#EE6363',bg='#0A0A0A')
        trans_label.grid(row=1, column=1)
        frm = Frame(app_4)
        frm.grid(row=2, column=1, padx=30, pady=20)

        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6),
                          show="headings", height="10")
        tv.grid(row=3, column=2)

        tv.heading(1, text="User-ID", anchor=CENTER)
        tv.heading(2, text="Unique-ID", anchor=CENTER)
        tv.heading(3, text="Task", anchor=CENTER)
        tv.heading(4, text="Place", anchor=CENTER)
        tv.heading(5, text="Important Details", anchor=CENTER)
        tv.heading(6, text="Task Date", anchor=CENTER)

        def delete_selected():
            del_list = list()
            del_list_1 = list()
            for i in tv.selection():
                deleting = tv.set(i, '#6')
                tv.delete(i)

                with open('tasks.txt', 'r') as file:
                    for line in file:
                        line = line.split('/')
                        del_list.append(line)

                    for i in del_list:
                        if deleting in i:
                            del_list.remove(i)
                        else:
                            continue
                    print(del_list) 

                    for j in del_list:
                        j = '/'.join(j)
                        del_list_1.append(j)

                    with open('tasks.txt', 'w') as file:
                        file.writelines(del_list_1)




        delete = Button(app_4, text='Delete The Selected Task', font=(
            'bold', 15), command=delete_selected , bg='#EE6363')
        delete.grid(row=7, column=1)

        with open('tasks.txt', 'r') as file:
            trans_list = list()
            for line in file:
                line = line.split('/')

                trans_list.append(line)

            for i in trans_list:
                if name in i or unique in i:
                    tv.insert('', 'end', values=i)
                else:
                    continue

    def trans_entry():
        task = task_name.get()
        place = place_name.get()
        imp_details = task_details.get()
        task_date = trans_date.get()

        with open('tasks.txt', 'a') as file:
            file.write(name+'/')
            file.write(unique+'/')
            file.write(task+'/')
            file.write(place+'/')
            file.write(imp_details+'/')
            file.write(task_date+'/'+'\n')



        messagebox.showinfo('Success!', 'Your Task Has Been Saved')



    app_3 = tk.Toplevel(app,bg='#0A0A0A')
    app_3.geometry('690x900')
    label = Label(app_3, text="                 Your To-Do list", font=('bold', 28, 'italic') ,fg='#EE6363',bg='#0A0A0A')
    label.grid(row=0, column=0)
    user_id = Label(app_3, text='User-ID:'+name,
                    font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    user_id.grid(row=1, column=0)
    unique_id = Label(app_3, text='Unique-ID:'+unique,
                      font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    
    unique_id.grid(row=1, column=1)



    task_label = Label(app_3, text='Enter the task:',
                      font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    task_label.grid(row=2, column=0)
    task_name = StringVar()
    task_entry = Entry(app_3, textvariable=task_name, font=('bold', 15))
    task_entry.grid(row=2, column=1)

    place_label = Label(app_3, text='Enter the place of task:',
                                   font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    place_label.grid(row=3, column=0)
    place_name = StringVar()
    place_entry = Entry(
        app_3, textvariable=place_name, font=('bold', 15))
    place_entry.grid(row=3, column=1)

    imp_details = Label(app_3, text='Enter the task Details:',
                                font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    imp_details.grid(row=4, column=0)
    task_details = StringVar()
    task_details_entry = Entry(
        app_3, textvariable=task_details, font=('bold', 15))
    task_details_entry.grid(row=4, column=1)

    task_date = Label(app_3, text='Enter the Date of the task:',
                             font=('bold', 15, 'italic'), pady=40, padx=40,fg='#20B2AA',bg='#0A0A0A')
    task_date.grid(row=5, column=0)
    trans_date = StringVar()
    task_date_entry = Entry(
        app_3, textvariable=trans_date, font=('bold', 15))
    task_date_entry.grid(row=5, column=1)

    submit = Button(app_3, text='Submit', font=(
        'bold', 15), command=trans_entry, bg='#EE6363')
    submit.grid(row=6, column=1)

    show_trans = Button(app_3, text="Show all tasks", font=(
        'bold', 15), command=show_tasks, bg='#EE6363')
    show_trans.grid(row=6, column=0)

    space_2 = Label(app_3, text="",bg='#0A0A0A')
    space_2.grid(row=7, column=1)

    space_2 = Label(app_3, text="",bg='#0A0A0A')
    space_2.grid(row=8, column=1)

    quit_button = Button(app_3, text='Quit', font=(
        'bold', 15), command=app.quit, bg='#EE6363').grid(row=9, column=1)


def login():
    with open('file.txt', 'r') as f:
        # print(f.readlines())
        password = pwd_2.get()
        print(password)
        name = user_name.get()
        print(name)
        unique = unique_id.get()
        for line in f:
            line = line.rstrip()
            if re.search(name, line) and re.search(password, line) and re.search(unique, line):
                taskdo(name, unique)
                break
            else:
                continue
        else:
            messagebox.showerror('Failed!', 'You Entered Wrong details')


def createNewWindow():
    def signin():
        with open('file.txt', 'r') as f:
            # print(f.readlines())
            password = pwd_1.get()
            print(password)
            name = user.get()
            print(name)
            uniqueID = unique
            print(uniqueID)
            
            for line in f:
                line = line.rstrip()
                if re.search(name, line):
                    messagebox.showinfo('Error!', 'Name already exists')
                    break
                else:
                    continue
            else:
                with open('file.txt', 'a') as file:
                    file.write(name+'/')
                    file.write(password + '/')
                    file.write(str(uniqueID)+'/'+'\n')



                messagebox.showinfo('Success!', 'Signin Successful')

    app_2 = tk.Toplevel(app)
    # username entry
    main = Label(app_2, text='Signup', font=('bold', 25, 'italic'),fg='#EE6363')
    main.grid(row=0, column=0)
    user = StringVar()
    user_label_1 = Label(app_2, text='Enter UserName: ',
                         font=('bold', 15, 'italic'), pady=30, padx=30,fg='#20B2AA')
    user_label_1.grid(row=1, column=0)
    user_entry_1 = Entry(app_2, textvariable=user, font=('bold', 15))
    user_entry_1.grid(row=1, column=1)

    pwd_1 = StringVar()
    pwd_label_1 = Label(app_2, text='Enter Password: ',
                        font=('bold', 15, 'italic'),fg='#20B2AA')
    pwd_label_1.grid(row=2, column=0)
    pwd_entry_1 = Entry(app_2, textvariable=pwd_1, font=('bold', 15), show='*')
    pwd_entry_1.grid(row=2, column=1)

    unique = randint(21000, 56633)

    unique_label = Label(app_2, text='Your Unique-ID is:',
                         font=('bold', 15, 'italic'), pady=30, padx=30,fg='#20B2AA')
    unique_label.grid(row=6, column=1)

    unique_label_id = Label(app_2, text=unique,
                            font=('bold', 15), fg='#20B2AA')
    unique_label_id.grid(row=7, column=1)




    # submit button
    submit_1 = Button(app_2, text='Submit', font=('bold', 15), command=signin , bg='#EE6363')
    submit_1.grid(row=6, column=0)

    app_2.title('Signup')
    app_2.geometry('500x400')


# creating a window
app = tk.Tk()


# Login
spa = Label(app, text="")
spa.grid(row=0, column=1)
main_1 = Label(app, text='Login', font=('bold', 25, 'italic'),fg='#EE6363')
main_1.grid(row=1, column=0)

user_name = StringVar()
user_label_2 = Label(app, text='Enter UserName: ',
                     font=('bold', 15, 'italic'), pady=30, padx=30,fg='#20B2AA')
user_label_2.grid(row=2, column=0)
user_entry_2 = Entry(app, textvariable=user_name, font=('bold', 15))
user_entry_2.grid(row=2, column=1)

pwd_2 = StringVar()
pwd_label_2 = Label(app, text='Enter Password: ',
                    font=('bold', 15, 'italic'),fg='#20B2AA')
pwd_label_2.grid(row=3, column=0)
pwd_entry_2 = Entry(app, textvariable=pwd_2, font=('bold', 15), show='*')
pwd_entry_2.grid(row=3, column=1)

spa = Label(app, text="")
spa.grid(row=4, column=1)
unique_id = StringVar()
unique_label = Label(app, text='Enter Unique-ID:', font=('bold', 15, 'italic'),fg='#20B2AA')
unique_label.grid(row=5, column=0)
unique_id_entry = Entry(app, textvariable=unique_id,
                        font=('bold', 15), show='*')
unique_id_entry.grid(row=5, column=1)


spa = Label(app, text="")
spa.grid(row=6, column=1)

# submit button
submit_2 = Button(app, text='Submit', font=('bold', 15), command=login , bg='#EE6363')
submit_2.grid(row=7, column=0)

spa = Label(app, text="")
spa.grid(row=8, column=0)

spa = Label(app, text="")
spa.grid(row=9, column=0)

spa = Label(app, text="")
spa.grid(row=10, column=0)

signin_label = Label(app, text='Are You a New User?',
                     font=('italic', 15,'italic'),fg='#20B2AA')
signin_label.grid(row=11, column=1)
# Signin
signin = Button(app, text='Sign-in', font=('bold', 15),
                command=createNewWindow, bg='#EE6363')
signin.grid(row=12, column=1)


app.title('Login')
app.geometry('500x500')
app.mainloop()
