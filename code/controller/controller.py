from tkinter import Tk
import threading

from view import View
from methods import BruteForce, PiyavskyMethod, StronginMethod


class Controller:

    def __init__(self):
        self.window = Tk()
        
        def on_close():
            self.window.quit()
            self.window.destroy()

        self.window.protocol('WM_DELETE_WINDOW', on_close)
        
        self.view = View(self)
        self.result = None
        self.method = None
        
    def run(self):
        self.window.mainloop()
        
    def start_model(self, f, borders, alg_params):
        alg = BruteForce if alg_params[0]=="Brute force" else \
             (PiyavskyMethod if alg_params[0]=="Piyavsky’s algorithm" \
              else StronginMethod)
    
        def run_thread():
            self.method = alg()
            self.result = self.method.compute(f, borders, alg_params[1],
                                              alg_params[2], alg_params[3])
            self.view.cancel_calculations()
            
        self.thread = threading.Thread(target=run_thread)
        self.thread.start()
        
    def stop_model(self):
        if self.method:
            self.method.set_if_cancel_computing(True)
        
    