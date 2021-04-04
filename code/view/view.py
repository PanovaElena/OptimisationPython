import tkinter as tk
from tkinter.messagebox import showerror
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as ma
import numpy as np

from widgets import Widgets

class View:
    
    def __init__(self, controller):   
        self.controller = controller
        self._create_window()
                   
    def _create_window(self):
        window = self.controller.window  
        window.title("Optimisation")
        
        wsize = (1000, 600)
        window.geometry('%dx%d' % wsize)
        window.resizable(width=False, height=False)
        
        frame = tk.Frame(window, bg="gray94",
                         width=wsize[0], height=wsize[1])
        frame.pack()
        
        widgets = Widgets(self, frame)
        self._set_default_values()
        
    def _set_default_values(self):
        self.var_a.set(4)
        self.var_b.set(8)
        self.var_c.set(2)
        self.var_d.set(0.5)
        self.var_x1.set(0)
        self.var_x2.set(8)
        self.var_n_steps.set(100)
        self.var_eps.set(1e-8)
        self.var_r.set(2)
    
    def _get_func(self):
        try: a = float(self.var_a.get())
        except Exception: raise Exception("Variable 'a' should be float")
        
        try: b = float(self.var_b.get())
        except Exception: raise Exception("Variable 'b' should be float")
        
        try: c = float(self.var_c.get())
        except Exception: raise Exception("Variable 'c' should be float")
        
        try: d = float(self.var_d.get())
        except Exception: raise Exception("Variable 'd' should be float")
            
        def f(x):
            return a*ma.sin(b*x) + c*ma.cos(d*x) 
        return f
            
    def _get_borders(self):
        try: x1 = float(self.var_x1.get())
        except Exception: raise Exception("Variable 'x1' should be float")
        
        try: x2 = float(self.var_x2.get())
        except Exception: raise Exception("Variable x2 should be float")
        
        if x2 < x1:
            raise Exception("x2 > x1")
        return (x1, x2)

    def _get_alg(self):
        alg = self.var_algorithm.get()
        
        try: n_steps = int(self.var_n_steps.get())
        except Exception: raise Exception("Number of steps should be int")
        
        if n_steps <= 0:
            raise Exception("Number of steps should be more than 0")
        
        try: eps = float(self.var_eps.get())
        except Exception: raise Exception("Accuracy should be float")
        
        if eps <= 0:
            raise Exception("Accuracy should be more than 0")
        
        try: r = float(self.var_r.get())
        except Exception: raise Exception("Variable r should be float")
        
        if r <= 1:
            raise Exception("Variable r should be more than 1")
            
        return alg, n_steps, eps, r
        
    def _save_params(self):
        self.f = self._get_func()
        self.borders = self._get_borders()
        self.alg_params = self._get_alg()
    
    def _click_button_start(self):
        try:
            self._save_params()
            self.button_start.config(state=tk.DISABLED)
            self.button_stop.config(state=tk.NORMAL)
            self.button_show.config(state=tk.DISABLED)
            self.controller.start_model(self.f, self.borders, self.alg_params)  
        except Exception as e:
            showerror("Error", str(e))
            
    def _click_button_stop(self):
        self.cancel_calculations()
        
    def _click_show_result(self):
        self._show_result()
    
    def cancel_calculations(self):
        self.controller.stop_model()
        self.button_stop.config(state=tk.DISABLED)
        self.button_start.config(state=tk.NORMAL)
        self.button_show.config(state=tk.NORMAL)

    def _create_ax(self):
        self.ax.clear()
        self.ax.grid()
        self.ax.set_xlabel("$x$")
        self.ax.set_ylabel("$f(x)$")
        
    def _show_result(self):
        x_star, f_x_star, eps, n_steps, list_res = self.controller.result
        
        self.label_x_star.config(text="%0.7f" % x_star)
        self.label_f_x_star.config(text="%0.7f" % f_x_star)
        self.label_n_steps.config(text=str(n_steps)) 
        self.label_eps.config(text="%e" % eps)
        
        f_vec = np.vectorize(self.f)
        N = 1000
        x = np.linspace(self.borders[0], self.borders[1], N)
        self._create_ax()
        self.ax.plot(x, f_vec(x), "g")
        self.ax.plot([list_res[i][0] for i in range(len(list_res))],
                     [list_res[i][1] for i in range(len(list_res))],
                     ">r")
        self.canvas.draw()
        
        
        