'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re


@dataclass(frozen=True)
class Usuario:
    pass
    
    @staticmethod
    def of(dni:str, nombre:str, apellidos:str, fecha_nacimiento:date) -> Usuario:
        pass
    
    
    @staticmethod
    def parse(linea:str) -> Usuario:
        pass
        
    def __str__(self):
        pass

if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)