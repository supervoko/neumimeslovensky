import tkinter as tk
import re


window = tk.Tk()
window.title("neumimslovensky")
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
button1 = tk.Button(window, text="disclaimer", command=disclaimer)
button1.pack()


# create a function to clear text input
def clear_text():
    text_input.delete("1.0", "end")


# if button 3 is pressed, clear text input
button2 = tk.Button(window, text="clear text", command=clear_text)
button2.pack()


# if button 3 is pressed, close window
def close_window():
    window.destroy()


button3 = tk.Button(window, text="exit", command=close_window)
button3.pack()


# add text input with up to 10000 characters
text_input = tk.Text(window, width=100, height=15)
text_input.pack()


# crates new window that displays a little edited text input value while
def results():
    window_results = tk.Tk()
    window_results.title("results")
    window_results.geometry("400x400")
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
    # ____________________________________________________________________________________________________________
    # CAREFUL! I SPEND 3 HOURS ON THIS PART AND I WASN'T ABLE TO FIND A WAY TO GET IT TO WORK
    # ____________________________________________________________________________________________________________
    # I tried to use loop with two list, but it didn't work

    # create two lists: list1 and list2
    # define edited_text_results_value where everything in text_results_value from list1
    # is replaced with items from list2, and then put it in text_results
    # text_results_value_str = str(text_results_value)
    # a = ["po", "pt"]
    # b = ["podmět", "předmět"]
    # for i in range(len(a)):
    #     if b[i] in text_results_value_str:
    #         text_results_value_str = text_results_value_str.replace(b[i], a[i])
    # print(text_results_value_str)
    # ____________________________________________________________________________________________________________
    # END OF CAREFUL PART
    # ____________________________________________________________________________________________________________

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
def submit_text():
    text_input_value = text_input.get("1.0", "end-1c")
    if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
        green_submit_button()
        # print("correct")
        results()
    else:
        if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
            green_submit_button()
            # print("correct")
            results()
        else:
            red_submit_button()
            # print("incorrect")
            # exit()


# SUBMIT BUTTON
# add button under text input to submit and store text input in variable
button_submit = tk.Button(window, text="submit", command=submit_text)
button_submit.pack()

# start window
window.mainloop()
