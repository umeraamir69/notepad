from tkinter import *
import os
import time
from tkinter import messagebox, colorchooser, font 
from tkinter import ttk , filedialog , font
# from PIL import Image , ImageFile


root = Tk()
root.geometry("1284x1000")
root.title("Text Editor")


 # ------------------------------------images-------------------------------- #
img_new = PhotoImage(file="new.png")
img_open = PhotoImage(file="open.png")
img_cut = PhotoImage(file="cut.png")
img_exit = PhotoImage(file="exit.png")
img_paste = PhotoImage(file="paste.png")
img_save = PhotoImage(file="save.png")
img_save_as = PhotoImage(file="save_as.png")
img_copy = PhotoImage(file= "copy.png")
img_clear_all = PhotoImage(file= "clear_all.png")
img_find = PhotoImage(file= "find.png")
img_status_bar = PhotoImage(file= "status_bar.png")
img_tool_bar = PhotoImage(file= "tool_bar.png")
img_Dark = PhotoImage(file= "dark.png")
img_Light_Default = PhotoImage(file= "light_default.png")
img_Light_Plus = PhotoImage(file= "light_plus.png")
img_Monokai = PhotoImage(file= "monokai.png")
img_Red = PhotoImage(file= "red.png")
img_Night_Blue = PhotoImage(file= "night_blue.png")
img_bold = PhotoImage(file= "bold.png")
img_italic = PhotoImage(file= "italic.png")
img_underline = PhotoImage(file= "underline.png")
img_align_left = PhotoImage(file= "align_left.png")
img_align_center = PhotoImage(file= "align_center.png")
img_align_right = PhotoImage(file= "align_right.png")
img_font_color = PhotoImage(file= "font_color.png")
# img_ = PhotoImage(file= ".png")


# # -----------------------------------DATA-------------------------------- #
color_theme_names = ("Light_Default" , "Dark" , "Light_Plus" , "Night_Blue" , "Red" ,"Monoaki")
color_theme_valeus = {
    "Light Default": ("#000000" ,"#ffffff") ,
    "Dark" : ("#ffffff" ,"#000000"),
    "Light Plus" : ("#000000" ,"#97d6db"),
    "Night Blue" : ("#0b9fb9" ,"#ffffff"),
    "Red" : ("#c8dfcd" ,"#e06363"), 
    "Monokai" : ("#e42961" ,"#dbf2f1")
}

Label(root , text = "__Xh.Someone_69__" , font = ("" , 14 )).pack()

# ________________________________Text Editor Scrooll Bar____________________________  #
scrol_bar_text = Scrollbar(root, orient = VERTICAL)
scrol_bar_text.pack(side=RIGHT , fill = Y)

text = Text(root)
text.config(wrap = WORD , relief = SOLID , yscrollcommand = scrol_bar_text.set)

# __________________________________Variabels________________________________________ #
font_var = tuple(font.families())
var_color_theme = StringVar()
var_font = StringVar()
var_font_size = IntVar()
current_font = "Arial"
current_font_size = 12
var_statusbar = BooleanVar()
var_toolbar = BooleanVar()
var_statusbar.set(True)
var_toolbar.set(True)
data = ''
url = ""
# # ----------------------------------Functions----------------------------

def fn_font(event = None):
    dict_font = font.Font(font=text['font']).actual()
    global current_font 
    if dict_font['weight'] == 'normal':
        is_bold = ""
    else :
        is_bold = "bold"
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['slant'] == 'roman':
        is_italic = ""
    else :
        is_italic = "italic"
    if dict_font['underline'] == 0:
        is_underline = ""
    else :
        is_underline = "underline"
    biu = is_bold+" "+is_italic+" "+is_underline
    current_font = var_font.get()
    text.configure(font=(current_font , current_font_size , biu))

def fn_font_size(event= None):
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['weight'] == 'normal':
        is_bold = ""
    else :
        is_bold = "bold"
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['slant'] == 'roman':
        is_italic = ""
    else :
        is_italic = "italic"
    if dict_font['underline'] == 0:
        is_underline = ""
    else :
        is_underline = "underline"
    biu = is_bold+" "+is_italic+" "+is_underline
    global current_font_size
    current_font_size = var_font_size.get()
    text.configure(font=(current_font , current_font_size , biu))

