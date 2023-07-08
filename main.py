# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# importuje nutné moduly
import tkinter as tk  # pro práci s okny
import re  # pro získání důležitých dat z inputu
from tkinter import messagebox # pro error handeling s chybovou hláškou

# každá hodnota každého indexu listu A koresponduje s hodnotou stejného indexu listu B
# jedná se jednoduchou databázi, pomocí které program

# přeložené názvy očekávaných názvů vstupu
a = ["věta hlavní", "věta vedlejší", "podmět", "předmět", "přívlastek shodný",
     "přívlastek neshodný", "přísudek", "příslovečné určení místa", "příslovečné určení způsobu", "doplněk"]
# očekávané zkratkové názvy vstupu
b = ["vh", "vv", "po", "pt", "pks", "pkn", "ps", "pum", "puz", "dop"]


def main():
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

    # funkce a tlačítko pro zavolání funkce pro vložení schránky do inputu
    # POTENCIÁLNÍ PORUŠENÍ BEZPEČNOSTI A NARUŠENÍ SOUKROMÍ
    def paste_clipboard():
        try:
            clipboard_text = window.clipboard_get()
            text_input.insert(tk.END, clipboard_text)
        except tk.TclError: # v případě problému se schránkou handelne error chybovou hláškou
            messagebox.showwarning("Clipboard Error", "Clipboard is empty or unavailable.")

    button_paste = tk.Button(window, text="paste from clipboard", command=paste_clipboard)
    button_paste.pack()

    # vznik okna pro zobrazení výstupu
    def results():
        window_results = tk.Tk()
        window_results.title("results")
        window_results.geometry("500x400")
        window_results.resizable(True, True)
        scrollbar = tk.Scrollbar(window_results)  # přidá scrollbar
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # přidá scrollbar
        text_results = tk.Text(window_results, width=130, height=400)
        text_results.pack()
        # __________________________________________________________________________________________
        text_input_value = text_input.get("1.0", "end-1c")  # vytvoření krátkodobé proměné pro práci s ní

        # za pomoci regexu (?<==')(.*?)(?='>) extrahuje pouze důležitý text

        if is_debug_mode == 2:  # v případě zapnutého debug módu proces přeskočí
            text_results_value = str(text_input_value)
        else:
            # za pomoci regexu nalezne všechna důležitá data a uschová je do krátkodobé proměn
            text_results_value = re.findall(r'''(?<==\')(.*?)(?=\')''', str(text_input_value))

        # překládá zkratková slova za pomoci listu A a listu B

        # NÁSLEDUJÍCÍ ŘÁDEK NEGATIVNĚ OVLIVŇUJE OUTPUT, NEBOŤ PO SOBĚ ZANECHÁVÁ PO SOBĚ PRVKY LISTU VE FORMĚ STRINGU
        text_results_value_str = str(text_results_value)  # změní list dat na string pro lepší manipulaci
        # přeskočí krok, pokud je zapnutý debug mód
        if is_debug_mode == 3:
            pass
        else:
            # loop, který projede každý index v listu b
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
        results()
    # funkce pro změnu barvy tlačítka v případě pravděpodobně špatného inputu
    def red_submit_button():
        button_submit.config(fg="red")
        button_submit.after(500, lambda: button_submit.config(fg="black"))

    # logika schvalování inputu
    # pokud je stisknuto tlačítko submit,
    # je zkontrolováno, zda je input správný a v případě že je,
    # a zavolá se funkce results.
    def submit_text():
        text_input_value = text_input.get("1.0", "end-1c")
        # v případě zaplého debug módu je celá logika přeskočena a funkce results je zavolána okamžitě
        if is_debug_mode < 1:

            if text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[7] == "i":
                green_submit_button()

            elif text_input_value.startswith("{") and text_input_value.endswith("}") and text_input_value[5] == "i":
                green_submit_button()

            else:
                red_submit_button()

        else:
            green_submit_button()

    # tlačítko submit
    # vloží input do proměné a zavolá logiku pro schvalování inputu
    button_submit = tk.Button(window, text="submit", command=lambda: submit_text())
    button_submit.pack()

    # tlačítko pro ukončení aplikace
    def close_window():
        window.destroy()

    button_exit = tk.Button(window, text="exit", command=close_window)
    button_exit.pack()

    # zapne hlavní inputové okno
    window.mainloop()

