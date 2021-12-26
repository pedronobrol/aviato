import os
from random import randint

class Canvas:
    def __init__(self, file_name: str, height: float, width: float, x_origin: float, y_origin: float):
        self.file_name = file_name 
        self.path = f'{os.getcwd()}/samples/{file_name}'
        self.height = height
        self.width = width
        self.x_origin = x_origin
        self.y_origin =  y_origin
        self.canvas = ''
 
    def pack(self) -> None:
        '''
        Make changes to canvas persistent
        '''
        canvas_file = open(self.path,'w')
        self.canvas += '</svg>'
        canvas_file.write(self.canvas)
        canvas_file.close()
    def unpack (self):
        '''
        Unpack canvas so that it can be editable again
        '''
        self.canvas = self.canvas.replace('</svg>',  '')

    def start_canvas(self) -> None:
        self.canvas +=  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="230.39999999999998 86.39999999999998 2419.2 2419.2">'
        self.insert_square(self.x_origin, self.y_origin, self.height, self.width)

    def insert_square(self, x_origin: float, y_origin: float, height: float, width: float) -> None:
        self.insert_line(x_origin, x_origin + width, y_origin, y_origin)
        self.insert_line(x_origin  + width, x_origin + width, y_origin, y_origin + height)
        self.insert_line(x_origin, x_origin, y_origin, y_origin + height)
        self.insert_line(x_origin, x_origin + width, y_origin + height, y_origin + height)
    
    def next_step(self):
        self.insert_random_lines(self.x_origin, self.y_origin, self.height, self.width)

    def insert_random_lines(self, x_origin: float, y_origin: float, height: float, width: float) -> None:

        x1 =  randint(x_origin, x_origin + width)
        x2 = randint(x_origin, x_origin + width)
        y1 = randint(y_origin, y_origin + height)
        y2= randint(y_origin, y_origin + height)
        print(f'>>>: {y_origin} [[{x1}, {y1}],[{x2},{y2}]')
        self.insert_line(x1, x2, y1, y2, color ='#f00') 
        
    def insert_line(self, x1: float, x2: float, y1: float, y2: float, opacity: float = 1, color: str = '#000', stroke_width: float = 6.72):
        self.canvas +=  f'<line stroke="{color}" opacity="{opacity}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="{stroke_width}"/>'

# canvas = Canvas('sample6.svg', 1800, 1900, 500, 400)   

# canvas.start_canvas()
# canvas.next_step()
# canvas.next_step()

# canvas.pack()

