from tkinter import*
from PIL import Image ,ImageTk
import speech_to_text
import action



root= Tk()
root.title("ai assistant")
root.geometry("550x675")
root.resizable(False,False)                              # no resising is allowed
root.config(bg="#000000")

def ask():
    ask_a= speech_to_text.speech_to_voice()
    bot_val= action.Action(ask_a)
    text.insert(END, " use--->>"+ask_a+"/n")
    if bot_val!=None:
        text.insert(END ,"bot <--- "+str(bot_val)+"/n")
    if bot_val == "ok sir":
        root.destroy()


def Send():
    send= entry.get()
    bot =action.Action(send)
    text.insert(END, " use--->>"+send+"/n")
    if bot!=None:
        text.insert(END ,"bot <--- "+str(bot)+"/n")
    if bot == "ok sir":
        root.destroy()

def Del_text():
    text.delete("1.0","end")


# frame

frame = LabelFrame(root ,padx=100,pady = 3,borderwidth =7, relief ="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=0,padx=55,pady=55)


# text label

text_label= Label(frame,text="Ai Assistant",font=("comic Sans ms",14,"bold"),bg="#FDFEFF")
text_label.grid(row=0,column=0,padx=20,pady=10)


#  image
image = Image.open("image/Ai_assistant.png")
image = image.resize((200, 200))

photo = ImageTk.PhotoImage(image)

image_label = Label(frame, image=photo)
image_label.image = photo  # keep reference
image_label.grid(row=1, column=0, pady=20)


# adding text frame 



text =Text(root,font=("curier 10 bold"),bg="#356696")

text.grid(row=2,column=0)
text.place(x=75,y=375,width=375,height=100)    # x & y dipicts the place of text frame & width and hight dipicts its size



# entry widget or command widget
entry = Entry(root , justify=CENTER)
entry.place(x=75,y=500,width=375, height=50)     # x & y dipicts the place of text frame & width and hight dipicts its size



# button
button_1=Button(root,text="ask",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button_1.place(x=70,y=575)


button_2=Button(root,text="Send",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=Send)
button_2.place(x=350,y=575)


button_3=Button(root,text="Delete",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=Del_text)
button_3.place(x=200,y=575)

root.mainloop()
