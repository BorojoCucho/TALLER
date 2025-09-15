import tkinter as tk
from tkinter import messagebox, Toplevel

# Crear ventana principal primero
ventana = tk.Tk()
ventana.title("Gestor de Recetas")
ventana.geometry("400x500")

# Clase Receta para almacenar nombre y lista de ingredientes
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

# Clase GestorRecetas para gestionar las recetas
class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

# Función para mostrar ayuda
def mostrar_ayuda():
    messagebox.showinfo(
        "Acerca de las recetas",
        """Recetas Python
Desarrollada en Python 3

Autor: BOROJO
Versión: 1.0

Funcionalidad:
- Crear Recetas
- Verificar recetas
- Almacenar recetas"""
    )

# Función para agregar una nueva receta
def agregar_receta():
    nombre = entry_nombre.get()
    ingredientes = entry_ingredientes.get().split(",")
    ingredientes = [i.strip() for i in ingredientes]  # limpiar espacios
    
    if nombre and ingredientes and all(ingredientes):
        gestor.agregar_receta(nombre, ingredientes)
        listbox_recetas.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente válido.")

# Función para mostrar los ingredientes de una receta seleccionada en una ventana nueva
def ver_ingredientes():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]

        # Crear ventana nueva para mostrar ingredientes
        ventana_ingredientes = Toplevel(ventana)
        ventana_ingredientes.title(f"Ingredientes de {receta.nombre}")
        ventana_ingredientes.geometry("300x300")

        label = tk.Label(ventana_ingredientes, text=f"Ingredientes de {receta.nombre}:", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Mostrar cada ingrediente en una etiqueta separada o en un Text (editable no)
        text_ingredientes = tk.Text(ventana_ingredientes, wrap="word", height=15, width=40)
        text_ingredientes.pack(padx=10, pady=10, fill="both", expand=True)
        text_ingredientes.insert("1.0", "\n".join(receta.ingredientes))
        text_ingredientes.config(state="disabled")  # que no sea editable

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(ventana_ingredientes, text="Cerrar", command=ventana_ingredientes.destroy)
        btn_cerrar.pack(pady=5)
    else:
        messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")

# Función para eliminar una receta seleccionada
def eliminar_receta():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_receta(indice)
        if nombre:
            listbox_recetas.delete(indice)
            messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la receta.")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para eliminar.")

# Crear barra de menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Menú Archivo
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Instancia del gestor de recetas
gestor = GestorRecetas()

# Agregar recetas predeterminadas
gestor.agregar_receta("Sancocho", [
    "1 kg de carne de res o pollo",
    "3 mazorcas de maíz",
    "2 yucas medianas",
    "3 papas",
    "2 plátanos verdes",
    "1 cebolla",
    "2 dientes de ajo",
    "Sal y pimienta al gusto",
    "Cilantro"
])

gestor.agregar_receta("Jugo de Borojo", [
    "1 taza de pulpa de borojo",
    "2 tazas de agua",
    "2 cucharadas de azúcar o miel (al gusto)",
    "Jugo de 1 limón"
])
gestor.agregar_receta("Galletas", [
    "2 tazas de harina",
    "1 taza de azúcar",
    "1 taza de mantequilla",
    "1 huevo",
    "1 cucharadita de polvo para hornear",
    "1 cucharadita de esencia de vainilla",
    "Pizca de sal"
])

gestor.agregar_receta("Pasta", [
    "200 g de pasta",
    "2 dientes de ajo",
    "1 taza de salsa de tomate",
    "Aceite de oliva",
    "Sal y pimienta al gusto",
    "Queso rallado (opcional)"
])

gestor.agregar_receta("Pizza Americana", [
    "1 masa para pizza",
    "1 taza de salsa de tomate",
    "200 g de queso mozzarella",
    "100 g de pepperoni",
    "Aceitunas (opcional)",
    "Orégano al gusto"
])

gestor.agregar_receta("Hamburguesa", [
    "1 pan de hamburguesa",
    "150 g de carne molida",
    "Lechuga",
    "Tomate en rodajas",
    "Queso cheddar",
    "Mostaza y ketchup al gusto"
])
gestor.agregar_receta("Pastel de Tres Leches", [
    "1 taza de harina",
    "1 taza de azúcar",
    "4 huevos",
    "1/2 taza de leche",
    "1 cucharadita de polvo para hornear",
    "1 lata de leche condensada",
    "1 lata de leche evaporada",
    "1 taza de crema de leche o nata"
])

# Etiquetas y entradas para el nombre y los ingredientes
label_nombre = tk.Label(ventana, text="Nombre de la receta:")
label_nombre.pack(pady=(10, 2))

entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=(0, 10), fill="x", padx=20)

label_ingredientes = tk.Label(ventana, text="Ingredientes (separados por coma):")
label_ingredientes.pack(pady=(0, 2))

entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack(pady=(0, 10), fill="x", padx=20)

# Botón para agregar receta
btn_agregar = tk.Button(ventana, text="Agregar receta", command=agregar_receta)
btn_agregar.pack(pady=(0, 10))

# Listbox para mostrar las recetas guardadas
listbox_recetas = tk.Listbox(ventana)
listbox_recetas.pack(pady=(0, 10), fill="both", expand=True, padx=20)

# Mostrar las recetas iniciales en el listbox
for receta in gestor.recetas:
    listbox_recetas.insert(tk.END, receta.nombre)

# Frame para botones juntos
btn_frame = tk.Frame(ventana)
btn_frame.pack(pady=(0, 20))

# Botones para ver y eliminar recetas
btn_ver = tk.Button(btn_frame, text="Ver ingredientes", command=ver_ingredientes)
btn_ver.pack(side="left", padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar receta", command=eliminar_receta)
btn_eliminar.pack(side="left", padx=5)

ventana.mainloop()