def fn_bold():
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['slant'] == 'roman':
        is_italic = ""
    else :
        is_italic = "italic"

    if dict_font['underline'] == 0:
        is_underline = ""
    else :
        is_underline = "underline"

    if dict_font['weight'] == "normal":
        bi = 'bold' +" "+is_italic+" "+is_underline
        text.configure(font=(current_font , current_font_size , bi ))
    elif dict_font['weight'] == "bold":
        bi = is_italic+" "+is_underline
        text.configure(font=(current_font , current_font_size , bi ))
      


def fn_underline():
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['weight'] == 'normal':
        is_bold = ""
    else :
        is_bold = "bold"

    if dict_font['slant'] ==" roman":
        is_italic = ""
    else :
        is_italic = "italic"

    if dict_font['underline'] == 0:
        bi = is_bold +" "+is_italic+" "+"underline"
        text.configure(font=(current_font , current_font_size , bi ))
    elif dict_font['underline'] == 1:
        bi = is_bold+" "+is_italic
        text.configure(font=(current_font , current_font_size , bi ))



def fn_italic():
    dict_font = font.Font(font=text['font']).actual()
    if dict_font['weight'] == 'normal':
        is_bold = ""
    else :
        is_bold = "bold"

    if dict_font['underline'] == 0:
        is_underline = ""
    else :
        is_underline = "underline"

    if dict_font['slant'] == "roman":
        bi = is_bold +" "+"italic"+" "+is_underline
        text.configure(font=(current_font , current_font_size , bi ))
    elif dict_font['slant'] == "italic":
        bi = is_bold+" "+is_underline
        text.configure(font=(current_font , current_font_size , bi ))

def fn_text_color():
    color_var = colorchooser.askcolor()
    text.configure(fg = color_var[-1])

def fn_allign_left():
    text_allign_left = text.get(1.0 ,'end')
    text.tag_config('left' , justify = LEFT)
    fn_prg_in()
    text.delete(1.0 , END)
    text.insert(END , text_allign_left , 'left')
    text.delete("end-1c")

def fn_allign_center():
    text_allign_center = text.get(1.0 ,'end')
    text.tag_config('center' , justify = CENTER)
    fn_prg_in()
    text.delete(1.0 , END)
    text.insert(END , text_allign_center , 'center')
    text.delete("end-1c")

def fn_allign_right():
    text_allign_right = text.get(1.0 ,'end')
    text.tag_config('right' , justify = RIGHT)
    fn_prg_in()
    text.delete(1.0 , END)
    text.insert(END , text_allign_right , 'right')
    text.delete("end-1c")

def fn_word_counter(event=None):
    if text.edit_modified():
        words = len(text.get(1.0 , "end-1c").split(" "))
        charchs = len(text.get(1.0 , "end-1c"))
        frm_words.configure(text =f"Charchters : {charchs} , Words : {words}")
    text.edit_modified(False)


def fn_new_file():
    global url
    content = ""
    content = str(text.get(1.0 , 'end-1c'))
    if content:
        if url == "":
            a = messagebox.askquestion("||  Saving  ? ||" , "Do yow Want to Save?")
            if a == "no":
                fn_prg_in()
                text.delete(1.0 , END)
                content = ""
                url = ""
            elif a == "yes":
                content1 = str(text.get(1.0 , 'end-1c'))
                url = filedialog.asksaveasfile(mode= "w" ,defaultextension = '.txt' ,filetypes = (("Text Files" , "*.txt") , ("All types" , "*.*")))
                fn_prg_in()
                url.write(content1)
                url.close
                text.delete(1.0 , END)
                content = ""
                content1 = ""
                url = ""
        else:
            try:
                content2 = str(text.get(1.0 , END))
                with open (url.name , "w" , encoding='utf-8') as fr:
                    fr.write(content2)
            except Exception as e:
                messagebox.showwarning(f"The Data is not Saved . Saved it Maunally\nError = {e}")
            else:
                fn_prg_in()
                text.delete(1.0 , END)
                content2 = ""
                content = ""
                text.delete(1.0 , END)
                url = ""
    else:
        url = ''
        fn_prg_in()
        text.delete(1.0 , END)



