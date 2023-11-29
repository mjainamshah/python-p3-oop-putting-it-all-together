#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size
        self.condition = "New"

    def repair(self):
        self.condition = "New"
        return "The shoe has been repaired."
    
    def cobble(self):
        repair_msg = self.repair() 
        return repair_msg
    pass