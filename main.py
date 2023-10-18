import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Ping-Pong Retro")

#configuracion de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
canvas = tk.Canvas(ventana,width=ancho_pantalla, height=alto_pantalla, bg="Black")
canvas.pack()

#Raqueta

raqueta = canvas.create_rectangle(350,580,450,590,fill="White")

#pelota
pelota = canvas.create_oval(390,290,410,310,fill="red")

velocidad_x = random.choice([2,-2])
velocidad_y = -2
#Funcion para mover la raqueta 

def mover_raqueta(event):
    
    tecla = event.keysym
    
    if tecla == "Left":
        canvas.move(raqueta,-20,0)
    elif tecla == "Right":
        canvas.move(raqueta,20,0)


canvas.bind_all("<KeyPress-Left>",mover_raqueta)
canvas.bind_all("<KeyPress-Right>",mover_raqueta)


def actualizar_juego():
    global velocidad_x, velocidad_y, actualizar
    canvas.move(pelota, velocidad_x, velocidad_y)
    pelota_pos = canvas.coords(pelota)

    if pelota_pos[0] <= 0 or pelota_pos[2] >= ancho_pantalla:
        velocidad_x *= -1
    
    if pelota_pos[1] <= 0:
        velocidad_y *= -1
    
    if canvas.coords(raqueta)[0] <= pelota_pos[2] <= canvas.coords(raqueta)[2] and canvas.coords(raqueta)[1] <= pelota_pos[3] <= canvas.coords(raqueta)[3]:
        velocidad_y *= -1
    
    if pelota_pos[3] >= alto_pantalla:
        canvas.create_text(ancho_pantalla / 2, alto_pantalla / 2, text="Game Over", fill="Orange", font=("Arial", 36))
        ventana.after_cancel(actualizar)
    actualizar = ventana.after(10, actualizar_juego)

actualizar_juego()
ventana.mainloop()