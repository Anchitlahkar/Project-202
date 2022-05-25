import socket
from tkinter import *
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# nickname = input("Choose your Nickname:\t")

ip_address = "127.0.0.1"
port = 8000

# client.connect((ip_address, port))

print("Connected with the Server...")


class GUI:

    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.geometry("500x600")
        self.login.configure(bg="lightgreen")
        self.login.resizable(height=FALSE, width=False)

        self.title = Label(self.login, width=10, height=1, text="Login",
                           bg="lightgreen", font="Calibri 35 bold italic")
        self.title.place(x=140, y=10)

        self.line = Label(self.login, width=400, bg="green")
        self.line.place(y=70, relheight=0.01)
        
        nameEntry = Entry(self.login, width=25, justify="center",
                      font=("Chalkboard SE", 22), bd=1, bg="white")
        nameEntry.place(x=50, y=120)
    
        button = Button(self.login, text="Save", font=(
            "Chalkboard SE", 15), command=saveName, width=12, height=1, bg="blue", bd=3)
        button.place(x=50, y=220)

        self.Window.mainloop()


def saveName():
        print("saveName")
    


g = GUI()


"""
def receive():
    while True:
        try:
            msg = client.recv(2048).decode("utf-8")
            if msg == "NICKNAME":
                client.send(nickname.encode("utf-8"))

            else:
                print(msg)

        except:
            print("An error occurred")
            client.close()
            break


def write():
    while True:
        msg = f"{nickname}:{input('')}"
        client.send(msg.encode("utf-8"))


receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
"""
