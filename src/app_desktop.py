import tkinter as tk
from tkinter import messagebox, ttk
# Importamos el motor analítico desde tu validator.py
from validator import evaluar_transaccion


def ejecutar_auditoria():
    # 1. Recuperar datos de la interfaz
    id_cliente = entry_id.get().strip()
    monto_str = entry_monto.get().strip()
    cant_fallidas = entry_fallidas.get().strip()
    risk_score = entry_risk.get().strip()

    if not id_cliente or not monto_str or not cant_fallidas or not risk_score:
        messagebox.showerror(
            "Campos Vacíos", "Por favor, complete todos los campos.")
        return

    try:
        monto = float(monto_str)

        # Regla de negocio básica para el monto
        if monto <= 0:
            messagebox.showerror(
                "Monto Inválido", "El monto debe ser mayor a $0.00.")
            return

        if monto > 50000:
            lbl_resultado.config(
                text=f"RECHAZADA POR POLÍTICA (ID: {id_cliente})", fg="#FFFFFF")
            lbl_motivo.config(
                text=f"Monto de ${monto:,.2f} excede el límite automático ($50,000).\nRequiere auditoría manual por prevención de lavado de dinero.", fg="#FFCDD2")
            frame_resultado.config(bg="#B71C1C")
            return

        # 2. LLAMADA AL MOTOR DE IA (validator.py)
        respuesta = evaluar_transaccion(cant_fallidas, risk_score)

        # 3. Pintar la interfaz según la respuesta del modelo
        if respuesta["codigo"] == 1:  # RECHAZADA por el árbol
            lbl_resultado.config(
                text=f"TRANSACCIÓN RECHAZADA (ID: {id_cliente})", fg="#D32F2F")
            lbl_motivo.config(text=respuesta["motivo"], fg="#721C24")
            frame_resultado.config(bg="#F8D7DA")

        elif respuesta["codigo"] == 0:  # APROBADA por el árbol
            lbl_resultado.config(
                text=f"TRANSACCIÓN APROBADA (ID: {id_cliente})", fg="#388E3C")
            lbl_motivo.config(
                text=f"Operación autorizada por ${monto:,.2f}. {respuesta['motivo']}", fg="#155724")
            frame_resultado.config(bg="#D4EDDA")

        else:  # Error de rutas o datos dentro de validator.py
            messagebox.showerror("Error en Motor", respuesta["motivo"])

    except ValueError:
        messagebox.showerror("Error de Formato",
                             "Monto, fallas y score deben ser numéricos.")


# --- DISEÑO TKINTER ---
ventana = tk.Tk()
ventana.title("SentryBank v1.2 - Core Gateway Desktop")
ventana.geometry("540x520")
ventana.configure(bg="#F3F4F6")

lbl_titulo = tk.Label(ventana, text="SentryBank™ Desktop Validator", font=(
    "Segoe UI", 15, "bold"), bg="#F3F4F6", fg="#1E3A8A")
lbl_titulo.pack(pady=15)

# Panel de datos simulados
frame_gen = tk.LabelFrame(ventana, text=" 1. Datos Financieros (Filtros Core) ",
                          bg="#F3F4F6", fg="#1E40AF", font=("Segoe UI", 9, "bold"), padx=15, pady=8)
frame_gen.pack(pady=5, fill="x", padx=25)

tk.Label(frame_gen, text="ID Cliente:", bg="#F3F4F6").grid(
    row=0, column=0, sticky="w", pady=2)
entry_id = tk.Entry(frame_gen, width=12)
entry_id.grid(row=0, column=1, padx=5)
entry_id.insert(0, "CLI-9948")

tk.Label(frame_gen, text="Monto ($):", bg="#F3F4F6").grid(
    row=0, column=2, sticky="w", padx=10)
entry_monto = tk.Entry(frame_gen, width=12)
entry_monto.grid(row=0, column=3)
entry_monto.insert(0, "150.00")

# Panel de variables reales del modelo
frame_inputs = tk.LabelFrame(ventana, text=" 2. Variables Analíticas (Modelo IA) ",
                             bg="#F3F4F6", fg="#1E40AF", font=("Segoe UI", 9, "bold"), padx=15, pady=8)
frame_inputs.pack(pady=10, fill="x", padx=25)

tk.Label(frame_inputs, text="Transacciones Fallidas (7d):",
         bg="#F3F4F6").grid(row=0, column=0, sticky="w", pady=4)
entry_fallidas = tk.Entry(frame_inputs, width=8, justify="center")
entry_fallidas.grid(row=0, column=1, padx=10)
entry_fallidas.insert(0, "0")

tk.Label(frame_inputs, text="Puntaje de Riesgo (0.0 - 1.0):",
         bg="#F3F4F6").grid(row=1, column=0, sticky="w", pady=4)
entry_risk = tk.Entry(frame_inputs, width=8, justify="center")
entry_risk.grid(row=1, column=1, padx=10)
entry_risk.insert(0, "0.0")

# Botón
btn_evaluar = tk.Button(ventana, text="AUDITAR OPERACIÓN", font=(
    "Segoe UI", 10, "bold"), bg="#1E3A8A", fg="white", bd=0, padx=15, pady=6, command=ejecutar_auditoria)
btn_evaluar.pack(pady=15)

# Consola de Resultados
frame_resultado = tk.Frame(ventana, bg="#E5E7EB",
                           bd=1, relief="solid", padx=15, pady=10)
frame_resultado.pack(pady=5, fill="x", padx=25)

lbl_resultado = tk.Label(frame_resultado, text="SISTEMA EN ESPERA", font=(
    "Segoe UI", 10, "bold"), bg="#E5E7EB", fg="#374151")
lbl_resultado.pack()
lbl_motivo = tk.Label(frame_resultado, text="Haga clic en Auditar para procesar los datos con el Árbol de Decisión.", font=(
    "Segoe UI", 9, "italic"), bg="#E5E7EB", fg="#6B7280")
lbl_motivo.pack(pady=2)

ventana.mainloop()