def fn_open(event=None):
    global url , data
    data = ""
    data = text.get(1.0 , "end-1c")
    if data:
        if url =="":
            ab = messagebox.askquestion("Document not saved" , "The data is'nt saved. Do yow Want to Save?")
            if ab == "yes":
                url = filedialog.asksaveasfile(mode= "w" ,defaultextension = '.txt' ,filetypes = (("Text Files" , "*.txt") , ("All types" , "*.*")))
                url.write(data)
                fn_prg_in()
                url.close() 
                url = ""
                data = ""
                url = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select File To Open" , filetypes = (("Text files" , "*.txt"),("CSV files" , "*.csv"),
                ("Python" , "*.py"),("All Files" , "*.*")))
                try:
                    with open(url , "r") as fr:
                        text.delete(1.0 , END)
                        root.title(os.path.basename(url))
                        fn_prg_in()
                        text.insert(1.0 , fr.read())
                except FileNotFoundError:
                    messagebox.showerror("file not found" , "The file you want to open is'nt found!!")
                except:
                    messagebox.showerror("Error" , "error in opening File.")
            elif ab == "no":
                url = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select File To Open" , filetypes = (("Text files" , "*.txt"),("CSV files" , "*.csv"),
                ("Python" , "*.py"),("All Files" , "*.*")))
                try:
                    with open(url , "r") as fr:
                        text.delete(1.0 , END)
                        fn_prg_in()
                        root.title(os.path.basename(url))
                        text.insert(1.0 , fr.read())
                except FileNotFoundError:
                    messagebox.showerror("file not found" , "The file you want to open is'nt found!!")
                except:
                    messagebox.showerror("Error" , "error in opening File.")
        else:
            try:
                contnet = str(text.get(1.0 , END))
                with open(url.name , "w" , encoding="utf-8") as fw:
                    fw.write(contnet)
                    url = ""
            except:
                messagebox.showwarning("Document not saved!" , "The document is'nt saved, kindly saved it automatically||!||")
            finally:
                url = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select File" , filetypes = (("Text files" , "*.txt"),("CSV files" , "*.csv"),
                ("Python" , "*.py"),("All Files" , "*.*")))
                try:
                    with open(url , "r") as fr:
                        fn_prg_in()
                        text.delete(1.0 , END)
                        root.title(os.path.basename(url))
                        text.insert(1.0 , fr.read())
                except FileNotFoundError:
                        messagebox.showerror("file not found" , "The file you want to open is'nt found!!")
                except:
                    messagebox.showerror("Error" , "error in opening File.")
    else:
        url = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select File" , filetypes = (("Text files" , "*.txt"),("CSV files" , "*.csv"),
        ("Python" , "*.py"),("All Files" , "*.*")))
        try:
            with open(url , "r") as fr:
                fn_prg_in()
                text.delete(1.0 , END)
                root.title(os.path.basename(url))
                text.insert(1.0 , fr.read())
        except FileNotFoundError:
            messagebox.showerror("file not found" , "The file you want to open is'nt found!!")
        except:
            messagebox.showerror("Error" , "error in opening File.")
            


def fn_save(event=None):
    global url
    try:
        if url:
            counter = str(text.get(1.0 , 'end-1c'))
            with open (url.name , "w") as fw:
                fn_prg_in()
                fw.write(counter)
                root.title(os.path.basename(url))
        else:
            counter2 = str(text.get(1.0 , 'end-1c'))
            url = filedialog.asksaveasfile(mode= "w" ,defaultextension = '.txt' ,filetypes = (("Text Files" , "*.txt") , ("All types" , "*.*")))
            fn_prg_in()
            url.write(counter2)
            url.close()
    except Exception as a:
        messagebox.showerror("Not saved" , f"The data is'nt saved\n{a}")


def fn_save_as():
    global url
    try:
        url = filedialog.asksaveasfile(mode= "w"  ,filetypes = (("Text Files" , "*.txt") , ("All types" , "*.*")))
        content = str(text.get(1.0 , 'end-1c'))
        fn_prg_in()
        url.write(content)
        url.close
    except :
        messagebox.showerror("Error" , "something went wrong!!")

def fn_exit():
    global url
    try:
        if url == "":
            data = str(text.get(1.0 , "end-1c"))
            if data :
                abc = messagebox.askquestion("Exit Withouth Saving" , "Do you want to save the document?||!||")
                if abc == "yes":
                    url = filedialog.asksaveasfile(mode= "w" , defaultextension ="*.txt" ,filetypes = (("Text Files" , "*.txt") , ("All types" , "*.*")))
                    content = str(text.get(1.0 , 'end-1c'))
                    url.write(content)
                    url.close
        else :
            with open (url.name , "w" , encoding= "utf-8") as fww:
                fww.write(text.get(1.0 ,END))
    except Exception as e:
        messagebox.showerror("error" , f"File not saved \n{e}")
    else:
        messagebox.showinfo("Thank" , "Thanks for using __Xh.Someone . I hope you Like This......")
    finally:
        fn_prg_dn()
        root.destroy()

