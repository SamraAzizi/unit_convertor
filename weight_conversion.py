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
        
