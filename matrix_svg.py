import codecs
import svg_stack as ss



def save_svg_document(path_of_document, layout):
    doc = ss.Document()
    doc.setLayout(layout)
    doc.save(path_of_document)
    del doc


def svg_layout_matrix(svg_file_matrix):
    
    n = len(svg_file_matrix)
    m = len(svg_file_matrix[0])

    layoutList = [0] * n
    layoutFinal = ss.VBoxLayout()

    for i in range(0,n):
        layoutList[i] = ss.HBoxLayout()
        
        for j in range(0,m):
            layoutList[i].addsvg(svg_file_matrix[i][j], alignment=ss.AlignCenter)
        layoutFinal.addLayout(layoutList[i])

    return layoutFinal


class SVGFile:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors



class SVGFileComponent(SVGFile):
    def __init__(self, name, relative_directory, colors={"#000000"}):
        self.name = name
        self.relative_path = relative_directory
        self.colors = colors
    
    def coloring(self, new_color, past_colors:dict, working_dir):
        svg_file = codecs.open(self.relative_path).read()
        for color in past_colors.items:
            new_svg_file = svg_file.replace(color, new_color)

    def coloring_all(self, new_color):
        svg_file = codecs.open(self.relative_path).read()
        for color in self.colors:
            new_svg_file = svg_file.replace(color, new_color)



class SVGFileMatrix(SVGFile):
    def svg_colors(self):
        n = len(self.matrix)
        m = len(self.matrix[0])

        layoutList = [0] * n
        
    
    def svg_layout(self):
    
        n = len(self.matrix)
        m = len(self.matrix[0])

        layoutList = [0] * n
        layoutFinal = ss.VBoxLayout()

        for i in range(0,n):
            layoutList[i] = ss.HBoxLayout()
        
            for j in range(0,m):
                layoutList[i].addsvg(self.matrix[i][j], alignment=ss.AlignCenter)
            layoutFinal.addLayout(layoutList[i])


        return layoutFinal

    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix
        # self.colors = 
        self.layout = self.svg_layout()

        

def add_relative_directory_to_svg_matrix(svg_matrix, relative_source_path):
    # Prefixes the directory going to the constituents of the svg matrix to their names.
    for i in range(0,len(svg_matrix)):
        for j in range(0,len(svg_matrix[i])):
            svg_matrix[i][j] = relative_source_path + svg_matrix[i][j]


'''
def svg_layout_matrix(svg_file_matrix):
    
    n = len(svg_file_matrix)
    m = len(svg_file_matrix[0])

    layoutList = [0] * n
    layoutFinal = ss.VBoxLayout()

    for i in range(0,n):
        layoutList[i] = ss.HBoxLayout()
        
        for j in range(0,m):
            layoutList[i].addsvg(svg_file_matrix[i][j], alignment=ss.AlignCenter)
        layoutFinal.addLayout(layoutList[i])


    return layoutFinal
'''


def save_svg_document(path_of_document, layout):
    doc = ss.Document()
    doc.setLayout(layout)
    doc.save(path_of_document)
    del doc

