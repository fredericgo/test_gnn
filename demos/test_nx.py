import os
import sys
# Our Modules
reader_folder = os.path.realpath(os.path.abspath('..'))
if reader_folder not in sys.path:
    sys.path.append(reader_folder)

from GraphReader import graph_reader

g = graph_reader.create_graph_grec('../data/GREC/data/image10_1.gxl')