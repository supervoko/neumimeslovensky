# importuje nutné moduly
import tkinter as tk        # pro práci s okny
import re                   # pro získání důležitých dat z inputu


def main(is_debug_mode):
    def submit_text_a(is_debug_mode):
        # každá hodnota každého indexu listu A koresponduje s hodnotou stejného indexu listu B
        # jedná se jednoduchou databázi, pomocí které program
        # přeložené názvy očekávaných názvů vstupu
        a = ["věta hlavní", "věta vedlejší", "podmět", "předmět", "přívlastek shodný",
             "přívlastek neshodný", "přísudek", "příslovečné určení místa", "příslovečné určení způsobu", "doplněk"]
        # očekávané zkratkové názvy vstupu
        b = ["vh", "vv", "po", "pt", "pks", "pkn", "ps", "pum", "puz", "dop"]
        submit_text(a, b, is_debug_mode)

    window = tk.Tk()
    window.title("neumimeslovensky")
    window.geometry("400x400")
    window.resizable(False, False)

    # okno s textovým políčkem pro input
    text_input = tk.Text(window, width=100, height=15)
    text_input.pack()

    # funkce pro odstranění všeho textu
    def clear_text():
        text_input.delete("1.0", "end")

    # tlačítko se zavoláním funkce pro odstranění textu
    button_clear_text = tk.Button(window, text="clear text", command=clear_text)
    button_clear_text.pack()

    # funkce a tlačítko pro zavolání funkce pro
    # vložení schránky do inputu
    # POTENCIÁLNÍ PORUŠENÍ BEZPEČNOSTI A NARUŠENÍ SOUKROMÍ
    def paste_clipboard():
        clipboard_text = window.clipboard_get()
        text_input.insert(tk.END, clipboard_text)

    button_paste = tk.Button(window, text="paste from clipboard", command=paste_clipboard)
    button_paste.pack()

    # vznik okna pro zobrazení výstupu
    def results(a, b, is_debug_mode):
        window_results = tk.Tk()
        window_results.title("results")
        window_results.geometry("500x400")
        window_results.resizable(True, True)
        scrollbar = tk.Scrollbar(window_results) # přidá scrollbar
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # přidá scrollbar
        text_results = tk.Text(window_results, width=130, height=400)
        text_results.pack()
        #__________________________________________________________________________________________
        text_input_value = text_input.get("1.0", "end-1c") # vytvoření krátkodobé proměné pro práci s ní

        # za pomoci regexu (?<==')(.*?)(?='>) extrahuje pouze důležitý text


        if is_debug_mode == 3: # v případě zapnutého debug módu proces přeskočí
            text_results_value = str(text_input_value)
        else:
            # za pomoci regexu nalezne všechna důležitá data a uschová je do krátkodobé proměn
            text_results_value = re.findall(r'''(?<==\')(.*?)(?=\')''', str(text_input_value))

        # překládá zkratková slova za pomoci listu A a listu B

        # NÁSLEDUJÍCÍ ŘÁDEK NEGATIVNĚ OVLIVŇUJE OUTPUT, NEBOŤ PO SOBĚ ZANECHÁVÁ PO SOBĚ PRVKY LISTU VE FORMĚ STRINGU
        text_results_value_str = str(text_results_value) # změní list dat na string pro lepší manipulaci
        # přeskočí krok, pokud je zapnutý debug mód
        if is_debug_mode == 4:
            pass
        else:
            # loop, který projede keždý index v listu b
            # a nahradí hodnotu toho indexu za hodnotu stejného indexu v listu a
            for x in range(len(a)):
                text_results_value_str = text_results_value_str.replace(b[x], a[x])
        # strčí výsledek do dříve vytvořeného okna
        text_results.insert(tk.END, text_results_value_str)
        # tlačítko pro zavření okna
        button_results = tk.Button(window_results, text="close", command=window_results.destroy)
        button_results.pack()

    # funkce pro změnu barvy tlačítka v případě správného inputu
    def green_submit_button():
        button_submit.config(fg="green")
        button_submit.after(500, lambda: button_submit.config(fg="black"))

    # funkce pro změnu barvy tlačítka v případě pravděpodobně špatného inputu
    def red_submit_button():
        button_submit.config(fg="red")
        button_submit.after(500, lambda: button_submit.config(fg="black"))

    # logika schvalování inputu
    # pokud je stisknuto tlačítko submit,
    # je zkontrolováno, zda je input správný a v případě že je,
    # a zavolá se funkce results.
    def submit_text(a, b, is_debug_mode):
        # v případě zaplého debug módu je celá logika přeskočena a funkce results je zavolána okamžitě
        if is_debug_mode < 2:
            text_input_value = text_input.get("1.0", "end-1c")

            if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
                green_submit_button()
                results(a, b, is_debug_mode)

            elif text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
                green_submit_button()
                results(a, b, is_debug_mode)

            else:
                red_submit_button()

        else:
            results(a, b, is_debug_mode)

    # tlačítko submit
    # vloží input do proměné a zavolá logiku pro schvalování inputu
    button_submit = tk.Button(window, text="submit", command=lambda: submit_text_a(is_debug_mode))
    button_submit.pack()

    # tlačítko pro ukončení aplikace
    def close_window():
        window.destroy()

    button_exit = tk.Button(window, text="exit", command=close_window)
    button_exit.pack()

    # zapne hlavní inputové okno
    window.mainloop()


