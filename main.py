import tkinter as tk
import re


def main(is_debug_mode):
    def submit_text_a(is_debug_mode):
        a = ["věta hlavní", "věta vedlejší", "podmět", "předmět", "přívlastek shodný",
             "přívlastek neshodný", "přísudek", "příslovečné určení místa", "příslovečné určení způsobu", "doplněk"]

        b = ["vh", "vv", "po", "pt", "pks", "pkn", "ps", "pum", "puz", "dop"]
        submit_text(a, b, is_debug_mode)

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
    def results(a, b, is_debug_mode):
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

        if is_debug_mode == 3:
            text_results_value = str(text_input_value)
        else:
            text_results_value = re.findall(r'''(?<==\')(.*?)(?=\')''', str(text_input_value))

        # translates abbreviations

        text_results_value_str = str(text_results_value)
        if is_debug_mode == 4:
            j = 136137138
        else:
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
    def submit_text(a, b, is_debug_mode):
        if is_debug_mode < 2:
            text_input_value = text_input.get("1.0", "end-1c")
            if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
                green_submit_button()
                # print("correct")
                results(a, b, is_debug_mode)
            elif text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
                green_submit_button()
                # print("correct")
                results(a, b, is_debug_mode)
            else:
                red_submit_button()
                # print("incorrect")
                # exit()
        else:
            results(a, b, is_debug_mode)

    # SUBMIT BUTTON
    # add button under text input to submit and store text input in variable
    button_submit = tk.Button(window, text="submit", command=lambda: submit_text_a(is_debug_mode))
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
def disclaimer(is_debug_mode):
    def stupid2(is_debug_mode):
        window_disclaimer.destroy()
        main(is_debug_mode)

    window_disclaimer = tk.Tk()
    window_disclaimer.title("disclaimer")
    window_disclaimer.geometry("800x200")
    # make disclaimer window not resizable
    window_disclaimer.resizable(False, False)
    # disclaimer text
    disclaimer_text = tk.Label(window_disclaimer,
                               text="This application was created only for the purpose of "
                                    "improving the programming skills of the creators and "
                                    "at the same time as a proof of concept.\n"
                                    " It is not intended for any use with other applications,"
                                    " \nservices, websites "
                                    "and files or text obtained from them, and such use is "
                                    "also prohibited by the creator. \n"
                                    "The creators waive any responsibility for misuse of the "
                                    "program by the user. \n"
                                    "By clicking the \"I agree\" button, you confirm that you"
                                    " will not misuse the program "
                                    "for any reason other than testing reasons, \nthat you"
                                    " take all responsibility for your "
                                    "use of this application and that you understand these terms.")
    disclaimer_text.pack()
    button_disclaimer = tk.Button(window_disclaimer, text="I agree", command=lambda: stupid2(is_debug_mode))
    button_disclaimer.pack()
    window_disclaimer.mainloop()


def debug_mode():
    debug_mode_window = tk.Tk()
    debug_mode_window.title("debug mode")
    debug_mode_window.geometry("400x400")
    debug_mode_window.resizable(False, False)
    debug_mode_text = tk.Label(debug_mode_window, text="Do you want to start debug mode?", font=('Arial', 18))
    debug_mode_text2 = tk.Label(debug_mode_window,
                                text="(if you dont know what to select, press no. "
                                     "\nIf you had problems with the program before,"
                                     " \nI suggest trying all the debug modes in order.)",
                                font=('Arial', 8))
    debug_mode_text.pack()
    debug_mode_text2.pack()

    def func_no():
        is_debug_mode = 1
        debug_mode_window.destroy()
        disclaimer(is_debug_mode)

    def func_1():
        is_debug_mode = 2
        debug_mode_window.destroy()
        disclaimer(is_debug_mode)

    def func_2():
        is_debug_mode = 3
        debug_mode_window.destroy()
        disclaimer(is_debug_mode)

    def func_3():
        is_debug_mode = 4
        debug_mode_window.destroy()
        disclaimer(is_debug_mode)

    # works normally
    debug_mode_button_no = tk.Button(debug_mode_window, text="no", command=func_no, font=('Arial', 20))
    # ignores check for right input
    debug_mode_button_1 = tk.Button(debug_mode_window, text="1", command=func_1)
    # ignores check for right input and regex search
    debug_mode_button_2 = tk.Button(debug_mode_window, text="2", command=func_2)
    # ignores check for right input and abbreviation translation
    debug_mode_button_3 = tk.Button(debug_mode_window, text="3", command=func_3)
    debug_mode_button_no.pack()
    debug_mode_button_1.pack()
    debug_mode_button_2.pack()
    debug_mode_button_3.pack()
    debug_mode_window.mainloop()


debug_mode()
