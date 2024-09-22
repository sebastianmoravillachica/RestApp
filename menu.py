import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar, Label

def obtener_menu():
    return {
        "bebidas": [
            "Agua",
            "Refresco",
            "Cerveza"
        ],
        "comidas": [
            "Pizza",
            "Ensalada",
            "Pasta"
        ],
        "acompañamientos": [
            "Papas fritas",
            "Arroz",
            "Verduras"
        ]
    }

def mostrar_menu(root):
    menu = obtener_menu()

    # Crear un nuevo frame para el menú
    frame_menu = Frame(root)
    frame_menu.pack(pady=20)

    # Crear un canvas para las scrollbars
    canvas = Canvas(frame_menu)
    scrollbar_y = Scrollbar(frame_menu, orient="vertical", command=canvas.yview)
    scrollbar_y.pack(side="right", fill="y")

    menu_frame = Frame(canvas)
    canvas.create_window((0, 0), window=menu_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.config(yscrollcommand=scrollbar_y.set)

    # Título del menú
    Label(menu_frame, text="Menú de Comidas", font=("Arial", 16)).grid(row=0, columnspan=2)

    # Agregar bebidas
    Label(menu_frame, text="Bebidas", font=("Arial", 14)).grid(row=1, columnspan=2)
    for i, bebida in enumerate(menu["bebidas"], start=2):
        Label(menu_frame, text=f"{i - 1}. {bebida}").grid(row=i, column=0, sticky="w")

    # Agregar comidas
    Label(menu_frame, text="Comidas", font=("Arial", 14)).grid(row=len(menu["bebidas"]) + 2, columnspan=2)
    for i, comida in enumerate(menu["comidas"], start=len(menu["bebidas"]) + 3):
        Label(menu_frame, text=f"{i - len(menu['bebidas']) - 2}. {comida}").grid(row=i, column=0, sticky="w")

    # Agregar acompañamientos
    Label(menu_frame, text="Acompañamientos", font=("Arial", 14)).grid(row=len(menu["bebidas"]) + len(menu["comidas"]) + 3, columnspan=2)
    for i, acompanamiento in enumerate(menu["acompañamientos"], start=len(menu["bebidas"]) + len(menu["comidas"]) + 4):
        Label(menu_frame, text=f"{i - len(menu['bebidas']) - len(menu['comidas']) - 3}. {acompanamiento}").grid(row=i, column=0, sticky="w")

    # Actualizar la vista del canvas
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    menu_frame.bind("<Configure>", on_frame_configure)

    return frame_menu  # Retornar el frame para poder ocultarlo o mostrarlo según sea necesario