def fn_find_replace(event=None):

    def fn_find():
        fn_prg_in()
        word = find_input.get()
        text.tag_remove('match', '1.0', END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config('match', foreground='red', background='yellow')
    
    def fn_replace():
        fn_prg_in()
        word = find_input.get()
        replace_text = replace_input.get()
        content = text.get(1.0, END)
        new_content = content.replace(word, replace_text)
        text.delete(1.0, END)
        text.insert(1.0, new_content)

    find_dialogue = Toplevel()
    find_dialogue.geometry('350x150+500+200')
    find_dialogue.title('Find & Replace')
    find_dialogue.resizable(0,0)


    find_frame = ttk.LabelFrame(find_dialogue, text='Find & Replace:')
    find_frame.pack(pady=20)


    text_find_label = Label(find_frame, text='Find : ')
    text_replace_label = Label(find_frame, text= 'Replace')
    find_input = Entry(find_frame, width=30)
    replace_input = Entry(find_frame, width=30)

    find_input.focus_set()

    find_button = Button(find_frame, text='Find', command=fn_find)
    replace_button = Button(find_frame, text= 'Replace', command=fn_replace)


    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

def fn_hide_toolbar(event=None):
    global var_toolbar
    if var_toolbar:
        fn_prg_in()
        frm_tool_bar.pack_forget()
        var_toolbar = False
    else:
        fn_prg_dn()
        text.pack_forget()
        frm_tool_bar.pack(fill = X)
        text.pack(fill = BOTH , expand = TRUE)
        var_toolbar = True

def fn_hide_statusbar(event=None):
    global var_statusbar
    if var_statusbar:
        fn_prg_in()
        frm_end.pack_forget()
        var_statusbar = False
    else:
        fn_prg_dn()
        frm_end.pack(side = BOTTOM , fill =X)
        var_statusbar = True

def fn_colour_theme ():
    val = color_theme_valeus.get((var_color_theme.get()))
    fn_prg_in()
    text.configure(bg = val[0] , fg = val[1] )

def fn_help():
    fn_prg_in()
    messagebox.showinfo("Help" ,"This is simple software So no help avalible for more help visit \"www.google.com/help\"")

def fn_about():
    fn_prg_in()
    messagebox.showinfo("About Us" , "This Software Is made bt Umer Aamir\ncontact : 0335-9119222\nEmail : xh.someone69@gmail.com")

def fn_prg_in():
    for i in range (1,100 , 18):
        prg['value'] = i
        prg.update()
        time.sleep(0.0045)
    prg['value'] = 0
    prg.update() 

def fn_prg_dn():
    for i in range (100,1 , -18):
        prg['value'] = i
        prg.update()
        time.sleep(0.0001)
    prg['value'] = 0
    prg.update()
# ========================================Frames======================================== #
frm_end = Label(root)
frm_tool_bar = Label(root , bg = "#bcdce0")
frm_words = Label(frm_end , bg = "gray")

frm_end.pack(side = BOTTOM , fill = X)
frm_words.pack(side = LEFT)
frm_tool_bar.pack(fill = X  )

text.pack(fill = BOTH , expand = TRUE)
# # =========================================Menu_Bar===================================== #
mn = Menu(root , borderwidth = 20)
m1 = Menu(mn , tearoff = FALSE)
m1.add_command(label = "New File" , command = fn_new_file ,image = img_new , compound = LEFT , accelerator = "Ctrl + N")
m1.add_command(label = "Open" , command = fn_open ,image = img_open , compound = LEFT , accelerator = "Ctrl + O")
m1.add_separator()
m1.add_command(label = "Save" , command = fn_save ,image = img_save , compound = LEFT , accelerator = "Ctrl + S")
m1.add_command(label = "Save As" , command = fn_save_as ,image = img_save_as , compound = LEFT , accelerator = "Ctrl + Alt + S")
m1.add_separator()
m1.add_command(label = "Exit" , command = fn_exit ,image = img_exit , compound = LEFT , accelerator = "Alt + F4")
mn.add_cascade(label = "File" , menu = m1 )
m2 = Menu(mn , tearoff= False)
m2.add_command(label = "Cut" , image = img_cut , compound = LEFT , accelerator = "Ctrl + X" , command = lambda:text.event_generate('<Control x>'))
m2.add_command(label = "Copy" , image = img_copy , compound = LEFT , accelerator = "Ctrl + C" , command = lambda:text.event_generate('<Control c>')) 
m2.add_command(label = "Paste" , image = img_paste , compound = LEFT , accelerator = "Ctrl + V" , command = lambda:text.event_generate('<Control v>')) 
m2.add_command(label = "Clear all" , image = img_clear_all, compound = LEFT , accelerator = "Ctrl + Alt + C" , command = lambda:text.delete(1.0 , END))
m2.add_command(label = "Find" , image = img_find , compound = LEFT , accelerator = "Ctrl + F" , command = fn_find_replace)
mn.add_cascade(label = "Edit" , menu = m2)
m3 = Menu(mn , tearoff= FALSE)
m3.add_checkbutton(label = "Status Bar" , command = fn_hide_statusbar , offvalue = False, onvalue = True , variable = var_statusbar ,image = img_status_bar , compound = LEFT)
m3.add_checkbutton(label = "Tool Bar" , command = fn_hide_toolbar , offvalue = False, onvalue = True , variable = var_toolbar ,image = img_tool_bar , compound = LEFT)
# m3.add_checkbutton(label = "Side Bar" , image = img_tool_bar , compound = LEFT , command = "pass")
mn.add_cascade(label = "View" , menu = m3)
m4 = Menu(mn , tearoff = False)
m4.add_radiobutton(label = "Light Default" ,  image = img_Light_Default , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
m4.add_radiobutton(label = "Light Plus" ,  image = img_Light_Plus , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
m4.add_radiobutton(label = "Dark" ,  image = img_Dark , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
m4.add_radiobutton(label = "Red" ,  image = img_Red , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
m4.add_radiobutton(label = "Monokai" ,  image = img_Monokai , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
m4.add_radiobutton(label = "Night Blue" ,  image = img_Night_Blue , compound = LEFT , variable = var_color_theme , command = fn_colour_theme)
mn.add_cascade(label = "Color Theme" , menu = m4)
m5 = Menu(mn , tearoff = False)
m5.add_command(label = "Help" , command = fn_help)
m5.add_command(label = "About Us" , command = fn_about)
mn.add_cascade(label = "Help" , menu = m5)
# ==========================================Tool_Bar==================================== #
combo_font = ttk.Combobox(frm_tool_bar , state = "readonly" , textvariable = var_font , width = 30)
combo_font_size = ttk.Combobox(frm_tool_bar ,state  = "readonly" , textvariable = var_font_size , width = 10)
bt_font_color = Button(frm_tool_bar , image = img_font_color , command = fn_text_color)
bt_bold = Button(frm_tool_bar , image = img_bold , command = fn_bold)
bt_italic = Button(frm_tool_bar, image = img_italic , command = fn_italic)
bt_underline = Button(frm_tool_bar, image = img_underline , command = fn_underline)
bt_allign_left = Button(frm_tool_bar , image = img_align_left , command  = fn_allign_left)
bt_allign_center = Button(frm_tool_bar , image = img_align_center , command = fn_allign_center)
bt_allign_right = Button(frm_tool_bar , image = img_align_right , command = fn_allign_right)

combo_font.pack(side  = LEFT , padx = 1)
combo_font_size.pack(side  = LEFT , padx = 1)
bt_font_color.pack(side = LEFT, padx = 1)
bt_bold.pack(side  = LEFT , padx = 3)
bt_italic.pack(side  = LEFT , padx = 3)
bt_underline.pack(side  = LEFT , padx = 3)
bt_allign_left.pack(side  = LEFT , padx = 5)
bt_allign_center.pack(side  = LEFT , padx = 5)
bt_allign_right.pack(side = LEFT , padx = 5)

combo_font['values'] = font_var
combo_font.current(font_var.index('Arial'))
combo_font_size['values'] = tuple(range(8,100,2))
combo_font_size.current(1)
# -------------------------------------------Status_Bar---------------------------------- #
prg = ttk.Progressbar(frm_end ,orient = HORIZONTAL, length = 650 , mode = "determinate" )
prg.pack(side = RIGHT)
# ___________________________________________bind_______________________________________ #
combo_font.bind('<<ComboboxSelected>>' , fn_font)
combo_font_size.bind('<<ComboboxSelected>>' , fn_font_size)
text.bind('<<Modified>>' , fn_word_counter)
# ____________________ End Of Appplication & Configrations___________
root.bind("<Control-o>", fn_open)
root.bind("<Control-n>", fn_new_file)
root.bind("<Control-s>", fn_save)
root.bind("<Control-Alt-s>", fn_save_as)
root.bind("<Control-q>", fn_exit)
root.bind("<Control-f>", fn_find_replace)
root.bind("<Control-r>", fn_find_replace)

text.config(font = (current_font , current_font_size))
scrol_bar_text.config(command=text.yview)
root.config(menu=mn)
root.mainloop()