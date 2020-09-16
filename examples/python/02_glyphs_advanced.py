from paraview.simple import *

# Create a PointSource with 100 random points. The default radius of a
# PointSource is 0, so we need to set a radius as well.
ps = PointSource()
ps.NumberOfPoints = 100
ps.Radius = 1.0
Show(ps)

# Create a filter that assign a random scalar value to each point
ra = RandomAttributes()
ra.GenerateCellVectors = False
ra.GeneratePointScalars = True
ra.GeneratePointVectors = True
ra.DataType = "Float"
ra.ComponentRange = [0, 1]
ra.Input = ps
Show(ra)
Hide(ra)

# Create a Glyph filter that adds a sphere to each point. By default,
# the Glyph filter will not show all points in the dataset, so we need
# to change the GlyphMode to "All Points".
glyph1 = Glyph()
glyph1.GlyphType = "Sphere"  # You can also set this to a custom source
glyph1.GlyphMode = "All Points"
glyph1.ScaleArray = ['POINTS', 'RandomPointScalars']
glyph1.OrientationArray = None
glyph1.Input = ra
Show(glyph1)
glyph2 = Glyph()
glyph2.GlyphType = "Sphere"  # You can also set this to a custom source
glyph2.GlyphMode = "All Points"
glyph2.ScaleArray = None
glyph2.OrientationArray = None
glyph2.Input = ra
Show(glyph2)
glyph3 = Glyph()
glyph3.GlyphType = "Arrow"  # You can also set this to a custom source
glyph3.GlyphMode = "All Points"
glyph3.ScaleArray = None
glyph3.OrientationArray = ['POINTS', 'RandomPointVectors']
glyph3.Input = ra 
Show(glyph3)

# Show points and glyphs side-by-side by adding a custom translation to
# each source/filter. Also give the points a more distinct color.
glyph1_props = GetDisplayProperties(glyph1)
glyph1_props.Position = [-2, 0, 0]
glyph1_props.ColorArrayName = None
glyph2_props = GetDisplayProperties(glyph2)
glyph2_props.Position = [0, 0, 0]
glyph3_props = GetDisplayProperties(glyph3)
glyph3_props.Position = [2, 0, 0]
lut = GetColorTransferFunction(glyph1_props.ColorArrayName[1])
colorbar = GetScalarBar(lut)
colorbar.Enabled = True
colorbar.ComponentTitle = ""
colorbar.Title = "RandomPointScalars"
colorbar.TitleColor = [0, 0, 0]
colorbar.LabelColor = [0, 0, 0]
colorbar.TitleFontSize = 10
colorbar.LabelFontSize = 10

# Change the window background color
view_props = GetViewProperties()
view_props.Background = [1, 1, 1]

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool
Interact()