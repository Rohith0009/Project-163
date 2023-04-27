from tkinter import *
from tkinter import messagebox
import ctypes

# Compatibility Settings
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("CARDIOVASCULAR SYMPTOMS")
root.geometry("1600x1600")
root.configure(bg="pale turquoise")

radiobtn1 = StringVar(value="0")

q1 = Label(
    root,
    bg="pale turquoise",
    text="Do you experience shortness of breath during routine activities?",
)
q1.pack()

q1r1 = Radiobutton(
    root, bg="pale turquoise", text="Yes", variable=radiobtn1, value="yes"
)
q1r1.pack()

q1r2 = Radiobutton(root, bg="pale turquoise", variable=radiobtn1, text="No", value="no")
q1r2.pack()

radiobtn2 = StringVar(value="0")

q2 = Label(
    root,
    bg="pale turquoise",
    text="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?",
)
q2.pack()

q2r1 = Radiobutton(
    root, bg="pale turquoise", variable=radiobtn2, text="Yes", value="yes"
)
q2r1.pack()

q2r2 = Radiobutton(root, bg="pale turquoise", variable=radiobtn2, text="No", value="no")
q2r2.pack()

radiobtn3 = StringVar(value="0")

q3 = Label(
    root,
    bg="pale turquoise",
    text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?",
)
q3.pack()

q3r1 = Radiobutton(
    root, bg="pale turquoise", variable=radiobtn3, text="Yes", value="yes"
)
q3r1.pack()

q3r2 = Radiobutton(root, bg="pale turquoise", variable=radiobtn3, text="No", value="no")
q3r2.pack()

radiobtn4 = StringVar(value="0")

q4 = Label(
    root,
    bg="pale turquoise",
    text="Do you experience shortness of breath while at rest/lying down?",
)
q4.pack()

q4r1 = Radiobutton(
    root, bg="pale turquoise", variable=radiobtn4, text="Yes", value="yes"
)
q4r1.pack()

q4r2 = Radiobutton(root, bg="pale turquoise", variable=radiobtn4, text="No", value="no")
q4r2.pack()

radiobtn5 = StringVar(value="0")

q5 = Label(
    root,
    bg="pale turquoise",
    text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",
)
q5.pack()

q5r1 = Radiobutton(
    root, bg="pale turquoise", variable=radiobtn5, text="Yes", value="yes"
)
q5r1.pack()

q5r2 = Radiobutton(root, bg="pale turquoise", variable=radiobtn5, text="No", value="no")
q5r2.pack()


def checker():
    score = 0
    if radiobtn1.get() == "yes":
        score += 1

    if radiobtn2.get() == "yes":
        score += 1

    if radiobtn3.get() == "yes":
        score += 1

    if radiobtn4.get() == "yes":
        score += 1

    if radiobtn5.get() == "yes":
        score += 1
    print(score)

    if score == 1:
        messagebox.showinfo(
            "Report", "Your Just Imagining stuff you dont have any problems"
        )
        print("here")
    elif score >= 2 and score <= 3:
        messagebox.showinfo(
            "Report", "You Might Have A Problem I Recommend to go to a doctor"
        )
    elif score == 4:
        messagebox.showinfo("Report", "Go To The DOCTOR TO SURVIVE")
    else:
        messagebox.showinfo("Report", "You Will Probably DIE In 1 minute")


thebtn = Button(root, text="Get Result", bg="pale turquoise", command=checker)
thebtn.pack()

root.mainloop()
