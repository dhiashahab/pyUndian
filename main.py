import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from random import randint

# Root window
root = tk.Tk()
root.title('Undian Doorprize')
root.resizable(1, 0)
root.geometry('600x455')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

label1 = ttk.Label(root, text="Daftar Peserta Undian:")
label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

label2 = ttk.Label(root, text="Peserta Yang Beruntung:")
label2.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)


# membuat scrolled text editor untuk daftar peserta undian
textContainer1 = tk.Frame(root, borderwidth=1, relief="sunken")
textContainer1.grid_rowconfigure(0, weight=1)
textContainer1.grid_columnconfigure(0, weight=1)

text_peserta = tk.Text(textContainer1, height=22, wrap="none", borderwidth=0)
textVsb1 = tk.Scrollbar(textContainer1, orient="vertical", command=text_peserta.yview)
textHsb1 = tk.Scrollbar(textContainer1, orient="horizontal", command=text_peserta.xview)
text_peserta.configure(yscrollcommand=textVsb1.set, xscrollcommand=textHsb1.set)

text_peserta.grid(row=0, column=0, sticky="nsew")
textVsb1.grid(row=0, column=1, sticky="ns")
textHsb1.grid(row=1, column=0, sticky="ew")

textContainer1.grid(column=0, row=1, sticky="ew", padx=5, pady=5)


# membuat scrolled text editor untuk daftar yang dapat undian
textContainer2 = tk.Frame(root, borderwidth=1, relief="sunken")
textContainer2.grid_rowconfigure(0, weight=1)
textContainer2.grid_columnconfigure(0, weight=1)

text_dapatdoorprize = tk.Text(textContainer2, height=22, wrap="none", borderwidth=0)

textVsb2 = tk.Scrollbar(textContainer2, orient="vertical", command=text_dapatdoorprize.yview)
textHsb2 = tk.Scrollbar(textContainer2, orient="horizontal", command=text_dapatdoorprize.xview)
text_dapatdoorprize.configure(yscrollcommand=textVsb2.set, xscrollcommand=textHsb2.set)

text_dapatdoorprize.grid(row=0, column=0, sticky="nsew")
textVsb2.grid(row=0, column=1, sticky="ns")
textHsb2.grid(row=1, column=0, sticky="ew")

textContainer2.grid(column=1, row=1, sticky="ew", padx=5, pady=5)


# fungsi untuk menampilkan dialog open, lalu membuka file tsb
def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    filename = fd.askopenfilename(filetypes=filetypes)
    # read the text file and show its content on the Text
    try:
        f = open(filename)
        file_cont = f.read()
        f.close()
        text_peserta.delete('1.0', 'end')
        text_peserta.insert('end',file_cont)

    except UnicodeDecodeError:
        messagebox.showinfo('Perhatian !!!', 'File ' + filename + ' tidak dapat dibuka.\nSilahkan untuk menggunakan file text (.txt).')


# fungsi untuk menampilkan dialog save, lalu membuka file tsb
def save_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the save as file dialog
    filename = fd.asksaveasfilename(filetypes=filetypes, defaultextension='.txt')
    if not filename: return
    f = open(filename, 'w')
    f.write(text_dapatdoorprize.get('1.0', 'end-1c'))
    f.close()
    tk.messagebox.showinfo('Informasi', 'Hasil Undian tersimpan di ' + filename)


# fungsi untuk mengambil salah satu nama dari daftar peserta secara acak
def undian():
    total_lines = int(text_peserta.index('end-1c').split('.')[0])  
    rand_line = randint(1,total_lines)
    start_index = str(rand_line) + '.0'
    end_index = str(rand_line) + '.end'
    dapat_undian = text_peserta.get(start_index , end_index )
    if dapat_undian != '':
      #print(dapat_undian)
      tk.messagebox.showinfo('Informasi', 'Selamat untuk:\n' + dapat_undian)
      text_dapatdoorprize.insert('end', dapat_undian + '\n')  
  
    #hapus namanya dari daftar, supaya tidak dapat undian dua kali
    text_peserta.delete(start_index , end_index + '+1c')

# fungsi untuk menampilkan pilihan sebelum keluar
def on_closing():
    if messagebox.askokcancel("Keluar", "Yakin mau keluar sekarang?"):
        root.destroy()


# membuat open file button
open_button = ttk.Button(
    root,
    text='Buka File',
    command=open_text_file
)
open_button.grid(column=0, row=2, sticky=tk.E, padx=10, pady=10)

# membuat undi button
undi_button = ttk.Button(
    root,
    text='Undi 1 Nama',
    command=undian
)
undi_button.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10)

# membuat save file button
save_button = ttk.Button(
    root,
    text='Simpan File',
    command=save_text_file
)
save_button.grid(column=1, row=2, sticky=tk.E, padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
