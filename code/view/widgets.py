import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Widgets:
  
    def __init__(self, view, frame):
        self.view = view
        self._create_widgets(frame)
        
    def _create_widgets(self, frame):
        frame_func_label = tk.Frame(frame, bg="gray94")
        frame_func_label.place(relheight=0.15, relwidth=0.288, relx=0.02, rely=0.025)
        self._create_latex_texts(frame_func_label)
        
        frame_parameters = tk.LabelFrame(frame, bg="gray94", text="Parameters")
        frame_parameters.place(relheight=0.25, relwidth=0.29, relx=0.02, rely=0.2)
        self._create_parameter_entries(frame_parameters)
        
        frame_algorithm = tk.LabelFrame(frame, bg="gray94", text="Algorithm")
        frame_algorithm.place(relheight=0.4, relwidth=0.29, relx=0.02, rely=0.47)
                               
        frame_algorithm_radio = tk.Frame(frame_algorithm, bg="gray94")
        frame_algorithm_radio.place(relheight=0.45, relwidth=1, relx=0.0, rely=0.0)                     
        self._create_algorithm_buttons(frame_algorithm_radio)
        
        frame_algorithm_parameters = tk.Frame(frame_algorithm, bg="gray94")
        frame_algorithm_parameters.place(relheight=0.5, relwidth=1, relx=0.0, rely=0.45)
        self._create_algorithm_parameter_entries(frame_algorithm_parameters)

        frame_buttons = tk.Frame(frame, bg="gray94")
        frame_buttons.place(relheight=0.1, relwidth=0.29, relx=0.02, rely=0.9)
        self._create_buttons(frame_buttons)

        frame_results = tk.LabelFrame(frame, bg="gray94", text="Results")  
        frame_results.place(relheight=0.15, relwidth=0.65, relx=0.33, rely=0.02)
        self._create_results_labels(frame_results)
        
        frame_ax = tk.Frame(frame)
        frame_ax.place(relheight=0.75, relwidth=0.65, relx=0.33, rely=0.2)
        self._create_ax(frame_ax)
    
    def _create_ax(self, master):
        fig = plt.figure()
        self.view.ax = fig.add_subplot(111)
        self.view._create_ax()
        self.view.canvas = FigureCanvasTkAgg(fig, master)
        self.view.canvas.get_tk_widget().pack(fill=tk.BOTH)
        self.view.canvas.draw()
        
    def _create_results_labels(self, master):
        frame_l = tk.Frame(master)
        frame_l.place(relheight=0.9, relwidth=0.2, relx=0.0, rely=0.08)
        
        l_x_star = tk.Label(frame_l, text="x* = ", font=12)
        l_x_star.pack(expand=1, anchor=tk.NE)
        
        l_f_x_star = tk.Label(frame_l, text="f* = ", font=12)
        l_f_x_star.pack(expand=1, anchor=tk.NE)
        
        frame_labels = tk.Frame(master)
        frame_labels.place(relheight=0.9, relwidth=0.2, relx=0.2, rely=0.08)
        
        self.view.label_x_star = tk.Label(frame_labels, text="_", font=12)
        self.view.label_x_star.pack(expand=1, anchor=tk.NW)
        
        self.view.label_f_x_star = tk.Label(frame_labels, text="_", font=12)
        self.view.label_f_x_star.pack(expand=1, anchor=tk.NW)
        
        frame_l = tk.Frame(master)
        frame_l.place(relheight=0.9, relwidth=0.4, relx=0.4, rely=0.08)
        
        l_n_steps = tk.Label(frame_l, text="Number of steps = ", font=12)
        l_n_steps.pack(expand=1, anchor=tk.NE)
        
        l_eps = tk.Label(frame_l, text="Achieved accuracy = ", font=12)
        l_eps.pack(expand=1, anchor=tk.NE)
        
        frame_labels = tk.Frame(master)
        frame_labels.place(relheight=0.9, relwidth=0.2, relx=0.8, rely=0.08)
        
        self.view.label_n_steps = tk.Label(frame_labels, text="_", font=12)
        self.view.label_n_steps.pack(expand=1, anchor=tk.NW)
         
        self.view.label_eps = tk.Label(frame_labels, text="_", font=12)
        self.view.label_eps.pack(expand=1, anchor=tk.NW)
    
    def _create_buttons(self, master):       
        self.view.button_start = tk.Button(master, text="Start", font=15, bg="white",
                                 command=self.view._click_button_start)
        self.view.button_start.place(relwidth=0.3, relx=0.0)
        
        self.view.button_stop = tk.Button(master, text="Stop", font=15, bg="white",
                                command=self.view._click_button_stop, state=tk.DISABLED)
        self.view.button_stop.place(relwidth=0.3, relx=0.33)
        
        self.view.button_show = tk.Button(master, text="Show", font=15, bg="white",
                                command=self.view._click_show_result, state=tk.DISABLED)
        self.view.button_show.place(relwidth=0.3, relx=0.66)

    def _create_algorithm_parameter_entries(self, master):
        self.view.var_n_steps = tk.StringVar()
        self.view.var_eps = tk.StringVar()
        self.view.var_r = tk.StringVar()
        
        frame_labels = tk.Frame(master)
        frame_labels.place(relheight=0.9, relwidth=0.6, relx=0.0, rely=0.08)
        
        l_n_steps = tk.Label(frame_labels, text="Max number of steps = ", font=12)
        l_n_steps.pack(expand=1, anchor=tk.NE)
        
        l_eps = tk.Label(frame_labels, text="Accuracy = ", font=12)
        l_eps.pack(expand=1, anchor=tk.NE)
        
        l_r = tk.Label(frame_labels, text="r = ", font=12)
        l_r.pack(expand=1, anchor=tk.NE)
        
        frame_entries = tk.Frame(master)
        frame_entries.place(relheight=0.9, relwidth=0.35, relx=0.6, rely=0.08)
        
        entry_n_steps = tk.Entry(frame_entries, textvariable=self.view.var_n_steps, font=15)
        entry_n_steps.pack(expand=1, anchor=tk.NW)           
        
        entry_eps = tk.Entry(frame_entries, textvariable=self.view.var_eps, font=15)
        entry_eps.pack(expand=1, anchor=tk.NW)
        
        entry_r = tk.Entry(frame_entries, textvariable=self.view.var_r, font=15)
        entry_r.pack(expand=1, anchor=tk.NW)

    def _create_algorithm_buttons(self, master):
        self.view.var_algorithm = tk.StringVar()
        self.view.var_algorithm.set("Brute force")
            
        radio_brute_force = tk.Radiobutton(master, text="Brute force", font=15,
                                           variable=self.view.var_algorithm,
                                           value="Brute force")
        radio_brute_force.place(relx=0.15, rely=0.03)
        
        radio_piavsky = tk.Radiobutton(master, text="Piyavsky’s algorithm", font=15,
                                       variable=self.view.var_algorithm,
                                       value="Piyavsky’s algorithm")
        radio_piavsky.place(relx=0.15, rely=0.33)
        
        radio_strongin = tk.Radiobutton(master, text="Strongin's algorithm", font=15,
                                        variable=self.view.var_algorithm,
                                        value="Strongin's algorithm")
        radio_strongin.place(relx=0.15, rely=0.63)      
    
    def _create_latex_texts(self, master):
        fig = plt.figure(figsize=(1, 1))
        ax = fig.add_subplot(111)
        ax.text(-0.1, 0.7, r"$f(x)=a\cdot\sin{(bx)}+c\cdot\cos{(dx)}$", fontsize = 13)
        ax.text(-0.1, 0.2, r"$f^*=f(x^*)=\min_{x\in[x_1, x_2]} f(x)$", fontsize = 13)
        plt.axis('off')
        canvas = FigureCanvasTkAgg(fig, master)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
    
    def _create_parameter_entries(self, master):
        self.view.var_a = tk.StringVar()
        self.view.var_b = tk.StringVar()
        self.view.var_c = tk.StringVar()
        self.view.var_d = tk.StringVar()
        self.view.var_x1 = tk.StringVar()
        self.view.var_x2 = tk.StringVar()
        
        l_a = tk.Label(master, text="a = ", font=12)
        l_a.place(relheight=0.2, relwidth=0.15, relx=0.02, rely=0.08)
        entry_a = tk.Entry(master, textvariable=self.view.var_a, font=15)
        entry_a.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.08)
        
        l_b = tk.Label(master, text="b = ", font=12)
        l_b.place(relheight=0.2, relwidth=0.15, relx=0.50, rely=0.08)
        entry_b = tk.Entry(master, textvariable=self.view.var_b, font=15)
        entry_b.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.08)
        
        l_c = tk.Label(master, text="c = ", font=12)
        l_c.place(relheight=0.2, relwidth=0.15, relx=0.02, rely=0.38)
        entry_c = tk.Entry(master, textvariable=self.view.var_c, font=15)
        entry_c.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.38)
        
        l_d = tk.Label(master, text="d = ", font=12)
        l_d.place(relheight=0.2, relwidth=0.15, relx=0.50, rely=0.38)
        entry_d = tk.Entry(master, textvariable=self.view.var_d, font=15)
        entry_d.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.38)
        
        l_x1 = tk.Label(master, text="x1 = ", font=12)
        l_x1.place(relheight=0.2, relwidth=0.15, relx=0.009, rely=0.68)
        entry_x1 = tk.Entry(master, textvariable=self.view.var_x1, font=15)
        entry_x1.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.68)
        
        l_x2 = tk.Label(master, text="x2 = ", font=12)
        l_x2.place(relheight=0.2, relwidth=0.15, relx=0.489, rely=0.68)
        entry_x2 = tk.Entry(master, textvariable=self.view.var_x2, font=15)
        entry_x2.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.68)
