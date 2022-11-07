import tkinter as tk
from tkinter import *
from tkinter import ttk,filedialog,messagebox
import tkinter.font 
import tkinter.colorchooser
import pymysql as sql
import os

password=""

try:
    myfile=open("Password_file.txt",'r')
    content=myfile.read()
    passwd=content
    test_connection=sql.connect(host="localhost",user="root",password=passwd,database="performance_schema")
    test_connection.close()

except:
    while True:
        myfile2=open("Password_file.txt",'w')
        passwd=input("Enter MySQL server password:")
        myfile2.write(passwd)
        myfile2.close()
        try:
            test_connection=sql.connect(host="localhost",user="root",password=passwd,database="performance_schema")
            if test_connection.open==True:
                break
        except:
            continue




main_application = tk.Tk()
main_application.geometry("800x600+0+0")
main_application.title("Untitled - Text Editor")
main_application.wm_iconbitmap("notes.ico")

main_menu=tk.Menu()

new_icon=tk.PhotoImage(file = "icons/new.png")
open_icon=tk.PhotoImage(file = "icons/open.png")
save_icon=tk.PhotoImage(file = "icons/save.png")
save_as_icon=tk.PhotoImage(file = "icons/save_as.png")
exit_icon=tk.PhotoImage(file = "icons/exit.png")

file=tk.Menu(main_menu,tearoff=False)
#Edit Menu Icon

copy_icon=tk.PhotoImage(file="icons/copy.png")
paste_icon=tk.PhotoImage(file="icons/paste.png")
cut_icon=tk.PhotoImage(file="icons/cut.png")
clear_icon=tk.PhotoImage(file="icons/clear_all.png")
find_icon=tk.PhotoImage(file="icons/find.png")

edit=tk.Menu(main_menu,tearoff=False)

#View menu icon

tool_bar=tk.PhotoImage(file="icons/tool_bar.png")
status_bar=tk.PhotoImage(file="icons/status_bar.png")


view=tk.Menu(main_menu,tearoff=False)

#color image
light_theme=tk.PhotoImage(file="icons/white.png")
dark_theme=tk.PhotoImage(file="icons/black.png")
red_theme=tk.PhotoImage(file="icons/red.png")
blue_theme=tk.PhotoImage(file="icons/blue.png")
green_theme=tk.PhotoImage(file="icons/green.png")

color_theme=tk.Menu(main_menu,tearoff=False)

theme_choose=tk.StringVar()

#color theme set
color_icon=(light_theme,dark_theme,red_theme,blue_theme,green_theme)

color_dict={'Light Default':('#000000','#ffffff'),
            'Dark':('#c4c4c4','#2d2d2d'),
            'Red':('#36fffc','#f03932'),
            'Blue':('#ff6817','#2d97ed'),
            'Green':('#990096','#59ff38')}






main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)

tool_bar_label=ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

font_tuple=tkinter.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar_label,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))


font_box.grid(row=0,column=0,padx=5,pady=5)

#size box

