from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define the entities
dot.node('Camera', 'Camera')
dot.node('Frame', 'Frame')
dot.node('YOLOv8', 'YOLOv8 Model')
dot.node('BagDetection', 'Bag Detection')
dot.node('Count', 'Count')
dot.node('UI', 'User Interface')
dot.node('Log', 'Log')
dot.node('Database', 'Database')

# Define the relationships
dot.edge('Camera', 'Frame', 'captures')
dot.edge('Frame', 'YOLOv8', 'input to')
dot.edge('YOLOv8', 'BagDetection', 'detects')
dot.edge('BagDetection', 'Count', 'triggers')
dot.edge('Count', 'UI', 'displays on')
dot.edge('Count', 'Log', 'logs to')
dot.edge('Log', 'Database', 'stores in')

# Render the ER diagram as a PNG image
dot.format = 'png'
file_path = '/mnt/data/er_diagram'
dot.render(file_path)

file_path + '.png'
