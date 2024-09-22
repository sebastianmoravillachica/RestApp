import tkinter as tk
from tkinter import messagebox
from database import connect_to_db

def registrar_usuario():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    email = entry_email.get()
    password = entry_password.get()

    if verificar_email(email):
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (?, ?, ?, ?)",
                               (nombre, apellidos, email, password))
                conn.commit()
                messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
                mostrar_login()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar usuario: {e}")
            finally:
                cursor.close()
                conn.close()
    else:
        messagebox.showwarning("Advertencia", "El email ya está registrado.")

def verificar_email(email):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = ?", (email,))
            count = cursor.fetchone()[0]
            return count == 0  # Devuelve True si el email no existe
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar el email: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    return False

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
            else:
                messagebox.showwarning("Error", "Credenciales incorrectas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al iniciar sesión: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_registro():
    frame_login.pack_forget()
    frame_registro.pack(pady=20)

def mostrar_login():
    frame_registro.pack_forget()
    frame_login.pack(pady=20)

# Crear la ventana principal
root = tk.Tk()
root.title("Registro y Login")

# Frame de Registro
frame_registro = tk.Frame(root)

tk.Label(frame_registro, text="Registro").grid(row=0, columnspan=2)

tk.Label(frame_registro, text="Nombre:").grid(row=1, column=0)
entry_nombre = tk.Entry(frame_registro)
entry_nombre.grid(row=1, column=1)

tk.Label(frame_registro, text="Apellidos:").grid(row=2, column=0)
entry_apellidos = tk.Entry(frame_registro)
entry_apellidos.grid(row=2, column=1)

tk.Label(frame_registro, text="Email:").grid(row=3, column=0)
entry_email = tk.Entry(frame_registro)
entry_email.grid(row=3, column=1)

tk.Label(frame_registro, text="Contraseña:").grid(row=4, column=0)
entry_password = tk.Entry(frame_registro, show="*")
entry_password.grid(row=4, column=1)

tk.Button(frame_registro, text="Registrar", command=registrar_usuario).grid(row=5, columnspan=2)

# Frame de Login
frame_login = tk.Frame(root)

tk.Label(frame_login, text="Login").grid(row=0, columnspan=2)

tk.Label(frame_login, text="Email:").grid(row=1, column=0)
entry_login_email = tk.Entry(frame_login)
entry_login_email.grid(row=1, column=1)

tk.Label(frame_login, text="Contraseña:").grid(row=2, column=0)
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.grid(row=2, column=1)

tk.Button(frame_login, text="Iniciar Sesión", command=login_usuario).grid(row=3, columnspan=2)

# Frame de selección
frame_selection = tk.Frame(root)
frame_selection.pack(pady=20)

tk.Label(frame_selection, text="¿Ya tienes una cuenta?").grid(row=0, columnspan=2)
tk.Button(frame_selection, text="Iniciar Sesión", command=mostrar_login).grid(row=1, column=0)
tk.Button(frame_selection, text="Registrar", command=mostrar_registro).grid(row=1, column=1)

root.mainloop()
