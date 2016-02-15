import scipy.spatial as sp, numpy as np  
from collections import OrderedDict
import math
import sys
import  timeit
sys.setrecursionlimit(999999999)
import itertools
from collections import Counter

class Vertice():
    __slots__ = ['x', 'y', 'z', 'close_points']
    def __init__(self): 
        self.x = 0
        self.y = 0
        self.z = 0
        self.close_points=[]

class collection(type):
    def __iter__(cls):
        return iter(cls._registry)

class Triangle():
    __slots__ = ['v1', 'v2', 'v3', 'centroid', 'neighbours', 'Nx', 'Ny', 'Nz', 'sem', 'Plist', 'clas','ground', 'roof', 'wall', 'building_ground',  '_registry']
    __metaclass__ = collection
    _registry = []
    
    def __init__(self):
        self.v1 =0
        self.v2 =0
        self.v3 =0
        self.centroid = ()
        self.neighbours = []
        self.Nx = 0
        self.Ny = 0
        self.Nz = 0
        self.sem =  ' '
        self.Plist = []
        self.ground = False
        self.roof = False
        self.wall = False
        self.building_ground = False
        self._registry.append(self)

class collect(type):
    def __iter__(cls):
        return iter(cls._registry)

class region():
    __metaclass__ = collect
    _registry = []
    def __init__(self):
        Collection = []
        self._registry.append(self)
