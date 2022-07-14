import svgutils 
import svgutils.transform as svgt
import svg_stack as ss

def add_relative_directory_to_svg_matrix(svg_matrix, relative_source_path):
    # Prefixes the directory going to the constituents of the svg matrix to their names.
    for i in range(0,len(svg_matrix)):
        for j in range(0,len(svg_matrix[i])):
            svg_matrix[i][j] = relative_source_path + svg_matrix[i][j]


# THIS DOESNT IMPLMENT DICTIONARY ELEMENTS IN THE MATRIX (FOR COLORING ETC), TO DO
def svg_layout_matrix(svg_file_matrix, width_of_block:int, height_of_block:int):
    # Only inpuy
    # Each entry of the matrix consits of a dictionary with
    n = len(svg_file_matrix) # Number of rows
    m = len(svg_file_matrix[0]) # Number of columns
    
    layoutMatrix = [0] * n
    for i in range(0,n):
        layoutMatrix[i] = [0] * m

    layoutMatrix[0][0] = svgutils.transform.fromfile(svg_file_matrix[0][0])
    width = width_of_block
    height = height_of_block


    layoutFinal = svgutils.transform.SVGFigure(str(n * width), str(m * height))

    for i in range(0,n):
        for j in range(0,m):
            layoutMatrix[i][j] = svgutils.transform.fromfile(svg_file_matrix[i][j])
            layoutMatrix[i][j] = layoutMatrix[i][j].getroot()
            layoutMatrix[i][j].moveto(j * width, i * height)
            
            layoutFinal.append(layoutMatrix[i][j])
    return layoutFinal

'''

For some reason doing 

width = layoutMatrix[0][0].width
height = layoutMatrix[0][0].height

doesn't work, even when they equal to the manually inputted values.

'''



letterA = [
    ["SVGs/Inkscape Curvy Knot SVGs/downRight.svg", "SVGs/Inkscape Curvy Knot SVGs/leftDown.svg"],
    ["SVGs/Inkscape Curvy Knot SVGs/upRight.svg", "SVGs/Inkscape Curvy Knot SVGs/upDownCrossingOver.svg"]
    ]




svg_layout_matrix(letterA, 60, 60).save("namewhtvr.svg")


class SVGFileComponent:
    def __init__(self, name, relative_path, color="#000000"):
        self.name = name
        self.relative_path = relative_path
        self.colour = color




class SVGFileMatrix:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix



