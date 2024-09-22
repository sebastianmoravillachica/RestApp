import tkinter as tk
from tkinter import messagebox
from database import connect_to_db
from menu import mostrar_menu  # Importar la función para mostrar el menú

def registrar_usuario():
    nombre = entry_registro_nombre.get()
    apellidos = entry_registro_apellidos.get()
    email = entry_registro_email.get()
    password = entry_registro_password.get()

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (?, ?, ?, ?)",
                            (nombre, apellidos, email, password))
            conn.commit()
            messagebox.showinfo("Registro Exitoso", "¡Usuario registrado con éxito!")
            mostrar_login()  # Regresar a la pantalla de login
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar usuario: {e}")
        finally:
            cursor.close()
            conn.close()

def login_usuario():
    email = entry_login_email.get()
    password = entry_login_password.get()

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT nombre FROM usuarios WHERE email = ? AND password = ?", (email, password))
            user = cursor.fetchone()
            if user:
                messagebox.showinfo("Bienvenido", f"Bienvenido, {user[0]}!")
                frame_login.pack_forget()  # Ocultar el frame de login
                mostrar_menu(root)  # Mostrar el menú después de iniciar sesión
            else:
                messagebox.showwarning("Error", "Credenciales incorrectas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al iniciar sesión: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_registro():
    frame_login.pack_forget()  # Ocultar el frame de login
    frame_registro.pack(pady=20)  # Mostrar el frame de registro

def mostrar_login():
    frame_registro.pack_forget()  # Ocultar el frame de registro
    frame_login.pack(pady=20)  # Mostrar el frame de login

# Crear la ventana principal
root = tk.Tk()
root.title("Registro y Login")

# Frame de Registro
frame_registro = tk.Frame(root)

tk.Label(frame_registro, text="Registro de Usuario", font=("Arial", 16)).grid(row=0, columnspan=2)

tk.Label(frame_registro, text="Nombre:").grid(row=1, column=0)
entry_registro_nombre = tk.Entry(frame_registro)
entry_registro_nombre.grid(row=1, column=1)

tk.Label(frame_registro, text="Apellidos:").grid(row=2, column=0)
entry_registro_apellidos = tk.Entry(frame_registro)
entry_registro_apellidos.grid(row=2, column=1)

tk.Label(frame_registro, text="Email:").grid(row=3, column=0)
entry_registro_email = tk.Entry(frame_registro)
entry_registro_email.grid(row=3, column=1)

tk.Label(frame_registro, text="Contraseña:").grid(row=4, column=0)
entry_registro_password = tk.Entry(frame_registro, show="*")
entry_registro_password.grid(row=4, column=1)

tk.Button(frame_registro, text="Registrarse", command=registrar_usuario).grid(row=5, columnspan=2)
tk.Button(frame_registro, text="Volver a Iniciar Sesión", command=mostrar_login).grid(row=6, columnspan=2)

# Frame de Login
frame_login = tk.Frame(root)

tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 16)).grid(row=0, columnspan=2)

tk.Label(frame_login, text="Email:").grid(row=1, column=0)
entry_login_email = tk.Entry(frame_login)
entry_login_email.grid(row=1, column=1)

tk.Label(frame_login, text="Contraseña:").grid(row=2, column=0)
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.grid(row=2, column=1)

tk.Button(frame_login, text="Iniciar Sesión", command=login_usuario).grid(row=3, columnspan=2)
tk.Button(frame_login, text="Registrar", command=mostrar_registro).grid(row=4, columnspan=2)

# Mostrar el frame de inicio de sesión por defecto
mostrar_login()

root.mainloop()
