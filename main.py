import tkinter
import ttkbootstrap as ttk
import wikipedia


window = ttk.Window(themename="darkly")
window.geometry("500x500")
window.title("Information Getter.")

search_input = ttk.Entry(window, font=("Arial", 12))
search_input.pack(pady=5)


def change_info():
    try:
        summary = wikipedia.summary(search_input.get(), sentences=2, auto_suggest=False)
        information_box.config(text=summary)
    except wikipedia.exceptions.PageError:
        information_box.config(text="Couldn't find info.")
    except wikipedia.exceptions.DisambiguationError:
        information_box.config(text="Please be more specific.")
    except Exception as e:
        information_box.config(text=f"An unknown error occurred. {e}")


get_info_button = ttk.Button(window, text="Get info!", command=change_info)
get_info_button.pack(pady=5)

information_box = ttk.Label(window, text="Enter a class to get information.", wraplength=470, font=("Arial", 13))
information_box.pack(pady=5)

wikipedia_credit = ttk.Label(window, text="Summaries taken from Wikipedia.", font=("Arial", 10))
wikipedia_credit.pack()
wikipedia_credit.place(relx=0.5, rely=0.95, anchor="center")

tkinter.mainloop()
