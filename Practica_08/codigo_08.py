import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("300x180")
ventana.iconbitmap("logo.ico")
ventana.configure(bg="#D9D9D9")  # Gris claro

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

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#D9D9D9")
frame_botones.pack(pady=10)

# Botón Guardar
btn_guardar = tk.Button(
    frame_botones,
    text="Guardar",
    bg="#4CAF50",
    fg="white"
)
btn_guardar.pack(side=tk.LEFT, padx=5)

# Botón Limpiar
btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    bg="#2196F3",
    fg="white"
)
btn_limpiar.pack(side=tk.LEFT, padx=5)

ventana.mainloop()
