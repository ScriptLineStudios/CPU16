import sys

from virtual_machine import VirtualMachine
from devices.graphics import GraphicsCard

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [FILE_TO_LOAD].hex")
        exit(1)
    
    graphics_card = GraphicsCard()

    virtual_cpu = VirtualMachine()
    virtual_cpu.attach(graphics_card)
    virtual_cpu.load_program(sys.argv[1])
    virtual_cpu.start_clock()