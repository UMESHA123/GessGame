import tkinter as tk
from tkcalendar import *
from tkinter import *
from tkinter import ttk

class GessGame():
    def __init__(self,root):
        self.root=root
        self.root.title(f"Gess Game")
        self.root.geometry('1000x600+200+10')
        self.root.resizable(False,False)
        self.root.config(bg='white')

        ######################## all variable here ########################
        self.num = IntVar()
        self.label_frame = StringVar()
        self.num_place_list = IntVar()
        self.var_count=IntVar()
        self.var_name=StringVar()
        self.num_place_entry=IntVar()
        self.next_num_place_entry=IntVar()
        self.result =StringVar()
        ######################## end all variable here ####################
        top_label=tk.Label(self.root,text='Gess Game',font=('times new roman',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        menu_frame=tk.LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=10,y=45,width=980,height=55)
        name_label=Label(menu_frame,text='Enter your name:',font=("times new roman",13,'bold'),bg='white',fg='black').grid(row=0,column=0,padx=5,pady=10)
        name_entry=ttk.Entry(menu_frame,width=40,textvariable=self.var_name).grid(row=0,column=1,padx=5,pady=10)

        coount=Label(menu_frame,text='Enter the Length of word:',font=("times new roman",13,'bold'),bg='white',fg='black').grid(row=0,column=2,padx=5,pady=10)
        count_entry=ttk.Entry(menu_frame,width=30,textvariable=self.var_count).grid(row=0,column=3,padx=5,pady=10)

        button1=ttk.Button(menu_frame,text='Enter',width=20,command=self.start).grid(row=0,column=4,padx=4,pady=10)
    def start(self):
        self.root.title(f"Gess Game played by {str(self.var_name.get())}")
        top_label=tk.Label(self.root,text=f'Gess Game played by {str(self.var_name.get())}',font=('times new roman',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)
        frame=Frame(self.root,width=980,height=480,bg='black')
        frame.place(x=10,y=110)

        self.label_frame = LabelFrame(frame,width=980,height=480)
        self.label_frame.place(x=0,y=0)

        label_col_1 = Label(self.label_frame,text='column-1',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=10)
        label_col_2 = Label(self.label_frame,text='column-2',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=10)
        label_col_3 = Label(self.label_frame,text='column-3',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=10)
        label_col_4 = Label(self.label_frame,text='column-4',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=10)
        label_col_5 = Label(self.label_frame,text='column-5',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=10)

        label_A = Label(self.label_frame,text='A',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=40)
        label_B = Label(self.label_frame,text='B',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=40)
        label_C = Label(self.label_frame,text='C',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=40)
        label_D = Label(self.label_frame,text='D',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=40)
        label_E = Label(self.label_frame,text='E',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=40)
        
        label_F = Label(self.label_frame,text='F',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=70)
        label_G = Label(self.label_frame,text='G',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=70)
        label_H = Label(self.label_frame,text='H',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=70)
        label_I = Label(self.label_frame,text='I',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=70)
        label_J = Label(self.label_frame,text='J',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=70)
       
        label_K = Label(self.label_frame,text='K',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=100)
        label_L = Label(self.label_frame,text='L',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=100)
        label_M = Label(self.label_frame,text='M',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=100)
        label_N = Label(self.label_frame,text='N',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=100)
        label_O = Label(self.label_frame,text='O',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=100)
        
        label_P = Label(self.label_frame,text='P',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=130)
        label_Q = Label(self.label_frame,text='Q',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=130)
        label_R = Label(self.label_frame,text='R',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=130)
        label_S = Label(self.label_frame,text='S',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=130)
        label_T = Label(self.label_frame,text='T',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=130)
       
        label_U = Label(self.label_frame,text='U',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=10,y=160)
        label_V = Label(self.label_frame,text='V',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=110,y=160)
        label_W = Label(self.label_frame,text='W',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=160)
        label_X = Label(self.label_frame,text='X',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=310,y=160)
        label_Y = Label(self.label_frame,text='Y',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=410,y=160)
        
        label_Z = Label(self.label_frame,text='Z',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=210,y=190)
        
        greet_label_with_name = Label(self.label_frame,text=(f'Hi  {(self.var_name.get())}.'),fg='black',font=('times new roman',13)).place(x=540,y=10)
          
        greet_label_with_name = Label(self.label_frame,text=(f'Hi please enter first letter to end  letter in which column.'),fg='black',font=('times new roman',13)).place(x=540,y=40)
        num_place_entry=ttk.Entry(self.label_frame,width=50,textvariable=self.num_place_entry)
        num_place_entry.place(x=540,y=90)

        num_place_entry_button= ttk.Button(self.label_frame,text='Enter',width=50,command=self.num_place)
        num_place_entry_button.place(x=540,y=120)
        
        instraction = Label(self.label_frame,text='Instraction.',font=('times new roman',12,'bold'),fg='black').place(x=10,y=210)
        instraction1 = Label(self.label_frame,text='1-->Enter the length of the word.',font=('times new roman',10,'bold'),fg='blue').place(x=10,y=230)
        instraction2 = Label(self.label_frame,text='2-->Enter 1st letter in which column like that enter the n-1 letter in the order.In the entry field',font=('times new roman',10,'bold'),fg='blue').place(x=10,y=250)
        instraction3 = Label(self.label_frame,text="3-->Ex. If imagin the 'WORD' then total length is 4 and 'W' in the column-3  and 'o'. In the column-5 'R' in the column-3 and 'D' in the column-4 ",font=('times new roman',10,'bold'),fg='blue').place(x=10,y=270)
        instraction4 = Label(self.label_frame,text='4-->After click on the next button you will get the one more pop window.',font=('times new roman',10,'bold'),fg='blue').place(x=10,y=290)
        instraction5 = Label(self.label_frame,text="5-->Repeat the step-4 by useing the pop window.",font=('times new roman',10,'bold'),fg='blue').place(x=10,y=310)
        instraction6 = Label(self.label_frame,text="6-->Reapet the step-2 and then enter the num in the entery filed and then the click on the next button",font=('times new roman',10,'bold'),fg='blue').place(x=10,y=330)
        instraction7 = Label(self.label_frame,text='Finally you get the one more button called RESULT button.To click on the RESULT button to dilplay the final result.',font=('times new roman',10,'bold'),fg='blue').place(x=10,y=350)
        instraction8 = Label(self.label_frame,text='For more information click on this button...',font=('times new roman',12,'bold'),fg='black').place(x=10,y=370)
        instraction_button = ttk.Button(self.label_frame,text="More info...")
        instraction_button.place(x=300,y=370)
    def num_place(self):
        self.next_aplhabet_table = Toplevel(self.root)
        self.next_aplhabet_table.geometry("600x600")
        self.next_aplhabet_table.title("Next alphabet table")

        label_col_1 = Label(self.next_aplhabet_table,text='column-1',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=80,y=10)
        label_col_2 = Label(self.next_aplhabet_table,text='column-2',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=180,y=10)
        label_col_3 = Label(self.next_aplhabet_table,text='column-3',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=280,y=10)
        label_col_4 = Label(self.next_aplhabet_table,text='column-4',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=380,y=10)
        label_col_5 = Label(self.next_aplhabet_table,text='column-5',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=480,y=10)

        col_1='AFKPU'
        col_2='BGLQV'
        col_3='CHMRWZ'
        col_4='DINSY'
        col_5='EJOTY'
        next_letter_order = []
        next_alphabel_table = []
        #print(self.num_place_entry.get())
        for letter_place_number in str(self.num_place_entry.get()):
            #print(letter_place_number)
            letter_place_number = int(letter_place_number)
            if letter_place_number == 1:
                next_letter_order.append(col_1)
            elif letter_place_number == 2:
                next_letter_order.append(col_2)
            elif letter_place_number == 3:
                next_letter_order.append(col_3)
            elif letter_place_number == 4:
                next_letter_order.append(col_4)
            elif letter_place_number == 5:
                next_letter_order.append(col_5)
        for row in next_letter_order:
            next_alphabel_table.append(row)
        #print(next_alphabel_table)  
        x_value = 80
        y_value = 40
        for i in range(self.var_count.get()):
            for j in range(5):
                label_1 = Label(self.next_aplhabet_table,text=f'{str(next_alphabel_table[i][j])}',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=10).place(x=x_value,y=y_value)
                x_value = x_value + 100
            x_value =80
            y_value = y_value + 30
        row_x_value = 10
        row_y_value = 40
        for i in range(self.var_count.get()):
            label_1 = Label(self.next_aplhabet_table,text=f' row {str(i)}',font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=7).place(x=row_x_value,y=row_y_value)
            row_y_value = row_y_value + 30    
        next_letter_place_number_list=[]

        def next_num_place():

            def result_show():
                final_result = Label(self.label_frame,text=f"Your imagen word is : {str(self.result)} !......😍👨‍💻💻",font = ("times new roman",13),bg='white',fg='black',relief=GROOVE,width=55,height=3).place(x=10,y=405)
            

            for j in str(self.next_num_place_entry.get()):
                next_letter_place_number_list.append(j)
            result = ""
            for i in range((self.var_count.get())):
                for j in next_letter_place_number_list:
                    j = int(j)
                    #print(next_alphabel_table[i][j-1])
                    result = result + str(next_alphabel_table[i][j-1])
                    next_letter_place_number_list.remove(str(j))
                    break
            #print(result)
            self.result = result
            result_button= ttk.Button(label_frame,text='Result',width=45,command=result_show)
            result_button.place(x=5,y=120)

      
        label_frame = LabelFrame(self.label_frame,width=300,height=150)
        label_frame.place(x=650,y=300)
        greet_label_with_name = Label(label_frame,text=(f'Hi please again enter first letter to end\nform pop window letter in which column.'),fg='black',font=('times new roman',13)).place(x=5,y=5)
        num_place_entry=ttk.Entry(label_frame,width=45,textvariable=self.next_num_place_entry)
        num_place_entry.place(x=5,y=50)
        next_num_place_entry_button= ttk.Button(label_frame,text='Next',width=45,command=next_num_place)
        next_num_place_entry_button.place(x=5,y=80)
  
if __name__=='__main__':
    root=tk.Tk()
    ob1=GessGame(root)
    root.mainloop()