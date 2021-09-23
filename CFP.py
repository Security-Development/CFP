import os
from tkinter import *
from tkinter import messagebox

strHome = os.getenv("USERPROFILE")

arrFile = [
    "app.py",
    "templates\index.html"
]

arrHoDir = [
    "static",
    "templates",
    "static\css",
    "static\js",
    "static\image"
]

app = {
"app.py": """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!!</h1>"

app.run(host="localhost", port=5000)
"""
}

def sendMessage(text):
    return messagebox.showinfo("안내", text)

def createProject():
    if ent.get() == "":
        return

    strPath = f"{strHome}\Desktop\{ent.get()}"

    try:
        os.makedirs(strPath)
    except FileExistsError:
        sendMessage("해당 이름으로 프로젝트가 이미 생성 되었습니다.")
        return

    for i in arrHoDir:
        os.makedirs(f"{strPath}\{i}")

    for i in arrFile:
        file = open(f"{strPath}\{i}", "w")
        try:
            file.write(app[i])
            sendMessage("app.py 파일 생성 완료\n")
        except KeyError:
            sendMessage("index.html 파일 생성 완료")

        file.close()

form = Tk()

form.title("CFP(CreateFlaskProject)")
form.geometry("300x100")
form.resizable(False, False)

ent = Entry(form, fg='Grey')
ent.insert(0, "프로젝트 이름을 적어주세요.")
ent.bind("<FocusIn>", lambda event: ent.delete(False, END))
ent.bind("<FocusOut>", lambda event: ent.insert(False, "프로젝트 이름을 적어주세요."))
ent.pack(padx=10, pady=15)

btn = Button(form, text="CreateProject", command=createProject)
btn.pack()

form.mainloop()
