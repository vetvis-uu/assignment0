from paraview.simple import *
import os

# Change working directory to allow data files to be found when the
# script is run from the Python shell in the ParaView GUI
datapath = os.path.dirname(os.path.abspath(__file__))
os.chdir(datapath)

# Read 4D point data stored in .CSV format on disk. The data will be
# represented as a table, so we also need to apply a TableToPoints
# filter to extract the points. 
reader = CSVReader(FileName="../data/timesteps.csv")
points = TableToPoints()
points.Input = reader
points.XColumn = " X"
points.YColumn = " Y"
points.ZColumn = " Z"
Show(points)

# Create a Glyph filter that adds a sphere to each point. By default,
# the Glyph filter will not show all points in the dataset, so we need
# to change the GlyphMode to "All Points".
glyph = Glyph()
glyph.GlyphType = "Sphere"  # You can also set this to a custom source
glyph.GlyphMode = "All Points"
glyph.ScaleArray = None
glyph.Input = points
Show(glyph)

# Create a Threshold filter to mask glyphs by the timestamp value
threshold = Threshold()
threshold.Input = glyph
threshold.ThresholdRange = [0, 100]
Show(threshold)
Hide(glyph)

# Add keyframes for animating the threshold range
track = GetAnimationTrack('ThresholdBetween', index=1, proxy=threshold)
track.KeyFrames = [CompositeKeyFrame(), CompositeKeyFrame()]
track.KeyFrames[0].KeyTime = 0.0
track.KeyFrames[0].KeyValues = [0.0]
track.KeyFrames[1].KeyTime = 1.0
track.KeyFrames[1].KeyValues = [199.0]
scene = GetAnimationScene()
scene.NumberOfFrames = 100

# Update the rendering of the current active view
Render()

# Allow interaction and keep the window open. This is only necessary
# if you run the script from the pvpython command line tool
scene.Play()
Interact()
