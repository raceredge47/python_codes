from tkinter.ttk import *
import tkinter as tk
from tkinter import *
from tkinter import filedialog,simpledialog,messagebox,colorchooser,font
import os
root=tk.Tk()
root.title("Text Editor")
root.geometry("500x500+400+80")
Main_menu=tk.Menu()
#**************** ICONS **********************
New=tk.PhotoImage(file='icons/new.png')
Open=tk.PhotoImage(file='icons/open.png')
Save=tk.PhotoImage(file='icons/save.png')
Save_as=tk.PhotoImage(file='icons/save_as.png')
Exit=tk.PhotoImage(file='icons/exit.png')
Cut=tk.PhotoImage(file='icons/cut.png')
Copy=tk.PhotoImage(file='icons/copy.png')
Paste=tk.PhotoImage(file='icons/paste.png')
#**************** END **************************

#**************** Main Menu ********************
file_menu=tk.Menu(Main_menu, tearoff=0)
edit_menu=tk.Menu(Main_menu, tearoff=0)
view_menu=tk.Menu(Main_menu, tearoff=0)
theme_menu=tk.Menu(Main_menu, tearoff=0)
help_menu=tk.Menu(Main_menu, tearoff=0)
#**************** END **************************

#**************** Cascade Menu *****************
Main_menu.add_cascade(label='File', menu=file_menu)
Main_menu.add_cascade(label='Edit', menu=edit_menu)
Main_menu.add_cascade(label='View', menu=view_menu)
Main_menu.add_cascade(label='Color Theme', menu=theme_menu)
Main_menu.add_cascade(label='Help', menu=help_menu)
#**************** END **************************

#**************** Toolbar Menu ************************
toolbar=tk.Label(root, background='darkgray')
toolbar.pack(side=tk.TOP, fill=tk.X)

#Font Family
fontlist=tk.font.families()
fontbox=tk.ttk.Combobox(toolbar, width=30,  state='readonly')
fontbox['value']= fontlist
fontbox.current(fontlist.index('Arial'))
fontbox.grid(row=0, column=0, padx=10)

#Font Size
sizebox=tk.ttk.Combobox(toolbar, width=10, justify=tk.RIGHT)
sizebox['value']=tuple(range(8,202,2))
sizebox.current(4)
sizebox.grid(row=0, column=1, padx=2)

#Bold Button
Bold=tk.PhotoImage(file='icons/bold.png')
bold_button=Button(toolbar, image=Bold)
bold_button.grid(row=0, column=2)

#Underline Button
underline=PhotoImage(file='icons/underline.png')
underlinebutton=Button(toolbar, image=underline)
underlinebutton.grid(row=0, column=3)

#Italic Button
Italic=tk.PhotoImage(file='icons/italic.png')
italic_button=Button(toolbar, image=Italic)
italic_button.grid(row=0, column=4)

#Left Align Button
Left_align=tk.PhotoImage(file='icons/left.png')
leftbutton=Button(toolbar, image=Left_align)
leftbutton.grid(row=0, column=5)

#Center Align Button
Center_align=tk.PhotoImage(file='icons/center.png')
centerbutton=Button(toolbar, image=Center_align)
centerbutton.grid(row=0, column=6)

#Right Align Button
Right_align=tk.PhotoImage(file='icons/right.png')
rightbutton=Button(toolbar, image=Right_align)
rightbutton.grid(row=0, column=7)

#Font Color Button
fontcolor=tk.PhotoImage(file='icons/font_color.png')
color=Button(toolbar, image=fontcolor)
color.grid(row=0, column=8)

#Find Button
find=tk.PhotoImage(file='icons/find.png')
search=Button(toolbar, image=find)
search.grid(row=0, column=9)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& END &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#****************** Text Area *************************
editor=Text(root)
editor.config(wrap='word', relief=FLAT)
scrollbar=Scrollbar(root)
editor.focus_set()
scrollbar.pack(side=RIGHT, fill=Y )
editor.pack(fill=BOTH, expand=True)
scrollbar.config(command=editor.yview)
editor.config(font=('Arial', 14), yscrollcommand=scrollbar.set)

current_fontfamily='Arial'
current_fontsize=14
def fontfamily(event=None):
    global current_fontfamily
    current_fontfamily=fontbox.get()
    editor.config(font=(current_fontfamily, current_fontsize))
def font_size(event=None):
    global current_fontsize
    current_fontsize=int(sizebox.get())
    editor.config(font=(current_fontfamily, current_fontsize))
fontbox.bind("<<ComboboxSelected>>", fontfamily)
sizebox.bind("<<ComboboxSelected>>", font_size)
def bold(event=None):
    fontdata=font.Font(font=editor['font'])
    if fontdata.actual()['weight']=='normal':
        editor.config(font=(current_fontfamily, current_fontsize, 'bold'))
    else:
        editor.config(font=(current_fontfamily, current_fontsize, 'normal'))
