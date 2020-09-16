from paraview.simple import *
import os

# Change working directory to allow data files to be found when the
# script is run from the Python shell in the ParaView GUI
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

# Read heightmap image stored in .PNG format on disk. The image will
# be represented as a uniform grid.
reader = OpenDataFile("../data/heightmap.png")
Show(reader)

# Create a filter that displaces the image plane using the height data
heightmap = WarpByScalar()
heightmap.ScaleFactor = 0.5
heightmap.Input = reader
Show(heightmap)
Hide(reader)

# Assign a discretised color function and a colorbar to the heightmap
heightmap_props = GetDisplayProperties(heightmap)
lut = GetColorTransferFunction(heightmap_props.ColorArrayName[1])
lut.ApplyPreset("Viridis (matplotlib)", True)
lut.Discretize = True
lut.NumberOfTableValues = 9
colorbar = GetScalarBar(lut)
colorbar.Enabled = True
colorbar.Title = "Height"
colorbar.TitleFontSize = 10
colorbar.LabelFontSize = 10

# Change the window background to a gradient
view_props = GetViewProperties()
view_props.UseGradientBackground = True

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool.
Interact()
