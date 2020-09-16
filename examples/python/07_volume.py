from paraview.simple import *
import os

# Change working directory to allow data files to be found when the
# script is run from the Python shell in the ParaView GUI
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

# Read volume data stored in legacy .VTK format on disk. The volume
# will be represented as a uniform grid.
reader = OpenDataFile("../data/tooth.vtk")
Show(reader)

# Create a filter that extracts an isocontour from the volume
isocontour = Contour()
isocontour.Isosurfaces = [80.0]  # You can also set multiple isolevels
isocontour.Input = reader
Show(isocontour)

# Show isocontour and volume rendering side-by-side by adding a custom
# translation to each source/filter.
reader_props = GetDisplayProperties(reader)
reader_props.SetRepresentationType("Volume")
reader_props.ScalarOpacityUnitDistance = 10.0  # Lowers the opacity
reader_props.Position = [60, 0, 0]
isocontour_props = GetDisplayProperties(isocontour)
isocontour_props.Position = [-60, 0, 0]

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
