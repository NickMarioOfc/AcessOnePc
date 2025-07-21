import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import time

def tocar_musica( ):
    pygame.mixer.init( )
    caminho_musica = "C:\\Users\\BRUNA & LARISSA\\Desktop\\comandos\\dj.mp3"
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play( )

    while pygame.mixer.music.get_busy( ):
        time.sleep(1)

def verificar_login( ):
    usuario = entry_usuario.get( )
    senha = entry_senha.get( )

    if usuario == "nick" and senha == "14112025!":
        messagebox.showinfo("Login","Acesso concedido!")
        tocar_musica( )
    else:
        messagebox.showerror("Login","Usuário ou senha incorretos.")

janela = tk.Tk( )
janela.title("Tela de Login")
janela.attributes("-fullscreen", True)
janela.configure(bg="#1e1e1e")

frame = tk.Frame(janela, bg="#1e1e1e")
frame.pack(expand=True)

tk.Label(frame, text="Usuário:",
font=("Arial", 14), fg="white",
bg="#1e1e1e").pack(pady=5)
entry_usuario = tk.Entry(frame,
font=("Arial", 14), fg="black")
entry_usuario.pack(pady=5)

tk.Label(frame, text="Senha:",
font=("Arial", 14), fg="white",
bg="#1e1e1e").pack(pady=5)
entry_senha = tk.Entry(frame,
font=("Arial", 14), width=30, show="*")
entry_senha.pack(pady=5)

tk.Label(frame, text="Simulação de acessar PC (segundo programa)", font=("Arial", 12), fg="gray", bg="#1e1e1e").pack(pady=10)

btn_login = tk.Button(frame, text="Entrar",
font=("Arial", 14),
command=verificar_login)
btn_login.pack(pady=15)

janela.mainloop()