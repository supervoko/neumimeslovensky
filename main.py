import tkinter as tk
import re


def submit_text_a():
    a = ["věta hlavní", "věta vedlejší", "podmět", "předmět", "přívlastek shodný",
         "přívlastek neshodný", "přísudek", "příslovečné určení místa", "příslovečné určení způsobu"]

    b = ["vh", "vv", "po", "pt", "pks", "pkn", "ps", "pum", "puz"]
    submit_text(a, b)


window = tk.Tk()
window.title("neumislovensky")
window.geometry("400x400")
window.resizable(False, False)


# create disclaimer popup window with text
def disclaimer():
    window_disclaimer = tk.Tk()
    window_disclaimer.title("disclaimer")
    window_disclaimer.geometry("400x200")
    # make disclaimer window not resizable
    window_disclaimer.resizable(False, False)
    # create text saying this is not intended in disclaimer window
    disclaimer_text = tk.Label(window_disclaimer, text="This is not intended for use in any way ")
    disclaimer_text.pack()
    button_disclaimer = tk.Button(window_disclaimer, text="close", command=window_disclaimer.destroy)
    button_disclaimer.pack()


# add buttons to window
button_disclaimer = tk.Button(window, text="disclaimer", command=disclaimer)
button_disclaimer.pack()


# create a function to clear text input
def clear_text():
    text_input.delete("1.0", "end")


# if button 3 is pressed, clear text input
button_clear_text = tk.Button(window, text="clear text", command=clear_text)
button_clear_text.pack()


# if button 3 is pressed, close window
def close_window():
    window.destroy()


button_exit = tk.Button(window, text="exit", command=close_window)
button_exit.pack()

# add text input with up to 10000 characters
text_input = tk.Text(window, width=100, height=15)
text_input.pack()


# crates new window that displays a little edited text input value while
def results(a, b):
    window_results = tk.Tk()
    window_results.title("results")
    window_results.geometry("500x400")
    # make results window resizable
    window_results.resizable(True, True)
    # creates scrollable results window
    scrollbar = tk.Scrollbar(window_results)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_results = tk.Text(window_results, width=130, height=400)
    text_results.pack()
    text_input_value = text_input.get("1.0", "end-1c")
    # create string with regex (?<==')(.*?)(?='>) to extract text between brackets
    text_results_value = re.findall(r'''(?<==\')(.*?)(?=\')''', str(text_input_value))
    # translates abbreviations
    text_results_value_str = str(text_results_value)
    for x in range(len(a)):
        text_results_value_str = text_results_value_str.replace(b[x], a[x])
    # packs translated text to output
    text_results.insert(tk.END, text_results_value_str)
    # create button to close results window
    button_results = tk.Button(window_results, text="close", command=window_results.destroy)
    button_results.pack()


def green_submit_button():
    button_submit.config(fg="green")
    button_submit.after(500, lambda: button_submit.config(fg="black"))


def red_submit_button():
    button_submit.config(fg="red")
    button_submit.after(500, lambda: button_submit.config(fg="black"))


# SUBMIT BUTTON AND TEXT INPUT CONTROL
# if submit button is pressed, turn submit whole button color blue for 5 seconds and call submit_text_value function
def submit_text(a, b):
    text_input_value = text_input.get("1.0", "end-1c")
    if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
        green_submit_button()
        # print("correct")
        results(a, b)
    elif text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
        green_submit_button()
        # print("correct")
        results(a, b)
    else:
        red_submit_button()
        # print("incorrect")
        # exit()


# SUBMIT BUTTON
# add button under text input to submit and store text input in variable
button_submit = tk.Button(window, text="submit", command=submit_text_a)
button_submit.pack()

# start window
window.mainloop()
# print hello world
