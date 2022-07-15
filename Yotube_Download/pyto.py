# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 23:06:12 2022

@author: Smurf
"""


from PyQt5 import uic

with open('hakkında.py','w',encoding=("utf-8"))as fout:
    uic.compileUi('hakkında.ui', fout)
    