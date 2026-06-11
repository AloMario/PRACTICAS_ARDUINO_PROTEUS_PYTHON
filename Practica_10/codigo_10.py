import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports

# Variable global para la conexión serial
conexion = None


# Función para actualizar la lista de puertos COM
def actualizar_puertos():

    puertos = [puerto.device for puerto in serial.tools.list_ports.comports()]
    combo_com['values'] = puertos

    # No seleccionar ningún puerto por defecto
    combo_com.set("")


# Función para conectar o desconectar
def conectar_desconectar():

    global conexion

    # Si ya existe una conexión, desconectar
    if conexion is not None and conexion.is_open:

        conexion.close()
        conexion = None

        btn_conectar.config(
            text="Conectar",
            bg="#4CAF50"
        )

        messagebox.showinfo(
            "Información",
            "Puerto desconectado correctamente."
        )

        return

    # Obtener puerto seleccionado
    puerto = combo_com.get()

    # Validar selección
    if puerto == "":

        messagebox.showwarning(
            "Advertencia",
            "Debe seleccionar un puerto COM."
        )

        return

    try:

        conexion = serial.Serial(
            puerto,
            baudrate=9600,
            timeout=1
        )

        btn_conectar.config(
            text="Desconectar",
            bg="#F44336"
        )

        messagebox.showinfo(
            "Información",
            f"Conectado correctamente a {puerto}"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"No fue posible conectar al puerto.\n\n{e}"
        )


# ==========================
# Ventana principal
# ==========================

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("350x250")
ventana.iconbitmap("logo.ico")
ventana.configure(bg="#D9D9D9")

# Etiqueta del puerto COM
label_com = tk.Label(
    ventana,
    text="Puerto COM",
    bg="#D9D9D9",
    fg="#003366"
)
label_com.pack(pady=(10, 0))

# ComboBox para los puertos COM
combo_com = ttk.Combobox(
    ventana,
    state="readonly",
    width=25
)
combo_com.pack(pady=5)

# Frame para los botones
frame_botones = tk.Frame(
    ventana,
    bg="#D9D9D9"
)
frame_botones.pack(pady=10)

# Botón Conectar / Desconectar
btn_conectar = tk.Button(
    frame_botones,
    text="Conectar",
    bg="#4CAF50",
    fg="white",
    width=12,
    command=conectar_desconectar
)
btn_conectar.pack(side=tk.LEFT, padx=5)

# Botón Actualizar
btn_actualizar = tk.Button(
    frame_botones,
    text="Actualizar",
    bg="#2196F3",
    fg="white",
    width=12,
    command=actualizar_puertos
)
btn_actualizar.pack(side=tk.LEFT, padx=5)

# Etiqueta y caja de texto para potenciómetro
label_pot = tk.Label(
    ventana,
    text="Valor de potenciómetro",
    bg="#D9D9D9",
    fg="#003366"
)
label_pot.pack()

entry_pot = tk.Entry(
    ventana,
    width=25
)
entry_pot.pack(pady=2)

# Etiqueta y caja de texto para ultrasónico
label_ultra = tk.Label(
    ventana,
    text="Valor de ultrasónico",
    bg="#D9D9D9",
    fg="#003366"
)
label_ultra.pack()

entry_ultra = tk.Entry(
    ventana,
    width=25
)
entry_ultra.pack(pady=2)

# Cargar puertos disponibles al iniciar
actualizar_puertos()

ventana.mainloop()