# vytvoří okno pro disclaimer a ukončí okno debug módu
def disclaimer(is_debug_mode):
    def rundisc(is_debug_mode):
        window_disclaimer.destroy()
        main(is_debug_mode)

    window_disclaimer = tk.Tk()
    window_disclaimer.title("disclaimer")
    window_disclaimer.geometry("800x200")
    window_disclaimer.resizable(False, False)
    # text disclaimeru
    # bylo by vhodné mít tento text uložený v samostatném soboru, nikoliv součástí aplikace
    disclaimer_text = tk.Label(window_disclaimer,
                               text="This application was created only for the purpose of "
                                    "improving the programming skills of the creators and "
                                    "at the same time as a proof of concept.\n"
                                    " It is not intended for any use with other applications,"
                                    " \nservices, websites "
                                    "and files or text obtained from them, and such use is "
                                    "also prohibited by the creator. \n"
                                    "The creators waive any responsibility for the misuse of the "
                                    "program by the user. \n"
                                    "By clicking the \"I agree\" button, you confirm that you"
                                    " will not misuse the program "
                                    "for any reason other than testing reasons, \nthat you"
                                    " take all responsibility for your "
                                    "use of this application and that you understand these terms.")
    disclaimer_text.pack()
    button_disclaimer = tk.Button(window_disclaimer, text="I agree", command=lambda: rundisc(is_debug_mode))
    button_disclaimer.pack()
    window_disclaimer.mainloop()

# okno pro zvolení debug módu
# cílem výběru debug módu je, aby si uživatel mohl zvolit, pokud mu určitá část kódu způsobuje problémy
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

    # funguje normálně
    debug_mode_button_no = tk.Button(debug_mode_window, text="no", command=func_no, font=('Arial', 20))
    # ignoruje kontrolu správného inputu
    debug_mode_button_1 = tk.Button(debug_mode_window, text="1", command=func_1)
    # ignoruje kontrolu správného inputu a zároveň přeskakuje filtraci regexem
    debug_mode_button_2 = tk.Button(debug_mode_window, text="2", command=func_2)
    # ignoruje kontrolu správného inputu a zároveň přeskakuje překládání zkratek
    debug_mode_button_3 = tk.Button(debug_mode_window, text="3", command=func_3)
    debug_mode_button_no.pack()
    debug_mode_button_1.pack()
    debug_mode_button_2.pack()
    debug_mode_button_3.pack()
    debug_mode_window.mainloop()

# zapne výběr debug módu a tím pádem celého programu
debug_mode()
