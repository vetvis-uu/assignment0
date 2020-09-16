from paraview.simple import *

# Create a PointSource with 50 random points. The default radius of a
# PointSource is 0, so we need to set a radius as well.
ps = PointSource()
ps.NumberOfPoints = 50
ps.Radius = 1.0
# Show(ps)

# Create a filter that assign a random scalar value to each point
ra = RandomAttributes()
ra.GenerateCellVectors = False
ra.GeneratePointScalars = True
ra.Input = ps

# Create a Glyph filter that adds a sphere to each point. By default,
# the Glyph filter will not show all points in the dataset, so we need
# to change the GlyphMode to "All Points".
glyph = Glyph()
glyph.GlyphType = "Sphere"  # You can also set this to a custom source
glyph.GlyphMode = "All Points"
glyph.Input = ra
glyph.ScaleFactor = 0.5
Show(glyph)

# Change the display properties of the glyphs so that they are
# visualized as transparent and with a custom color mapping
glyph_props = GetDisplayProperties(glyph)
glyph_props.Opacity = 0.2
lut = GetColorTransferFunction(glyph_props.ColorArrayName[1])
lut.ApplyPreset("Rainbow Uniform", True)

# Change the window background color
view_props = GetViewProperties()
view_props.Background = [1, 1, 1]

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool
Interact()