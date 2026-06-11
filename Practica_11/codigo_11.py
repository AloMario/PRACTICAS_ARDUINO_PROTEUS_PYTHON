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


# Función para leer datos del puerto serial
def leer_datos():
    global conexion
    try:
        if conexion is not None and conexion.is_open:
            if conexion.in_waiting > 0:
                trama = conexion.readline().decode('utf-8').strip()

                # Mostrar la trama en la consola de VS Code
                print(trama)
                datos = trama.split(",")
                if len(datos) == 4:
                    valor_pot = datos[1]
                    valor_distancia = datos[3]

                    # Actualizar caja de texto del potenciómetro
                    entry_pot.delete(0, tk.END)
                    entry_pot.insert(0, valor_pot)

                    # Actualizar caja de texto del ultrasónico
                    entry_ultra.delete(0, tk.END)
                    entry_ultra.insert(0, valor_distancia)

    except Exception as e:
        print("Error:", e)

    ventana.after(100, leer_datos)


# Función para conectar o desconectar
def conectar_desconectar():
    global conexion
    # Desconectar
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


# ======================================
# Ventana principal
# ======================================

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

# ComboBox de puertos COM
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

# Botón conectar/desconectar
btn_conectar = tk.Button(
    frame_botones,
    text="Conectar",
    bg="#4CAF50",
    fg="white",
    width=12,
    command=conectar_desconectar
)
btn_conectar.pack(side=tk.LEFT, padx=5)

# Botón actualizar puertos
btn_actualizar = tk.Button(
    frame_botones,
    text="Actualizar",
    bg="#2196F3",
    fg="white",
    width=12,
    command=actualizar_puertos
)
btn_actualizar.pack(side=tk.LEFT, padx=5)

# Etiqueta y caja de texto del potenciómetro
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

# Etiqueta y caja de texto del ultrasónico
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

# Cargar puertos disponibles
actualizar_puertos()

# Iniciar lectura periódica del puerto serial
leer_datos()

ventana.mainloop()