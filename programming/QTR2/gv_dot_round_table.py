# Import module
from graphviz import Digraph

# Create Digraph instance
dot = Digraph(comment="The Round Table")

# Add node (name, label)
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

# Edge A -> B, A -> L
dot.edges(['AB', 'AL'])
# Edge B -> L
dot.edge('B', 'L', constraint='false')

# See structure
print(dot.source)

# Save and render the source code (file directory, open visualized pdf)
dot.render('gv_dot_round_table.gv', view=False)
