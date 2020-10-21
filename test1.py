#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import fuzzy
import vocales


class Testprueba (unittest.TestCase):
    
    temperatura =[[10,20,30,40],
                  [20,30,40,50],
                  [30,40,50,60],
                  [40,50,60,70]]
    
    def test_fuzyy(self):
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,5),[0, 0, 0, 0])
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,25),[1, 0.5, 0, 0])
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,42),[0, 0.8, 1, 0.2])
    
    def test_vocales(self):
        self.assertEqual(vocales.cuenta_vocales("bibliotecario"),[7,6])
        self.assertEqual(vocales.cuenta_vocales("biblioteca"),[5,5])
        self.assertEqual(vocales.cuenta_vocales("mimamamemima"),[6,6])
        
    
if __name__ == '__main__':
    unittest.main()

