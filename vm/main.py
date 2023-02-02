import sys

from virtual_machine import VirtualMachine
from devices.graphics import GraphicsCard
from devices.keyboard import Keyboard

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [FILE_TO_LOAD].hex")
        exit(1)
    
    graphics_card = GraphicsCard()
    keyboard = Keyboard(graphics_card.screen)

    virtual_cpu = VirtualMachine()
    virtual_cpu.attach(graphics_card)
    virtual_cpu.attach(keyboard)
    virtual_cpu.load_program(sys.argv[1])
    virtual_cpu.start_clock()