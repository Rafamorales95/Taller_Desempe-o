import tkinter as tk
from tkinter import ttk, messagebox

# Sistema Kanban Médico con Listbox
class KanbanMedico:
    def __init__(self):
        self.pacientes_entrada = []
        self.pacientes_revision = []
        self.pacientes_tratamiento = []
        self.pacientes_dados_de_alta = []

    def agregar_paciente(self, nombre):
        if nombre:
            self.pacientes_entrada.append(nombre)
            return f"Paciente '{nombre}' agregado a la lista de entrada."
        else:
            return "Error: El nombre no puede estar vacío."

    def mover_a_revision(self, nombre):
        if nombre in self.pacientes_entrada:
            self.pacientes_entrada.remove(nombre)
            self.pacientes_revision.append(nombre)
            return f"Paciente '{nombre}' movido a revisión."
        return f"Paciente '{nombre}' no encontrado en la lista de entrada."

    def mover_a_tratamiento(self, nombre):
        if nombre in self.pacientes_revision:
            self.pacientes_revision.remove(nombre)
            self.pacientes_tratamiento.append(nombre)
            return f"Paciente '{nombre}' movido a tratamiento."
        return f"Paciente '{nombre}' no encontrado en la lista de revisión."

    def dar_de_alta(self, nombre):
        if nombre in self.pacientes_tratamiento:
            self.pacientes_tratamiento.remove(nombre)
            self.pacientes_dados_de_alta.append(nombre)
            return f"Paciente '{nombre}' dado de alta."
        return f"Paciente '{nombre}' no encontrado en la lista de tratamiento."


# Interfaz gráfica con Listbox para guardar y mover pacientes
class KanbanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paciente En Lista De Pendiente")
        self.kanban = KanbanMedico()

        # Configurar el estilo de ttk
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#007BFF", foreground="purple", font=("Arial", 12))
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))
        style.configure("TFrame", background="#F0F0F0")

        # Crear el frame principal
        main_frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
        main_frame.pack(fill="both", expand=True)

        # Crear widgets de la interfaz
        self.label = ttk.Label(main_frame, text="Nombre del paciente:")
        self.label.grid(column=0, row=0, sticky="W", padx=10, pady=10)

        self.nombre_entry = ttk.Entry(main_frame, width=30)
        self.nombre_entry.grid(column=1, row=0, sticky="W", padx=10, pady=10)

        self.agregar_btn = ttk.Button(main_frame, text="Agregar Paciente", command=self.agregar_paciente)
        self.agregar_btn.grid(column=0, row=1, padx=10, pady=10)

        # Crear Listbox para cada área
        self.entrada_listbox = tk.Listbox(main_frame, height=8, width=20)
        self.entrada_listbox.grid(column=0, row=2, padx=10, pady=10)
        self.revision_listbox = tk.Listbox(main_frame, height=8, width=20)
        self.revision_listbox.grid(column=1, row=2, padx=10, pady=10)
        self.tratamiento_listbox = tk.Listbox(main_frame, height=8, width=20)
        self.tratamiento_listbox.grid(column=2, row=2, padx=10, pady=10)
        self.alta_listbox = tk.Listbox(main_frame, height=8, width=20)
        self.alta_listbox.grid(column=3, row=2, padx=10, pady=10)

        # Etiquetas para cada Listbox
        self.entrada_label = ttk.Label(main_frame, text="Entrada", font=("Arial", 10, "bold"))
        self.entrada_label.grid(column=0, row=3)
        self.revision_label = ttk.Label(main_frame, text="Revisión", font=("Arial", 10, "bold"))
        self.revision_label.grid(column=1, row=3)
        self.tratamiento_label = ttk.Label(main_frame, text="Tratamiento", font=("Arial", 10, "bold"))
        self.tratamiento_label.grid(column=2, row=3)
        self.alta_label = ttk.Label(main_frame, text="Alta", font=("Arial", 10, "bold"))
        self.alta_label.grid(column=3, row=3)

        # Botones para mover pacientes entre áreas
        self.revision_btn = ttk.Button(main_frame, text="Mover a Revisión", command=self.mover_a_revision)
        self.revision_btn.grid(column=1, row=4, padx=10, pady=10)

        self.tratamiento_btn = ttk.Button(main_frame, text="Mover a Tratamiento", command=self.mover_a_tratamiento)
        self.tratamiento_btn.grid(column=2, row=4, padx=10, pady=10)

        self.alta_btn = ttk.Button(main_frame, text="Dar de Alta", command=self.dar_de_alta)
        self.alta_btn.grid(column=3, row=4, padx=10, pady=10)

        # Estilo para el fondo de la ventana
        self.root.configure(bg="#F0F0F0")

    # Funciones que interactúan con el sistema Kanban
    def agregar_paciente(self):
        nombre = self.nombre_entry.get()
        resultado = self.kanban.agregar_paciente(nombre)
        if resultado:
            self.entrada_listbox.insert(tk.END, nombre)
        self.nombre_entry.delete(0, tk.END)

    def mover_a_revision(self):
        seleccion = self.entrada_listbox.curselection()
        if seleccion:
            nombre = self.entrada_listbox.get(seleccion)
            self.kanban.mover_a_revision(nombre)
            self.entrada_listbox.delete(seleccion)
            self.revision_listbox.insert(tk.END, nombre)

    def mover_a_tratamiento(self):
        seleccion = self.revision_listbox.curselection()
        if seleccion:
            nombre = self.revision_listbox.get(seleccion)
            self.kanban.mover_a_tratamiento(nombre)
            self.revision_listbox.delete(seleccion)
            self.tratamiento_listbox.insert(tk.END, nombre)

    def dar_de_alta(self):
        seleccion = self.tratamiento_listbox.curselection()
        if seleccion:
            nombre = self.tratamiento_listbox.get(seleccion)
            self.kanban.dar_de_alta(nombre)
            self.tratamiento_listbox.delete(seleccion)
            self.alta_listbox.insert(tk.END, nombre)


# Función principal
def main():
    root = tk.Tk()
    root.geometry("800x400")  # Tamaño de la ventana
    app = KanbanApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
