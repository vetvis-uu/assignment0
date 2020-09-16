from paraview.simple import *
import os

# Change working directory to allow data files to be found when the
# script is run from the Python shell in the ParaView GUI
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

# Read a 3D RGBA point cloud stored in .PLY format on disk. The point
# cloud will be represented as an unstructured grid.
reader = OpenDataFile("../data/desk.ply")
Show(reader)

# Change the display propertios of the point cloud so that each point is
# visualized as a small disk. Since the points already have RGBA color
# values, we want to disable any color mapping. Also, the reader does not
# create any cell data for the points, so we need to change the
# representation to "Point Gaussian" to see the points.
reader_props = GetDisplayProperties(reader)
reader_props.MapScalars = False
reader_props.SetRepresentationType('Point Gaussian')
reader_props.ShaderPreset = 'Plain circle'
reader_props.GaussianRadius = 0.005

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool.
Interact()
