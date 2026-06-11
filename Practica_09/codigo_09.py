import tkinter as tk
from tkinter import messagebox

# Función del botón Guardar
def guardar():

    valor_pot = entry_pot.get()
    valor_ultra = entry_ultra.get()

    # Validar campos vacíos
    if valor_pot == "" or valor_ultra == "":
        messagebox.showwarning(
            "Advertencia",
            "Todos los campos deben tener contenido."
        )
        return

    # Validar números enteros
    try:
        int(valor_pot)
        int(valor_ultra)

        messagebox.showinfo(
            "Información",
            "Datos validados correctamente."
        )

    except ValueError:
        messagebox.showwarning(
            "Advertencia",
            "Los valores ingresados deben ser de tipo entero."
        )

# Función del botón Limpiar
def limpiar():

    entry_pot.delete(0, tk.END)
    entry_ultra.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("300x180")
ventana.iconbitmap("logo.ico")
ventana.configure(bg="#D9D9D9")

# Etiqueta y caja de texto para potenciómetro
label_pot = tk.Label(
    ventana,
    text="Valor de potenciómetro",
    bg="#D9D9D9",
    fg="#003366"
)
label_pot.pack()

entry_pot = tk.Entry(ventana)
entry_pot.pack()

# Etiqueta y caja de texto para ultrasónico
label_ultra = tk.Label(
    ventana,
    text="Valor de ultrasónico",
    bg="#D9D9D9",
    fg="#003366"
)
label_ultra.pack()

entry_ultra = tk.Entry(ventana)
entry_ultra.pack()

# Contenedor para botones
frame_botones = tk.Frame(
    ventana,
    bg="#D9D9D9"
)
frame_botones.pack(pady=10)

# Botón Guardar
btn_guardar = tk.Button(
    frame_botones,
    text="Guardar",
    bg="#4CAF50",
    fg="white",
    command=guardar
)
btn_guardar.pack(side=tk.LEFT, padx=5)

# Botón Limpiar
btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    bg="#2196F3",
    fg="white",
    command=limpiar
)
btn_limpiar.pack(side=tk.LEFT, padx=5)

ventana.mainloop()
