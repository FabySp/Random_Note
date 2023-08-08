from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Function for Theme
def change_theme(theme):
    text_field['bg'] = view_colours[theme]['text_bg']
    text_field['fg'] = view_colours[theme]['text_fg']
    text_field['insertbackground'] = view_colours[theme]['cursor']
    text_field['selectbackground'] = view_colours[theme]['select_bg']

# Function for Fonts
def change_fonts(font_user):
    text_field['font'] = fonts[font_user]['font']

# Finction for 'Close'
def notepad_exit():
    answer = messagebox.askokcancel('Exit', 'Are you sure you want to exit?')
    if answer:
        root.destroy()

# Function for 'Open'
def open_file():
    file_path = filedialog.askopenfilename(title='File selection', 
                                           filetypes=('Text documents (*.txt)', 
                                                      '*.txt',
                                                      ('All files','*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())

# Function for 'Save'
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text documents (*.txt)',
                                                         '*.txt'),
                                                         ('All documents','*.*')))
    f = open(file_path, 'w', encoding = 'utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()

# Set the nonebook window
root = Tk()
root.title("Random Notes")
root.geometry('400x400')
#root.iconbitmap() #icon for the notebook

# Create a Menu
main_menu = Menu(root)

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label = 'Open', command = open_file)
file_menu.add_command(label = 'Save', command = save_file)
file_menu.add_separator() # line for separation
file_menu.add_command(label='Close', command = notepad_exit)
root.config(menu = file_menu)

# View
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Dark', command=lambda:change_theme('dark'))
view_menu_sub.add_command(label='Light', command=lambda:change_theme('light'))
view_menu.add_cascade(label = 'Theme', menu = view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda:change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda:change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda:change_fonts('TNR'))
view_menu.add_cascade(label='Font...', menu=font_menu_sub)
root.config(menu=view_menu)

# Add menu list
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill = BOTH, expand = 1)

# Themes
view_colours = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor':'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor':'#A5A5A5', 'select_bg':'#FAEEDD'
    }
}

# Fonts
fonts = {
    'Arial':{
        'font':'Arial 14 bold'
    },
    'CSMS':{
        'font':('Comic Sans MS', 14, 'bold')
    },
    'TNR':{
        'font':('Times New Roman', 14, 'bold')
    }
}

text_field = Text(f_text,
                  bg = 'black',  fg = 'lime',
                  padx = 10,
                  pady = 10,
                  wrap = WORD,
                  insertbackground = 'brown',
                  selectbackground='#80917A',
                  spacing3=10,
                  width=30,
                  font = 'Arial 14 bold'
                  )
text_field.pack(expand=1, fill=BOTH, side=LEFT)

# Add scrollbar on the left side
scroll=Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)

text_field.config(yscrollcommand=scroll.set)

root.mainloop()
