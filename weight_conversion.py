import tkinter as tk
from tkinter import ttk

class WeightConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Converter")
        
        self.conversion_mode = tk.StringVar()
        self.conversion_mode.set("kg_to_lb")  # Default conversion mode
        
        self.weight_label = ttk.Label(root, text="Enter weight:")
        self.weight_label.grid(row=0, column=0)
        
        self.weight_entry = ttk.Entry(root, width=10)
        self.weight_entry.grid(row=0, column=1)
        
        self.unit_label = ttk.Label(root, text="kg")
        self.unit_label.grid(row=0, column=2)
        
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_weight)
        self.convert_button.grid(row=1, columnspan=3)
        
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=2, columnspan=3)
        
        self.radio_kg_to_lb = ttk.Radiobutton(root, text="kg to lb", variable=self.conversion_mode, value="kg_to_lb")
        self.radio_kg_to_lb.grid(row=3, column=0)
        
        self.radio_lb_to_kg = ttk.Radiobutton(root, text="lb to kg", variable=self.conversion_mode, value="lb_to_kg")
        self.radio_lb_to_kg.grid(row=3, column=1)
        
        self.radio_kg_to_g = ttk.Radiobutton(root, text="kg to g", variable=self.conversion_mode, value="kg_to_g")
        self.radio_kg_to_g.grid(row=3, column=2)
        
        self.radio_g_to_kg = ttk.Radiobutton(root, text="g to kg", variable=self.conversion_mode, value="g_to_kg")
        self.radio_g_to_kg.grid(row=3, column=3)

        self.root.geometry("300x200")  # Set window size to 300x200 pixels


