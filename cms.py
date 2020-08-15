from csv import DictReader,DictWriter
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font
import os

root=tk.Tk()
root.title('Contact List')
root.geometry('700x400')
root.resizable(0, 0)

# variable
fname=tk.StringVar()
lname=tk.StringVar()
gender=tk.StringVar()
age=tk.StringVar()
address=tk.StringVar()
contact=tk.StringVar()

# add data in csv file
def Database():
   with open('data.csv','r') as fp:
      csv_reader=DictReader(fp,delimiter=',')
      for row in csv_reader:
         fname = row['First Name']
         lname = row['Last Name']
         gender = row['Gender']
         age = row['Age']
         address = row['Address']
         contact = row['Contact']
         tree.insert("", 0, values=(0,fname,lname,gender,age,address,contact))

# add new contact functionality
def new_contact_action():
   add_window=tk.Toplevel()
   add_window.geometry('400x400')
   add_window.title('Add Contact')
   add_window.resizable(0,0)

   # label frame
   add_frame=ttk.LabelFrame(add_window,text='ADDING NEW CONTACT')
   add_frame.grid(row=0,column=0,padx=20,pady=20)

   # label loop
   add_labels=['First Name: ','Last Name: ','Gender: ','Age: ','Address: ','Contact: ']
   for i in range(len(add_labels)):
      current_label='label'+str(i)
      current_label=ttk.Label(add_frame,text=add_labels[i])
      current_label.grid(row=i,column=0,padx=10,pady=10,sticky=tk.W)

   # entry 
   fname=tk.StringVar()
   lname=tk.StringVar()
   gender=tk.StringVar()
   age=tk.StringVar()
   address=tk.StringVar()
   contact=tk.StringVar()

   fname_entry=ttk.Entry(add_frame,width=20,textvariable=fname)
   fname_entry.focus_set()
   lname_entry=ttk.Entry(add_frame,width=20,textvariable=lname)
   gender_entry=ttk.Combobox(add_frame,width=18,textvariable=gender,state='readonly')
   gender_entry['values']=('Male','Female','Other')
   gender_entry.current(1)
   age_entry=ttk.Entry(add_frame,width=20,textvariable=age)
   address_entry=ttk.Entry(add_frame,width=20,textvariable=address)
   contact_entry=ttk.Entry(add_frame,width=20,textvariable=contact)

   # entry grid
   fname_entry.grid(row=0,column=1,padx=10,pady=10)
   lname_entry.grid(row=1,column=1,padx=10,pady=10)
   gender_entry.grid(row=2,column=1,padx=10,pady=10)
   age_entry.grid(row=3,column=1,padx=10,pady=10)
   address_entry.grid(row=4,column=1,padx=10,pady=10)
   contact_entry.grid(row=5,column=1,padx=10,pady=10)

   def new_save_action():         
      with open('data.csv','a',newline='') as fp:
         dict_head=DictWriter(fp,fieldnames=['First Name','Last Name','Gender','Age','Address','Contact'])
         if fname.get()=='' or lname.get()=='' or gender.get()=='' or age.get()=='' or address.get()=='' or contact.get()=='':
            result=messagebox.showwarning('Warning','Please Complete The Required Field')
         else:
            if os.stat('data.csv').st_size==0:
               dict_head.writeheader()
            tree.delete(*tree.get_children())
            dict_head.writerow({'First Name':fname.get(),'Last Name':lname.get(),'Gender':gender.get(),'Age':age.get(),'Address':address.get(),'Contact':contact.get()})
            Database()

      fname_entry.delete(0,tk.END)
      lname_entry.delete(0,tk.END)
      gender_entry.delete(0,tk.END)
      age_entry.delete(0,tk.END)
      address_entry.delete(0,tk.END)
      contact_entry.delete(0,tk.END) 

   # save button
   save_btn=ttk.Button(add_frame,text='SAVE',command=new_save_action)
   save_btn.grid(row=7,columnspan=2,padx=4)

   add_window.mainloop()

