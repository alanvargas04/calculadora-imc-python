import tkinter as tk
from tkinter import ttk

# Função para calcular o IMC
def calcular_imc():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    imc = peso / (altura ** 2)
    resultado_label.config(text = f"Seu IMC é: {imc:.2f}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Define um estilo
style = ttk.Style()
style.configure("TButton", font=("Arial", 20), background="yellow")
style.configure("TLabel", font=("Arial", 20), background="yellow")
style.configure("TEntry", font=("Arial", 20))

# Cria os elementos da interface
peso_label = ttk.Label(janela, text="Digite seu peso em kg:")
peso_entry = ttk.Entry(janela)
altura_label = ttk.Label(janela, text="Digite sua altura em metros:")
altura_entry = ttk.Entry(janela)
calcular_button = ttk.Button(janela, text="Calcular", command=calcular_imc)
resultado_label = ttk.Label(janela, text="")

# Adiciona os elementos na janela
peso_label.pack(pady=10)
peso_entry.pack(pady=10)
altura_label.pack(pady=10)
altura_entry.pack(pady=10)
calcular_button.pack(pady=10)
resultado_label.pack(pady=10)

# Inicia a interface gráfica
janela.mainloop()
