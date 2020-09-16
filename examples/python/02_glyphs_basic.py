from paraview.simple import *

# Create a PointSource with 100 random points. The default radius of a
# PointSource is 0, so we need to set a radius as well.
ps = PointSource()
ps.NumberOfPoints = 100
ps.Radius = 1.0
Show(ps)

# Create a Glyph filter that adds a sphere to each point. By default,
# the Glyph filter will not show all points in the dataset, so we need
# to change the GlyphMode to "All Points".
glyph = Glyph()
glyph.GlyphType = "Sphere"  # You can also set this to a custom source
glyph.GlyphMode = "All Points"
glyph.Input = ps
Show(glyph)

# Show points and glyphs side-by-side by adding a custom translation to
# each source/filter. Also give the points a distinct color.
ps_props = GetDisplayProperties(ps)
ps_props.Position = [-1, 0, 0]
ps_props.DiffuseColor = [1, 0, 1]
ps_props.PointSize = 3
glyph_props = GetDisplayProperties(glyph)
glyph_props.Position = [1, 0, 0]

# Change the window background color
view_props = GetViewProperties()
view_props.Background = [1, 1, 1]  # Set the BG color to white

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool
Interact()