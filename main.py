import tkinter as tk
import re

def main():
    def submit_text_a(text_input):
        a = ["věta hlavní", "věta vedlejší", "podmět", "předmět", "přívlastek shodný",
             "přívlastek neshodný", "přísudek", "příslovečné určení místa", "příslovečné určení způsobu", "doplněk"]

        b = ["pu", "pus", "po", "pt", "pks", "pkn", "ps", "pum", "puz", "dop"]
        submit_text(a, b, text_input)

    window = tk.Tk()
    window.title("neumimslovensky")
    window.geometry("400x400")
    window.resizable(False, False)


    # main text input, we will be also pasting into that
    text_input = tk.Text(window, width=100, height=15)
    text_input.pack()

    # clear text input function
    def clear_text():
        text_input.delete("1.0", "end")

    # if button clear_text is pressed, clear text input
    button_clear_text = tk.Button(window, text="clear text", command=clear_text)
    button_clear_text.pack()

    # pastes into text input the clipboard data
    def paste_clipboard():
        clipboard_text = window.clipboard_get()
        text_input.insert(tk.END, clipboard_text)

    button_paste = tk.Button(window, text="paste from clipboard", command=paste_clipboard)
    button_paste.pack()
    # crates new window that displays a little edited text input value while
    def results(a, b, text_input):
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
    def submit_text(a, b, text_input):
        text_input_value = text_input.get("1.0", "end-1c")
        if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
            green_submit_button()
            # print("correct")
            results(a, b, text_input)
        elif text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
            green_submit_button()
            # print("correct")
            results(a, b, text_input)
        else:
            red_submit_button()
            # print("incorrect")
            # exit()

    # SUBMIT BUTTON
    # add button under text input to submit and store text input in variable
    button_submit = tk.Button(window, text="submit", command=lambda:submit_text_a(text_input))
    button_submit.pack()

    # if button close_window is pressed, close window
    def close_window():
        window.destroy()

    button_exit = tk.Button(window, text="exit", command=close_window)
    button_exit.pack()

    # start window
    window.mainloop()
    # print hello world

# create disclaimer popup window with text
def disclaimer():
    def stupid2():
        window_disclaimer.destroy()
        main()
    window_disclaimer = tk.Tk()
    window_disclaimer.title("disclaimer")
    window_disclaimer.geometry("800x200")
    # make disclaimer window not resizable
    window_disclaimer.resizable(False, False)
    # create text saying this is not intended in disclaimer window
    disclaimer_text = tk.Label(window_disclaimer, text="This application was created only for the purpose of improving the programming skills of the creators and at the same time as a proof of concept.\n"
                                                       " It is not intended for any use with other applications, \nservices, websites and files or text obtained from them, and such use is also prohibited by the creator. \n"
                                                       "The creators waive any responsibility for misuse of the program by the user. \n"
                                                       "By clicking the \"I agree\" button, you confirm that you will not misuse the program for any reason other than testing reasons, \nthat you take all responsibility for your use of this application and that you understand these terms.")
    disclaimer_text.pack()
    button_disclaimer = tk.Button(window_disclaimer, text="I agree", command=stupid2)
    button_disclaimer.pack()
    window_disclaimer.mainloop()



disclaimer()
