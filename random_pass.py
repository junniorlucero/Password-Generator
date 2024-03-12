import tkinter as tk
import tkinter.ttk as ttk
import random
import string


special_characters = ['!','@','#','$','%','^','&',
                      '*','(',')','-','_','=','+','[',']','{',
                      '}','|',';',':',
                      "'",'"',',','.','<','>','?','/']
def random_pass():
    user_input = 0
    try:
        user_input = int(entry.get())
    except ValueError:
        label = tk.Label(text = "Oops!  That was not a valid number.  Try again...",
                          foreground = 'red',
                          background = 'black',
                          font=('Helvetica',16, 'bold'))
        label.pack()
    out = ''
    while len(out) < user_input:
        choice = random.choice(['digit', 'letter', 'special'])
        if choice == 'digit':
            out += (str(random.randint(0, 9)))
        elif choice == 'letter':
            out += random.choice(string.ascii_letters)
        elif choice == 'special':
            out += random.choice(special_characters)

    label = tk.Label(
    text = out,
    foreground = '#00FF00',
    background = 'black',
    font=('Helvetica', 16, 'bold')
)
    label.pack()
    
window = tk.Tk(
    
)
window.title("Random Password Generator")
window.geometry('450x250')
window.configure(bg = 'black')



lbl_entry = tk.Label(text = "Enter your desired password length", font=('Helvetica', 24, 'bold'), fg = 'white', bg = 'black')
entry = tk.Entry(window, width = 5, relief=tk.SUNKEN)
lbl_entry.pack(pady=10)
entry.pack()



button = ttk.Button(window, text="Generate Password", command=random_pass)
button.pack(pady=5)



window.mainloop()