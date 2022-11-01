chars = {
        "drawchara": [f"movb 2+&", 
                        f"outb", 
                        f"movb 34+&", 
                        f"outb"
                        ,f"movb 66+&"
                        ,f"outb"
                        ,f"movb 67+&"
                        ,f"outb"
                        ,f"movb 68+&"
                        ,f"outb"
                        ,f"movb 98+&"
                        ,f"outb"
                        ,f"movb 3+&"
                        ,f"outb"
                        ,f"movb 4+&"
                        ,f"outb"
                        ,f"movb 5+&"
                        ,f"outb"
                        ,f"movb 37+&"
                        ,f"outb"
                        ,f"movb 69+&"
                        ,f"outb"
                        ,f"movb 101+&"
                        ,f"outb"],

        "drawcharb": [f"movb 3+&",
                        f"outb", 
                        f"movb 36+&",
                        f"outb",
                        f"movb 67+&",
                        f"outb", 
                        f"movb 100+&",
                        f"outb", 
                        f"movb 131+&",
                        f"outb", 
                        f"movb 34+&", 
                        f"outb", 
                        f"movb 66+&", 
                        f"outb", 
                        f"movb 98+&", 
                        f"outb"],

        "drawcharc": [f"movb 2+&",
                        f"outb",
                        f"movb 34+&",
                        f"outb",
                        f"movb 66+&",
                        f"outb",
                        f"movb 98+&",
                        f"outb",
                        f"movb 99+&",
                        f"outb",
                        f"movb 100+&",
                        f"outb",
                        f"movb 3+&",
                        f"outb",
                        f"movb 4+&",
                        f"outb"]
}

def add_all_chars_to_macro_definitions(macros):
    for key, value in chars.items():
        macros[key] = value

    return macros