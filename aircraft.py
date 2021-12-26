from canvas import Canvas
from random import randint, getrandbits
from copy import deepcopy

Node = [int]
Vertex = [Node, Node]
Graph = [Vertex]

class Aircraft:

    CANVAS_WIDTH = 1900
    CANVAS_HEIGHT = 1800
    CANVAS_X_ORIGIN = 500
    CANVAS_Y_ORIGIN = 400

    def __init__(self, graph: Graph = []) -> None:
        self.graph = Graph
    def build_2d_model(self, file_name: str):
        canvas = Canvas(file_name, self.CANVAS_HEIGHT, self.CANVAS_WIDTH, self.CANVAS_X_ORIGIN, self.CANVAS_Y_ORIGIN)
        canvas.start_canvas()
        for vertex in self.graph:
            canvas.insert_line(vertex[0][0], vertex[1][0], vertex[0][1], vertex[1][1], color = '#f00')
        canvas.pack()
    
    def generate_random_graph(self, max_distance: int, max_loops: int) -> Graph:
        self.graph  = []
        for loop in range(0, max_loops):
            start_loop = True
            for node in range(0, max_distance):
                if start_loop:
                    x1, y1 = self.get_random_start_coordinates()
                    start_loop = False
                else:
                    x1 = x2
                    y1 = y2
                x2 = randint(self.CANVAS_X_ORIGIN, self.CANVAS_X_ORIGIN + self.CANVAS_WIDTH/2)
                y2 = randint(self.CANVAS_Y_ORIGIN, self.CANVAS_Y_ORIGIN + self.CANVAS_HEIGHT)
                self.graph.append([[x1,y1], [x2, y2]])
            self.graph[-1][-1] = self.get_random_start_coordinates()
        self.mirror_graph() 
        return self.graph

    def mirror_graph(self) -> None:
        mirror = deepcopy(self.graph)
        for vertex in mirror:
            vertex[0][0] -= self.CANVAS_WIDTH + 2*self.CANVAS_X_ORIGIN
            vertex[0][0] *= -1
            vertex[1][0] -= self.CANVAS_WIDTH + 2*self.CANVAS_X_ORIGIN
            vertex[1][0] *= -1
        self.graph += mirror

    def get_random_start_coordinates(self) -> [int, int]:
        if bool(getrandbits(1)):
            x1 = randint(self.CANVAS_X_ORIGIN, self.CANVAS_X_ORIGIN + self.CANVAS_WIDTH/2)
            y1 = self.CANVAS_Y_ORIGIN
        else:
            x1 = self.CANVAS_X_ORIGIN
            y1 = randint(self.CANVAS_Y_ORIGIN, self.CANVAS_Y_ORIGIN + self.CANVAS_HEIGHT)
        return [x1,y1]
        
        


aircraft = Aircraft()

print(aircraft.generate_random_graph(3,3))
aircraft.build_2d_model('sample6.svg')