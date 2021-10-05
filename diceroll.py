#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Dice roll simulator for games.

    Simulate die rolling to get random results in your programs
    according to the number of faces of a real die; simulate the die 
    models most used in roleplaying games.
    
    1) How to roll a dice with 'Dice' class?
    
    The 'Dice' class contains the .roll() method. Just call one it in
    your program, assigning the result that will be returned by the 
    'Dice' class to a variable, and use the result according to your 
    need.
    
    Ex. (in the Interpreter)
    
    >>> Dice().roll()
    >>> 5
    
    The return of the class will be a random integer, according to the 
    number of sides of your die. By default, the 'Dice' class 
    represents a D6 model die.
    
    2) How to create a custom die with 'Dice' class?
    
    To create your own custom dice object, you need to create an instance
    from 'Dice', or a class that inherits from it. Enter a list as an 
    argument containing the contents of all sides of your die, or an 
    integer that represents the number of sides. to use it just call the 
    'roll' method. The return will be one of the values ​​entered on one of 
    the faces of your die.
    
    Ex. (in the Interpreter)
    
    >>> my_dice = Dice(['♤', '♡', '◇', '♧', '○', '□'])
    >>> my_dice.roll()
    >>> ♡
    
    You can still use the various pre-defined dice templates. The 'dice' 
    module contains classes that simulate the most used dice models in 
    RPG games.
    
    Ex. (in the Interpreter)
    
    >>> # Rolling a 3-sided die;
    >>> D3().roll()
    >>> 2
    >>>
    >>> # Rolling a 6-sided die;
    >>> D6().roll()
    >>> 5
    
    With the 'dice' module you can automatically simulate all these 
    RPG dice models just by calling the class that represents the 
    model (The number in each class name represents the number of 
    sides of the die):
        
        * D3
        * D4
        * D6
        * D8
        * D12
        * D20
        * D30
        * D100
    
"""


__author__ = 'Luiz R. Dererita'
__version__ = '0.0.1'
__copyright__ = 'Developed by Luiz R. Dererita. 2021 (c)'
__license__ = 'MIT License'
__email__ = 'luizdererita02@gmail.com'
__maintainer__ = 'Luiz R. Dererita'
__credits__ = 'Thanks to all free software comunity.'

                                        
from random import randint, choice
import re


class Dice():
    """ This class creates an instance of custom die. """
    
    def __init__(self, sides: int or list):
        """ Set the die faces with a list in the sides argument """
        self.sides = sides
    
    @property
    def sides(self):
        return self._sides
        
    @sides.setter
    def sides(self, sides):
        if not type(sides) in (int, tuple, list):
            error = 'Enter an integer or list that '\
                    'represents the sides of your die.'
            raise TypeError(error)
        self._sides = sides
    
    def roll(self):
        """ This method simulates the roll of a die. """
        if type(self.sides) is int:
            return randint(1, self.sides)
        return choice(self.sides)
        

class D3(Dice):
    """ This class simulates the roll of a D3 die. """
    
    def __init__(self):
        self.sides = 3 # set the sides of die
        
    
class D4(Dice):
    """ This method simulates the roll of a D4 die. """
    
    def __init__(self):
        self.sides = 4 # set the sides of die
    
    
class D6(Dice):
    """ This method simulates the roll of a D6 die. """
    
    def __init__(self):
        self.sides = 6 # set the sides of die
    

class D8(Dice):
    """ This method simulates the roll of a D8 die. """
    
    def __init__(self):
        self.sides = 8 # set the sides of die
    
    
class D10(Dice):
    """ This method simulates the roll of a D10 die. """
    
    def __init__(self):
        self.sides = 10 # set the sides of die
        
        
class D12(Dice):
    """ This method simulates the roll of a D12 die. """
    
    def __init__(self):
        self.sides = 12 # set the sides of die
        
        
class D20(Dice):
    """ This method simulates the roll of a D20 die. """
    
    def __init__(self):
        self.sides = 20 # set the sides of die
        
        
class D30(Dice):
    """ This method simulates the roll of a D30 die. """
    
    def __init__(self):
        self.sides = 30 # set the sides of die
    
        
class D100(Dice):
    """ This method simulates the roll of a D100 die. """
    
    def __init__(self):
        self.sides = 100 # set the sides of die
    