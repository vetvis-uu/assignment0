from paraview.simple import *
import os

# Change working directory to allow data files to be found when the
# script is run from the Python shell in the ParaView GUI
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

# Read 3D model stored in Wavefront (.OBJ) format on disk. The model
# will be represented as an unstructured grid.
reader = OpenDataFile("../data/bunny.obj")
Show(reader)

# Change the color of the model via the reader object
reader_props = GetDisplayProperties(reader)
reader_props.DiffuseColor = [1, 1, 0]

# Change the window background to a gradient
view_props = GetViewProperties()
view_props.UseGradientBackground = True
view_props.Background = [1, 1, 1]
view_props.Background2 = [0, 0, 0]

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool.
Interact()
