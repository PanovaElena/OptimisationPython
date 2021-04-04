import sys
sys.path.append("controller")
sys.path.append("view")
sys.path.append("model")

from controller import Controller

if __name__ == "__main__":
    cont = Controller()
    cont.run()