#A program for announcing that there's no classes.

#Utility Functions//

import time
import tkinter as tk

#header
def header():
    print()
    print("—————————————————————————————————————")
    print()


#Main Program//

header()
print("IMPORTANT ANNOUNCEMENT!")
header()

print("...")
time.sleep(1)

def show_announcement():
    root = tk.Tk()
    root.title("EMERGENCY ANNOUNCEMENT")
    root.configure(bg="red")

    window_width = 800
    window_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    header_label = tk.Label(
        root,
        text=".. IMPORTANT ANNOUNCEMENT ..",
        font=("Arial", 32, "bold"),
        bg="red",
        fg="white",
    )
    header_label.pack(pady=40)

    main_label = tk.Label(
        root, text="WALANG PASOK!", font=("Arial", 60, "bold"), bg="red", fg="yellow"
    )
    main_label.pack(pady=20)

    root.mainloop()


#Run it
show_announcement()