# -*- coding: utf-8 -*-

import pyxel

class Button():
    def __init__(self, col, pos, r, sound, key):
        self.col = col
        self.pos = pos
        self.sound = sound
        self.r = r
        self.colActivate = self.col[0]
        self.key = key
        pyxel.sound(self.sound[1]).set(f"{self.sound[2]}", "T", "7", "N", 10)
    def update(self):
        if (pyxel.btn(self.key)): 
            self.colActivate = self.col[0]
            pyxel.play(self.sound[0],self.sound[1])
        else: self.colActivate = self.col[1]
        
    def draw(self):
        pyxel.circb(self.pos[0],self.pos[1],self.r,self.colActivate)
        if (pyxel.btn(self.key)): pyxel.circ(self.pos[0],self.pos[1],self.r,self.colActivate)