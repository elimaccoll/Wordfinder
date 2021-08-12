import tkinter as tk
from typing import List

from wordfinder_gui_backend import *

recent_words = []
width = 700
height = width
bg_color = "lightgray"
gui = tk.Tk()
gui.geometry(f"{str(width)}x{str(height)}")

# Dictionary select
dict_name = tk.StringVar()

dict_sel_states = ["No Dictionary Selected"]
for i in range(getNumDictionaries()):
    dict_sel_states.append(getDictionaryLabels()[i])
dict_name.set(dict_sel_states[0])  # Default state

btn_text = tk.StringVar()
btn_text.set("Select Dictionary")


def isChecked():
    dict_sel = cb.get()
    if dict_sel != 0:
        btn['state'] = tk.NORMAL
        btn_text.set("Find Words!")
    else:  # No Dictionary Selected
        btn['state'] = tk.DISABLED
        btn_text.set("Select Dictionary")
    dict_name.set(f"{dict_sel_states[dict_sel]} Selected")


cb = tk.IntVar()
dict_cbs = []
y_pos = 0


def incY(y, val):
    y += val
    return y


x_pos = width / 2 - 60
space = 20
y_pos = incY(y_pos, space)
# Label to enter characters
letter_label = tk.Label(gui, font=("Arial", 12), text="Enter your characters", bg=bg_color)
letter_label.place(x=width / 2, y=y_pos, anchor="center")
# Entry box for characters
y_pos = incY(y_pos, 2 * space)
letter_entry = tk.Entry(gui, bd=5)
letter_entry.place(x=width / 2, y=y_pos, anchor="center")
# Label to select dictionary
y_pos = incY(y_pos, 2 * space)
letter_label = tk.Label(gui, font=("Arial", 12), text="Select a Dictionary", bg=bg_color)
letter_label.place(x=width / 2, y=y_pos, anchor="center")

# Checkboxes
y_pos = incY(y_pos, 1.5 * space)
for i in range(getNumDictionaries()):
    dict_cb = tk.Checkbutton(gui, text=getDictionaryLabels()[i], variable=cb, onvalue=i + 1, offvalue=0,
                             command=isChecked).place(x=x_pos, y=y_pos, anchor="w")
    y_pos = incY(y_pos, space)
    dict_cbs.append(dict_cb)

words = tk.StringVar()
words.set("Try searching for words!")


def convertWordsToString(words_to_string):
    words_str = ""
    for x in range(len(words_to_string)):
        words_str += words_to_string[x]
        if x != len(words_to_string) - 1:
            words_str += ", "
            # 25 words per line when printed in terminal
            if x % 25 == 0 and x != 0:
                words_str += "\n"
    return words_str


def getWords():
    word_list = backend(user_letters=letter_entry.get(), dict_num=cb.get())
    word_list_str = convertWordsToString(word_list)
    if not word_list_str:
        words.set("No words found")
        text_file_btn['state'] = tk.DISABLED
    else:
        words.set(word_list_str)
        text_file_btn['state'] = tk.NORMAL
        setFoundWords(word_list)


def setFoundWords(word_list):
    global recent_words
    recent_words = word_list


# Label for name of dictionary selected
y_pos = incY(y_pos, 0.75 * space)
dict_selected = tk.Label(gui, font=("Arial", 12), bg=bg_color, textvariable=dict_name).place(x=width / 2, y=y_pos,
                                                                                             anchor="center")
# Button to find words (disabled when dictionary not selected)
y_pos = incY(y_pos, 1.5 * space)
btn = tk.Button(gui, textvariable=btn_text, state=tk.DISABLED, padx=20, pady=5, command=getWords)
btn.pack()
btn.place(x=x_pos, y=y_pos)

# Label to show words below
y_pos = incY(y_pos, 3 * space)
words_out_label = tk.Label(gui, font=("Arial", 12), bg=bg_color, text="Words from Last Search").place(x=width / 2,
                                                                                                      y=y_pos,
                                                                                                      anchor="center")
# Label to display list of words
y_pos = incY(y_pos, 2 * space)
words_out = tk.Label(gui, font=("Arial", 12), bg=bg_color, textvariable=words).place(x=width / 2, y=y_pos,
                                                                                     anchor="center")
# Label asking to write to text file
y_pos = incY(y_pos, 3 * space)
text_out_label = tk.Label(gui, font=("Arial", 12), bg=bg_color,
                          text="Create text file of found words?\n This will overwrite a previous text file")
text_out_label.place(x=width / 2, y=y_pos, anchor="center")

text_status = tk.StringVar()
text_status.set("")


def writeTextFile():
    if getWords() != 0:
        printToTextFile(recent_words)
        text_status.set("Text file 'wordfinder.txt' was created!")
    else:
        text_status.set("No words found to create text file")


# Button to write text file
y_pos = incY(y_pos, 2 * space)
text_file_btn = tk.Button(gui, text="Write to text file", state=tk.DISABLED, padx=20, pady=5, command=writeTextFile)
text_file_btn.pack()
text_file_btn.place(x=x_pos, y=y_pos)
# Label for text file confirmation
y_pos = incY(y_pos, 3 * space)
text_out_label = tk.Label(gui, font=("Arial", 12), bg=bg_color, textvariable=text_status)
text_out_label.place(x=width / 2, y=y_pos, anchor="center")
gui.mainloop()
