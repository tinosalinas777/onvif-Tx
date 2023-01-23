from tkinter import *
from tkinter import messagebox
import os
import time
import threading


ventana=Tk()
ventana.geometry("500x300")
ventana.title("Tx-Escritorio")
ventana.config(bg="black")
ventana.resizable(False,False)

def inciarTransmicion(d,p,c):


    
    l=d.get()
    m=p.get()
    n=c.get()
    
    hilo0=threading.Thread(target=onvif,)
    hilo0.start()
    time.sleep(3)
    hilo1=threading.Thread(target=ffmpeg, args=(l,m,n))
    hilo1.start()
    messagebox.showinfo("Emitiendo..","Su escritorio se transmite por protocolo onvif!!")
    ventana.withdraw()
    
def onvif():
    os.system("runme.bat")
def ffmpeg(l,m,n):
    trn=""
    codec=""
    if transport.get()==False:
        trn="udp"
    else:
        trn="tcp"
    
    if h26x.get()==False:
        codec=" -c:v libx264 "
    else:
        codec="-c:v libx265"
    print("ffmpeg -video_size 1920x1080 -framerate 10 -f gdigrab -i desktop "+codec+" -f rtsp -rtsp_transport "+trn+" rtsp://"+l+":"+m+"/"+n)
    os.system("ffmpeg -video_size 1920x1080 -framerate 10 -f gdigrab -i desktop  -f rtsp -rtsp_transport "+trn+" rtsp://"+l+":"+m+"/"+n)
# asignar entradas a variables
ip=StringVar()
puerto=StringVar()
path=StringVar()
transport=BooleanVar()
h26x=BooleanVar()

#etiquetas y entradas (diseño de la ventana)

etiqueta1=Label(ventana, text="direccion ip del servidor",bg="black",fg="white")
etiqueta1.place(x=50,y=100)
etiqueta2=Label(ventana, text="puerto de escucha",bg="black",fg="white")
etiqueta2.place(x=50,y=150)
etiqueta3=Label(ventana, text="path",bg="black",fg="white")
etiqueta3.place(x=50,y=200)
etiqueta4=Label(ventana,text="Tx - ONVIF",bg="black",fg="white",font="none 20 bold")
etiqueta4.place(x=170,y=40)
etiqueta5=Label(ventana, text="Codecs y Protocolos",bg="black",fg="white")
etiqueta5.place(x=360,y=90)
entrada=Entry(ventana, textvariable=ip)
entrada.place(x=185,y=100)
entrada2=Entry(ventana, textvariable=puerto)
entrada2.place(x=185,y=150)
entrada3=Entry(ventana, textvariable=path)
entrada3.place(x=185,y=200)
boton=Button(ventana,text="Emitir", command=lambda:inciarTransmicion(ip,puerto,path), bg="green",width=18,height=2)
boton.place(x=350,y=250)
Rbh264=Radiobutton(ventana, text="H264",value=False,bg="black",fg="green",variable=h26x).place(x=350,y=130)
Rbh265=Radiobutton(ventana, text="H265",value=True,bg="black",fg="green",variable=h26x).place(x=350,y=180)
Rbhtcp=Radiobutton(ventana, text="TCP",value=True,bg="black",fg="green",variable=transport).place(x=420,y=130)
Rbhudp=Radiobutton(ventana, text="UDP",value=False,bg="black",fg="green",variable=transport).place(x=420,y=180)






ventana.mainloop()



