# import tkinter
# import urllib.request

# url="http://192.168.4,1"
# window=tkinter.Tk()
# window.title("ESP8266 WITH PYTHON")
# def sendRequest(url):
#     a=urllib.request.urlopen(url)

# while True:
#     headline=tkinter.Label(window,text="Bot control with python Tkinter(ESP2866)",fg="red",font=("ANUDAW",25))
#     headline.grid(column=2,row=0)
#     ON=tkinter.Button(window,text="ON",command=None,fg="yellow",bg="green",font=("Lobster 1.4",25))
#     ON.grid(column=2,row=1)
#     OFF=tkinter.Button(window,text="OFF",command=None,fg="yellow",bg="green",font=("Lobster 1.4",25))
#     OFF.grid(column=2,row=2)
#     window.mainloop()

class parent:
    def __init__(self):
        print("parent's __init__() invoked")
class Derived(parent):
    def __new__(self):
        print("Derived's __new__() invoked")
    def __init__(self):
        print("Derived's __init__() invoked")
def main():
    obj1 = parent()
    obj2 = Derived()
main()