bold_button.configure(command=bold)
def italic(event=None):
    fontdata = font.Font(font=editor['font'])
    if fontdata.actual()['slant']=='roman':
        editor.config(font=(current_fontfamily, current_fontsize, 'italic'))
    else:
        editor.config(font=(current_fontfamily, current_fontsize, 'normal'))
italic_button.configure(command=italic)
def under_line(event=None):
    fontdata=font.Font(font=editor['font'])
    if fontdata.actual()['underline']==0:
        editor.config(font=(current_fontfamily, current_fontsize, 'underline'))
    else:
        editor.config(font=(current_fontfamily, current_fontsize, 'normal'))
underlinebutton.configure(command=under_line)
def font_color(event=None):
    colorchsr=colorchooser.askcolor()
    editor.configure(fg=colorchsr[1])
color.configure(command=font_color)

def leftalign(event=None):
    content=editor.get(1.0, 'end')
    editor.tag_config('left', justify=tk.LEFT)
    editor.delete(1.0, tk.END)
    editor.insert(tk.INSERT, content, 'left')
leftbutton.configure(command=leftalign)

def centeralign(event=None):
    content=editor.get(1.0, 'end')
    editor.tag_config('center', justify=tk.CENTER)
    editor.delete(1.0, tk.END)
    editor.insert(tk.INSERT, content, 'center')
centerbutton.configure(command=centeralign)

def rightalign(event=None):
    content=editor.get(1.0, 'end')
    editor.tag_config('right', justify=tk.RIGHT)
    editor.delete(1.0, tk.END)
    editor.insert(tk.INSERT, content, 'right')
rightbutton.configure(command=rightalign)
#****************** End *******************************

#****************** Functionality *******************
filename=''
def newfile(event=None):
    global filename
    filename = ''
    editor.delete(1.0, END)
def openfile(event=None):
    global filename
    filename=filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
    with open(filename, 'r') as fileread:
        editor.delete(1.0, END)
        editor.insert(1.0, fileread.read())
    root.title(os.path.basename(filename))
def savefile(event=None):
    global filename
    if filename:
        content=str(editor.get(1.0, END))
        with open(filename, 'w', encoding='utf-8') as work:
            work.write(content)
    else:
        filename=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
        currentcontent=editor.get(1.0, END)
        filename.write(currentcontent)
        filename.close()

def saveasfile(event=None):
    global filename
    currentcontent=str(editor.get(1.0, END))
    filename=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
    filename.write(currentcontent)
    filename.close()
#**************** File Menu *****************
file_menu.add_command(label='New', image=New, compound=tk.LEFT, accelerator='Ctrl+N', command=newfile)
file_menu.add_command(label='Open', image=Open, compound=tk.LEFT, accelerator='Ctrl+O', command=openfile)
file_menu.add_command(label='Save', image=Save, compound=tk.LEFT, accelerator='Ctrl+S', command=savefile)
file_menu.add_command(label='Save As', image=Save_as, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=saveasfile)
file_menu.add_separator()
file_menu.add_command(label='Exit', image=Exit, compound=tk.LEFT, accelerator='Alt+F4')
#***************** END *********************

#****************** Edit Menu ******************
edit_menu.add_command(label='Undo', compound=tk.LEFT, accelerator='Ctrl+U')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', compound=tk.LEFT, image=Cut, accelerator='Ctrl+X', command=lambda: editor.event_generate('<Control x>'))
edit_menu.add_command(label='Copy', compound=tk.LEFT, image=Copy, accelerator='Ctrl+C', command=lambda: editor.event_generate('<Control c>'))
edit_menu.add_command(label='Paste', compound=tk.LEFT, image=Paste, accelerator='Ctrl+V', command=lambda: editor.event_generate('<Control v>'))
edit_menu.add_command(label='Delete', accelerator='Del', command=lambda : editor.delete(1.0, END))
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='F3')
edit_menu.add_command(label='Replace', accelerator='Ctrl+H')
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A')
#****************** END *********************

#****************** View Menu *****************
view_menu.add_command(label='Zoom')
view_menu.add_checkbutton(label='Toolbar', accelerator='Shift+T')
view_menu.add_checkbutton(label='Status bar', accelerator='Shift+B')
#****************** END ****8*******************

#****************** Theme Menu *****************
choice=tk.StringVar()
color_theme={'White':('#FFFFFF', '#000000'),
             'Dark' :('#2F4F4F', '#FFFFFF'),
             'Blue' :('#0000FF', '#000000')}
def colortheme(event=None):
    choose=choice.get()
    colors=color_theme.get(choose)
    bgcolor,fgcolor=colors[0], colors[1]
    editor.config(background=bgcolor, fg=fgcolor)
for i in color_theme:
    theme_menu.add_radiobutton(label= i, variable=choice, command=colortheme)
#****************** END **********************

#****************** Help Menu *****************
help_menu.add_command(label='About')
help_menu.add_command(label='Contact Us')
help_menu.add_command(label='Site')
#****************** END ***********************

root.config(menu=Main_menu)
root.bind("<Control-n>", newfile)
root.bind("<Control-s>", savefile)

root.mainloop()