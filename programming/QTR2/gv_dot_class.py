from graphviz import Graph

ni = Graph('ni')

ni.attr('node', shape='rarrow')
ni.node('1', 'Ni!')
ni.node('2', 'Ni!')
ni.node('3', 'Ni!', shape='egg')

ni.attr('node', shape='star')
ni.node('4', 'Ni!')
ni.node('5', 'Ni!')

ni.attr(rankdir='LR')
ni.edges(['12', '23', '34', '45'])

print(ni.source)

ni.render('gv_dot_class.gv', view=False)