def OnSelected(event):

   update_window=tk.Toplevel()
   update_window.geometry('400x400')
   update_window.title('Update Contact')
   update_window.resizable(0,0)

   current_item=tree.focus()
   content=(tree.item(current_item))
   # global selecteditems
   selecteditems=content['values']

   # label frame
   update_frame=ttk.LabelFrame(update_window,text='UPDATING CONTACT')
   update_frame.grid(row=0,column=0,padx=20,pady=20)

   # label loop
   add_labels=['First Name: ','Last Name: ','Gender: ','Age: ','Address: ','Contact: ']
   for i in range(len(add_labels)):
      current_label='label'+str(i)
      current_label=ttk.Label(update_frame,text=add_labels[i])
      current_label.grid(row=i,column=0,padx=10,pady=10,sticky=tk.W)

   # entry 
   fname=tk.StringVar()
   lname=tk.StringVar()
   gender=tk.StringVar()
   age=tk.StringVar()
   address=tk.StringVar()
   contact=tk.StringVar()

   contact.set(selecteditems[6])
   fname.set(selecteditems[1])
   lname.set(selecteditems[2])
   gender.set(selecteditems[3])
   age.set(selecteditems[4])
   address.set(selecteditems[5])

   fname_entry=ttk.Entry(update_frame,width=20,textvariable=fname)
   fname_entry.focus_set()
   lname_entry=ttk.Entry(update_frame,width=20,textvariable=lname)
   gender_entry=ttk.Combobox(update_frame,width=18,textvariable=gender,state='readonly')
   gender_entry['values']=('Male','Female','Other')
   gender_entry.current(1)
   age_entry=ttk.Entry(update_frame,width=20,textvariable=age)
   address_entry=ttk.Entry(update_frame,width=20,textvariable=address)
   contact_entry=ttk.Entry(update_frame,width=20,textvariable=contact)

   # entry grid
   fname_entry.grid(row=0,column=1,padx=10,pady=10)
   lname_entry.grid(row=1,column=1,padx=10,pady=10)
   gender_entry.grid(row=2,column=1,padx=10,pady=10)
   age_entry.grid(row=3,column=1,padx=10,pady=10)
   address_entry.grid(row=4,column=1,padx=10,pady=10)
   contact_entry.grid(row=5,column=1,padx=10,pady=10)

   # update contact funtionality
   def update_action():   
      # tree.delete(*tree.get_children())
      lines = list()
      with open('data.csv', 'r') as readFile:
         reader = csv.reader(readFile)
         for row in reader:
            lines.append(row)
            for field in row:
                  if field == selecteditems[1]:
                     lines.remove(row)
      with open('data.csv', 'w',newline='') as writeFile:
         writer = csv.writer(writeFile)
         writer.writerows(lines)

      with open('data.csv','a',newline='') as fp:
         dict_head=DictWriter(fp,fieldnames=['First Name','Last Name','Gender','Age','Address','Contact'])
         tree.delete(*tree.get_children())
         dict_head.writerow({'First Name':fname.get(),'Last Name':lname.get(),'Gender':gender.get(),'Age':age.get(),'Address':address.get(),'Contact':contact.get()})
         Database()

   # update button
   update_btn=ttk.Button(update_frame,text='UPDATE',command=update_action)
   update_btn.grid(row=7,columnspan=2,padx=4)
   
   update_window.mainloop()

# delete contact functionality
def delete_contact_action():
   if not tree.selection():
      result=messagebox.showwarning('Warning','You not selected any contact')
   else:
      result=messagebox.askokcancel('Delete','Are you sure you want to delete this record?')
      if result==True:
         current_item=tree.focus()
         contents=(tree.item(current_item))
         selecteditem = contents['values']
         tree.delete(current_item)
         lines = list()
         with open('data.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
               lines.append(row)
               for field in row:
                  if field == selecteditem[5]:
                     lines.remove(row)
         with open('data.csv', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

#label
heading=ttk.Label(root,text='CONTACT MANAGEMENT SYSTEM',font=('Arial',16,'bold'))
heading.pack(side=tk.TOP,fill=tk.X)

# label
input_label=tk.Label(root,bg='#6666ff')
input_label.pack(fill=tk.X)

# add and delete button
adds=tk.Button(input_label,text='ADD NEW CONTACT',bg="#28A745",fg='#ffffff',command=new_contact_action)
delete=tk.Button(input_label,text='DELETE CONTACT',bg="#DC3545",fg='#ffffff',command=delete_contact_action)

# grid
adds.grid(row=0,columnspan=3,padx=120)
delete.grid(row=0,column=6,padx=50)

# label 
input_frame=tk.LabelFrame(root,relief=tk.FLAT,bg='#6666ff')
input_frame.pack(fill=tk.X)

tree = ttk.Treeview(input_frame, columns=("MemberID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended")
tree.heading('MemberID', text="MemberID")
tree.heading('First Name', text="First Name")
tree.heading('Last Name', text="Last Name")
tree.heading('Gender', text="Gender")
tree.heading('Age', text="Age")
tree.heading('Address', text="Address")
tree.heading('Contact', text="Contact")
tree.column('#0', minwidth=0, width=0)
tree.column('#1', minwidth=0, width=0)
tree.column('#2', minwidth=0, width=80)
tree.column('#3', minwidth=0, width=120)
tree.column('#4', minwidth=0, width=90)
tree.column('#5', minwidth=0, width=80)
tree.column('#6', minwidth=0, width=120)
tree.column('#7', minwidth=0, width=120)
tree.pack()

tree.bind('<Double-Button-1>',OnSelected)

if __name__ == '__main__':
   Database()
   root.mainloop()