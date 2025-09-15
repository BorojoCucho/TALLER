import tkinter as tk
import random
import os
# se inserta el icono
icono = "icono.ico"

def iniciar_juego():
    global numero_secreto, intentos_restantes, juego_activo
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 10
    juego_activo = True
    etiqueta_resultado.config(text=f"Número generado. Intentos: {intentos_restantes}")
    boton_adivinar.config(state="normal")
    entrada_intento.delete(0, tk.END)


def verificar_intento():
    global intentos_restantes, juego_activo
    if not juego_activo:
        return
    try:
        intento = int(entrada_intento.get())
        if intento < 1 or intento > 100:
            etiqueta_resultado.config(text="Número fuera de rango")
            return
    except ValueError:
        etiqueta_resultado.config(text="Ingresa un número válido")
        return

    intentos_restantes -= 1
    if intento == numero_secreto:
        etiqueta_resultado.config(text="¡Ganaste!")
        juego_activo = False
        boton_adivinar.config(state="disabled")
    elif intento < numero_secreto:
        etiqueta_resultado.config(text=f"El número es mayor. Intentos: {intentos_restantes}")
    else:
        etiqueta_resultado.config(text=f"El número es menor. Intentos: {intentos_restantes}")

    if intentos_restantes == 0 and intento != numero_secreto:
        etiqueta_resultado.config(text=f"Perdiste. Número era {numero_secreto}")
        juego_activo = False
        boton_adivinar.config(state="disabled")

    entrada_intento.delete(0, tk.END)



# configuración ventana principal
ventana = tk.Tk()
ventana.title("Adivinador")
ventana.geometry("400x350")

# Cargar icono en la ventana principal (solo en Windows)
if os.path.exists(icono):
    try:
        ventana.iconbitmap(icono)
    except tk.TclError:
        print(f"Advertencia: No se pudo aplicar el icono (problema de compatibilidad).")
else:
    print(f"Advertencia: El archivo '{icono}' no se encuentra.")

# frame del adivinador
frame_adivinador = tk.LabelFrame(ventana, text="Adivinador de números", padx=10, pady=10)
frame_adivinador.pack(padx=20, pady=10, fill="x")

boton_generar = tk.Button(frame_adivinador, text="Generar número secreto", command=iniciar_juego)
boton_generar.pack(fill="x", pady=5)

tk.Label(frame_adivinador, text="Ingresa tu intento:").pack()
entrada_intento = tk.Entry(frame_adivinador)
entrada_intento.pack(fill="x", pady=5)

boton_adivinar = tk.Button(frame_adivinador, text="Adivinar", command=verificar_intento, state="disabled")
boton_adivinar.pack(fill="x", pady=5)

etiqueta_resultado = tk.Label(frame_adivinador, text="Genera un número para comenzar")
etiqueta_resultado.pack(pady=10)

# Variables globales para juego
numero_secreto = None
intentos_restantes = 10
juego_activo = False

ventana.mainloop()