# okno pro zvolení DM
def debug_mode_choose():
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

    def runmain():
        debug_mode_window.destroy()
        main()

    global is_debug_mode
    is_debug_mode = 0

    def DM_1():
        global is_debug_mode
        is_debug_mode = 1
        runmain()

    def DM_2():
        global is_debug_mode
        is_debug_mode = 2
        runmain()

    def DM_3():
        global is_debug_mode
        is_debug_mode = 3
        runmain()

    # funguje normálně
    debug_mode_button_no = tk.Button(debug_mode_window, text="no", command=runmain, font=('Arial', 20))
    # ignoruje kontrolu správného inputu
    debug_mode_button_1 = tk.Button(debug_mode_window, text="1", command=DM_1)
    # ignoruje kontrolu správného inputu a zároveň přeskakuje filtraci regexem
    debug_mode_button_2 = tk.Button(debug_mode_window, text="2", command=DM_2)
    # ignoruje kontrolu správného inputu a zároveň přeskakuje překládání zkratek
    debug_mode_button_3 = tk.Button(debug_mode_window, text="3", command=DM_3)

    debug_mode_button_no.pack()
    debug_mode_button_1.pack()
    debug_mode_button_2.pack()
    debug_mode_button_3.pack()

    debug_mode_window.mainloop()



# okno pro zvolení, zda chce uživatel běžet vanilla program, či zda má zájem přejít k výběru různých DM
def debug_mode_YN():
    global is_debug_mode
    is_debug_mode = 0
    def runmain():
        debug_mode_YN.destroy()
        main()

    def runDM():
        debug_mode_YN.destroy()
        debug_mode_choose()

    debug_mode_YN = tk.Tk()
    debug_mode_YN.title("Debug Mode")

    debug_mode_text_YN = tk.Label(debug_mode_YN, text="Do you want to start debug mode?", font=('Arial', 18))
    debug_mode_text_YN.grid(row=0, column=0, padx=5, pady=10, columnspan=2,)

    # tlačítko 1 pro spuštění neumímeslovensky
    button1 = tk.Button(debug_mode_YN, text="Yes", command=runmain)
    button1.grid(row=1, column=0, padx=10, pady=5)

    # tlačítko pro spuštění výběru debug módu
    button2 = tk.Button(debug_mode_YN, text="No", command=runDM)
    button2.grid(row=1, column=1, padx=10, pady=5)
    # logika velikosti okna a pozici tlačítek
    debug_mode_YN.update()  # aktualizuje okno, pro případnou úpravu jeho velikosti

    label_width = debug_mode_text_YN.winfo_width()
    button1_width = button1.winfo_width()
    button2_width = button2.winfo_width()

    max_button_width = max(button1_width, button2_width)

    window_width = max(label_width, max_button_width) + 30  # přidá extra prostor

    window_height = 150

    debug_mode_YN.geometry(f"{window_width}x{window_height}")
    debug_mode_YN.resizable(False, False)

    debug_mode_YN.mainloop()

# okno pro zobrazení prostého textu disclaimeru
def disclaimer():
    def runDM():
        window_disclaimer.destroy()
        debug_mode_YN()

    window_disclaimer = tk.Tk()
    window_disclaimer.title("disclaimer")
    window_disclaimer.geometry("600x150")
    window_disclaimer.resizable(False, False)
    # text disclaimeru
    # bylo by vhodné mít tento text uložený v samostatném soboru, nikoliv součástí aplikace
    disclaimer_text = tk.Label(window_disclaimer,
                               text="""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
    disclaimer_text.pack()
    button_disclaimer = tk.Button(window_disclaimer, text="I agree", command=runDM)
    button_disclaimer.pack()
    window_disclaimer.mainloop()


# zapne okno disclaimeru a tím pádem celého programu
disclaimer()
