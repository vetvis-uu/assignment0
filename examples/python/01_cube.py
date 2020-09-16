from paraview.simple import *

# Create a Box source for our cube
cube = Box()

# Make the cube visible
Show(cube)

# Change the cube color
cube_props = GetDisplayProperties(cube)
cube_props.DiffuseColor = [1, 0, 0]  # Set the cube color to red

# Change the window background color
view_props = GetViewProperties()
view_props.Background = [0, 0, 0]  # Set the BG color to black

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool
Interact()