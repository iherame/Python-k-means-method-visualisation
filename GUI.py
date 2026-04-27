import tkinter as tk
from funcs import *
from PIL import Image, ImageTk


XDIST = 30
YDIST = 30
CLUSTER_LIM = 10

def display(field, string):
    if isinstance(field, tk.Text):
        field.delete("1.0", "end")
        field.insert("1.0", string)
    elif isinstance(field, tk.Entry):
        field.delete(0, tk.END)
        field.insert(0, string)

def place_frame(frame, cb, cluster_slider, width_slider, height_slider, image_label):

    # max_clust = cb // CLUSTER_LIM
    max_clust = CLUSTER_LIM if cb > CLUSTER_LIM else cb
    cluster_slider = tk.Scale(frame, from_=1, to=max_clust, orient=tk.HORIZONTAL, length=500, background="#212121", fg="white")
    cluster_slider.place(x=XDIST,y=25)

    cluster_label = tk.Label(frame, text="Кол-во кластеров",font=("Arial",10), fg="white", background="#212121")
    cluster_label.place(x=XDIST+395, y=0)

    cluster_btn = tk.Button(frame,text="Кластеризовать",font=("Arial",10), background="#424242", fg="white",command=lambda: cluster_triger(cluster_slider, width_slider, height_slider, image_label))
    cluster_btn.place(x=XDIST+380, y=YDIST+45)

    frame.place(x=0,y=260, relwidth=0.5, relheight=0.5)

def cluster_triger(cluster_slider, width_slider, height_slider, image_label):
    cluster_count = cluster_slider.get()
    width = width_slider.get()
    height = height_slider.get()
    k_means_method(cluster_count, width, height, pixels)

    img = ImageTk.PhotoImage(Image.open("2.png"))
    image_label.configure(image=img)
    image_label.image = img



def create_triger(frame,height_slider, width_slider,power_slider, image_label):
    width = width_slider.get()
    height = height_slider.get()
    power = power_slider.get()
    global pixels
    count_of_black, pixels = get_image(width, height, power)

    place_frame(frame, count_of_black, 0, width_slider,height_slider, image_label)

    img = ImageTk.PhotoImage(Image.open("1.png"))
    image_label.configure(image=img)
    image_label.image = img

    with open ("temp.txt", "w") as f:
        for row in pixels:
            f.write(str(row))





def gui():
    # WINDOW CONFIGURATION
    window = tk.Tk()
    window.geometry("1090x560+450+70")
    window.resizable(False, False)
    window.configure(background="#212121")


    image_label = tk.Label()
    image_label.place(relx=0.7431, rely=0.5, anchor="center")

    # SLIDERS
    height_slider = tk.Scale(window, from_=10, to=500, orient=tk.HORIZONTAL, length=500, background="#212121", fg="white")
    height_slider.place(x=XDIST, y=YDIST)

    height_label = tk.Label(text="Высота изображения",font=("Arial",10), fg="white", background="#212121")
    height_label.place(x=XDIST+373,y=YDIST-20)

    width_slider = tk.Scale(window, from_=10, to=500, orient=tk.HORIZONTAL, length=500, background="#212121", fg="white")
    width_slider.place(x=XDIST, y=YDIST+70)

    width_label = tk.Label(text="Ширина изображения",font=("Arial",10), fg="white", background="#212121")
    width_label.place(x=XDIST+373,y=YDIST+50)

    power_slider = tk.Scale(window, from_=1, to=100, orient=tk.HORIZONTAL, length=500, background="#212121", fg="white")
    power_slider.place(x=XDIST, y=YDIST+140)

    power_label = tk.Label(text="Мощность множества",font=("Arial",10), fg="white", background="#212121")
    power_label.place(x=XDIST+370,y=YDIST+120)

    # BUTTONS
    creat_btn = tk.Button(window, text="Создать",font=("Arial",10), background="#424242", fg="white",command=lambda: create_triger(frame_cluster, height_slider, width_slider, power_slider, image_label))
    creat_btn.place(x=XDIST+425,y=YDIST+190)

    # FRAME
    frame_cluster = tk.Frame(window, bg="#212121")


    window.mainloop()
