from graphviz import Digraph

ps = Digraph(name='pet-shop', node_attr={'shape': 'plaintext'})

ps.node('parrot')
ps.node('dead')

ps.edge('parrot', 'dead')

# From left to right
ps.graph_attr['rankdir'] = 'LR'
ps.edge_attr.update(arrowhead='vee', arrowsize='2')

print(ps.source)

ps.render('gv_dot_styling.gv', view=False)