size_variable=tk.IntVar()
font_size=ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state="readonly")
font_size["values"]=tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#bold button
bold_icon=tk.PhotoImage(file="icons/bold.png")
bold_btn=ttk.Button(tool_bar_label,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic button
italic_icon=tk.PhotoImage(file="icons/italic.png")
italic_btn=ttk.Button(tool_bar_label,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)


#underline button
underline_icon=tk.PhotoImage(file="icons/underline.png")
underline_btn=ttk.Button(tool_bar_label,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)


#font color button
font_color_icon=tk.PhotoImage(file="icons/font_color_icon.png")
font_color_btn=ttk.Button(tool_bar_label,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)


#left alignment button
align_left_icon=tk.PhotoImage(file="icons/align_left.png")
align_left_btn=ttk.Button(tool_bar_label,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)






#center alignment button
align_center_icon=tk.PhotoImage(file="icons/align_center.png")
align_center_btn=ttk.Button(tool_bar_label,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)


#right alignment button
align_right_icon=tk.PhotoImage(file="icons/align_right.png")
align_right_btn=ttk.Button(tool_bar_label,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#history button
history_icon=tk.PhotoImage(file="icons/history.png")
history_btn=ttk.Button(tool_bar_label,image=history_icon)
history_btn.grid(row=0,column=9,padx=5)

#text editor

text_editor=tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=TRUE)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and function

font_now="Arial"
font_size_now=16


def change_font(main_application):
    global font_now
    font_now=font_family.get()
    text_editor.configure(font=(font_now,font_size_now))

def change_size(main_application):
    global font_size_now
    font_size_now=size_variable.get()
    text_editor.configure(font=(font_now,font_size_now))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

# bold function

#print(tkinter.font.Font(text=text_editor["font"]).actual())

def bold_fun():
    text_get=tkinter.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"]=='normal':
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"]=='bold':
        text_editor.configure(font=(font_now,font_size_now,"normal"))
bold_btn.configure(command=bold_fun)

def Italic_fun():
    text_get=tkinter.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"]=='roman':
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"]=='italic':
        text_editor.configure(font=(font_now,font_size_now,"roman"))
italic_btn.configure(command=Italic_fun)

def under_line_fun():
    text_get=tkinter.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"]==0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"]==1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))
underline_btn.configure(command=under_line_fun)


def Color_choose():
    color_var=tkinter.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=Color_choose)

def align_left():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
align_left_btn.configure(command=align_left)

def align_center():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
align_center_btn.configure(command=align_center)

def align_right():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
align_right_btn.configure(command=align_right)

#history

def history(x,y):
    mycon=sql.connect(host="localhost",user="root",password=passwd,db="performance_schema")
    cursor=mycon.cursor()
    cursor.execute("show databases")
    databases=cursor.fetchall()
    if databases.count(('text_editor',))==1:
        pass
    else:
        cursor.execute("Create database Text_Editor")
    cursor.execute("use text_editor")
    cursor.execute("show tables")
    tables=cursor.fetchall()
    if tables.count(('history',))==1:
        pass
    else:
        cursor.execute("create table history(File_Name varchar(200),Path Varchar(200),Date varchar(200),Time varchar(200))")
    cursor.execute("insert into history values(%s,%s,curdate(),curtime())",(x,y))
    mycon.commit()
    
    


def historytable(event=None):
    history_popup=tk.Toplevel()
    history_popup.geometry("800x600")
    history_popup.title("History")
    history_popup.resizable(0,0)

    #find_fram=ttk.LabelFrame(find_popup,text="Find and Replace Word")
    #find_fram.pack(pady=20)


    history_Frame=Frame(history_popup,bd=4,relief=RIDGE,bg="crimson") 
    history_Frame.place(x=10,y=10,width=760,height=500)

    scroll_x=Scrollbar(history_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(history_Frame,orient=VERTICAL)
    history_table=ttk.Treeview(history_Frame,columns=("File Name","Path","Date","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=history_table.xview)
    scroll_y.config(command=history_table.yview)
    history_table.heading("File Name",text="File Name")
    history_table.heading("Path",text="Path")
    history_table.heading("Date",text="Date")
    history_table.heading("Time",text="Time")
    history_table['show']='headings'
    history_table.column("File Name",width=100)
    history_table.column("Path",width=300)
    history_table.column("Date",width=100)
    history_table.column("Time",width=100)
    history_table.pack(fill=BOTH,expand=1)
    
    con=sql.connect(host="localhost",user="root",password=passwd,database="text_editor")
    cur=con.cursor()
    cur.execute("select * from history")
    rows=cur.fetchall()
    for row in rows:
        history_table.insert('',END,values=row)
        con.commit()
    con.close()


history_btn.configure(command=historytable)

    

#status bar  --- word and character count

status_bars=ttk.Label(main_application,text="Status Bar")
status_bars.pack(side=tk.BOTTOM)

text_change=False

def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0,"end-1c").split())
        chararcter=len(text_editor.get(1.0,"end-1c".replace(" ","")))
        status_bars.config(text=f"character :{chararcter} word :{word}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change_word)



def change_theme(event=None):
    get_theme=theme_choose.get()
    colour_tuple=color_dict.get(get_theme)
    fg_color,bg_color=colour_tuple[0],colour_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icon[count],variable=theme_choose,compound=tk.LEFT,command=change_theme)
    count+=1


show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar=False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar=True


view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="Status Bar",onvalue=True,offvalue=0,variable=show_status_bar,image=status_bar,compound=tk.LEFT,command=hide_statusbar)

edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All",image=clear_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tk.END))

def find_fun(event=None):

    def find():
        
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match",foreground="red",background="blue")

    

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_popup=tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find Word")
    find_popup.resizable(0,0)

    #frame for find
    find_fram=ttk.LabelFrame(find_popup,text="Find and Replace Word")
    find_fram.pack(pady=20)

    #label
    text_find=ttk.Label(find_fram,text="Find")
    text_replace=ttk.Label(find_fram,text="Replace")

    #entry box
    find_input=ttk.Entry(find_fram,width=30)
    replace_input=ttk.Entry(find_fram,width=30)

    #button
    find_button=ttk.Button(find_fram,text="Find",command=find)
    replace_button=ttk.Button(find_fram,text="Replace",command=replace)

    #text label grid
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=0,padx=4,pady=4)
 
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_fun)


 
 #file menu

text_url=None

def new_file(event=None):
    global text_url
    text_url=None
    text_editor.delete(1.0,tk.END)
    main_application.title("Untitled - Text Editor")
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)

def open_file(event=None):
    global text_url
    
    text_url=filedialog.askopenfilename(defaultextension=os.getcwd(),title="select file",filetypes=[("All Files","*.*"),
                           ("Text Files","*.txt"),
                           ("Python Scripts","*.py"),
                           ("MArkdown Documents","*.md"),
                           ("JavaScripts Files","*.js"),
                           ("HTML Documents","*.html"),
                           ("CSS Documents","*.css)")])

    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))
    


file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)

def save_file(event=None):
    global text_url
    if text_url!=None:
        try:
            content=str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
                for_read.close()
            main_application.title(os.path.basename(text_url))
        except Exception as e:
            print(e)
            
    else:
        save_as_file()
        
    





file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)

def save_as_file(event=None):
    global text_url
    try:

        
        text_url=filedialog.asksaveasfilename(
                            defaultextension=".txt",
                            filetypes=[("All Files","*.*"),
                           ("Text Files","*.txt"),
                           ("Python Scripts","*.py"),
                           ("MArkdown Documents","*.md"),
                           ("JavaScripts Files","*.js"),
                           ("HTML Documents","*.html"),
                           ("CSS Documents","*.css)")],
                            initialfile="Untitled.txt" )
                            
        content=text_editor.get(1.0,tk.END)
        with open(text_url,"w") as f:
            f.write(content)
        x=os.path.basename(text_url)
        y=os.path.dirname(text_url)
        main_application.title(x)
        history(x,y)
        
        
     
    except:
        return



file.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Shift+S",command=save_as_file)

def Exit_fun(event=None):
    global text_url
    global text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content=text_editor.get(1.0,tk.END)
                    with open(text_url,"w",encoding="utf-8" )as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:

                    content2=text_editor.get(1.0,tk.END)
                    text_url=filedialog.asksaveasfile(defaultextension="txt",mode="w",filetypes=[("All Files","*.*"),
                           ("Text Files","*.txt"),
                           ("Python Scripts","*.py"),
                           ("MArkdown Documents","*.md"),
                           ("JavaScripts Files","*.js"),
                           ("HTML Documents","*.html"),
                           ("CSS Documents","*.css)")])
                    text_url.write(content2)
                    text_url.close()
                    x=os.path.basename(text_url)
                    y=os.path.dirname(text_url)
                    history(x,y)
                    main_application.destroy()

            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return




file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Alt+F4",command=Exit_fun)


text_editor.bind('<Control-n>',new_file)
text_editor.bind('<Control-o>',open_file)
text_editor.bind('<Control-s>',save_file)
text_editor.bind('<Control-S>',save_as_file)


main_application.config(menu=main_menu)



main_application.mainloop()



