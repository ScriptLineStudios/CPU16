import sys

from virtual_machine import VirtualMachine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [FILE_TO_LOAD].hex")
        exit(1)
    
    virtual_cpu = VirtualMachine()
    virtual_cpu.load_program(sys.argv[1])
    virtual_cpu.start_clock()