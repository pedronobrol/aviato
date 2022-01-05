from typing import List
from canvas import Canvas
from random import randint, getrandbits, choice, uniform
from copy import deepcopy
from enum import Enum

Node = [int]
class Type (Enum):
    MOUNTAIN = '#f00'
    VALLEY = '#00f'
    FACET_CREASE = 'ffff00'
class Edge:
    def __init__ (self, node1: Node, node2: Node, angle: float, type: Type) -> None:
        self.node1 = node1
        self.node2 = node2
        self.angle = angle
        self.type = type

    def add(self, coords: List) -> None:
        self.node2 = coords

    def print (self) -> None:
        print('EDGE')
        print(self.node1)
        print(self.node2)
class Graph:
    def __init__(self, edges: List = [], faces: List = []) -> None:
        self.edges = edges
        self.faces = faces

    def append_edge (self, edge: Edge) -> None:
        self.edges.append(edge)
class Aircraft:

    CANVAS_WIDTH = 1900
    CANVAS_HEIGHT = 1800
    CANVAS_X_ORIGIN = 500
    CANVAS_Y_ORIGIN = 400

    def __init__(self) -> None:
        self.graph = Graph()

    def build_2d_model(self, file_name: str) -> None:
        canvas = Canvas(file_name, self.CANVAS_HEIGHT, self.CANVAS_WIDTH, self.CANVAS_X_ORIGIN, self.CANVAS_Y_ORIGIN)
        canvas.start_canvas()
        for edge in self.graph.edges:
            canvas.insert_line(edge.node1[0], edge.node2[0], edge.node1[1], edge.node2[1], edge.angle, edge.type.value)
        canvas.pack()  

    def generate_random_graph(self, max_distance: int, max_loops: int) -> Graph:
        self.graph  = Graph()
        for loop in range(0, max_loops):
            start_loop = True
            for node in range(0, max_distance):
                if start_loop:
                    x1, y1 = self.get_random_start_coordinates()
                    start_loop = False
                    self.graph.faces.append(max_distance + 1)
                else:
                    x1 = x2
                    y1 = y2
                x2 = randint(self.CANVAS_X_ORIGIN, self.CANVAS_X_ORIGIN + self.CANVAS_WIDTH/2)
                y2 = randint(self.CANVAS_Y_ORIGIN, self.CANVAS_Y_ORIGIN + self.CANVAS_HEIGHT)
                # Appending new edge with Node1 and Node2, angle [0,1] and type (MOUNTAIN, VALLEY)
                # TODO: Type and angle symetry in mirror or not?
                edge = Edge([x1,y1], [x2, y2], uniform(0,1), choice([Type.MOUNTAIN,Type.VALLEY]))
                self.graph.append_edge(edge)
                # TODO: Change this approach to count faces into the structure
            self.graph.edges[-1].add(self.get_random_start_coordinates())
        self.mirror_graph() 
        return self.graph

    def mirror_graph(self) -> None:
        mirror = deepcopy(self.graph)
        for edge in mirror.edges:
            edge.node1[0] -= self.CANVAS_WIDTH + 2*self.CANVAS_X_ORIGIN
            edge.node1[0] *= -1
            edge.node2[0] -= self.CANVAS_WIDTH + 2*self.CANVAS_X_ORIGIN
            edge.node2[0] *= -1
        # Graph is extended with mirror graph (symetric)
        self.graph.edges.extend(mirror.edges)
        self.graph.faces.extend(mirror.faces)

    def get_random_start_coordinates(self) -> List:
        if bool(getrandbits(1)):
            x1 = randint(self.CANVAS_X_ORIGIN, self.CANVAS_X_ORIGIN + self.CANVAS_WIDTH/2)
            y1 = self.CANVAS_Y_ORIGIN
        else:
            x1 = self.CANVAS_X_ORIGIN
            y1 = randint(self.CANVAS_Y_ORIGIN, self.CANVAS_Y_ORIGIN + self.CANVAS_HEIGHT)
        return [x1,y1]
        
        


aircraft = Aircraft()

print(aircraft.generate_random_graph(2,4))
aircraft.build_2d_model('sample9.svg')
