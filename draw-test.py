import schemdraw
from schemdraw import flow

d = schemdraw.Drawing()

d += (INT_X13Y100 := flow.Box(w=4, h=2).label('INT_X13Y100\nEN5BEG0'))
d += flow.Arrow().right().at(INT_X13Y100.E).length(d.unit*2)
d += (INT_X14Y100 := flow.Box(w=4, h=2).anchor('W').label('INT_X14Y100\nEN5A0'))
d += flow.Arrow().right().at(INT_X14Y100.E).length(d.unit*2)
d += (INT_X15Y100 := flow.Box(w=4, h=2).anchor('W').label('INT_X15Y100\nEN5B0'))
d += flow.Arrow().right().at(INT_X15Y100.E).length(d.unit*2)
d += (INT_X16Y100 := flow.Box(w=4, h=2).anchor('W').label('INT_X16Y100\nEN5MID0'))
d += flow.Arrow().up().at(INT_X16Y100.N).length(d.unit*2)
d += (INT_X16Y101 := flow.Box(w=4, h=2).anchor('S').label('INT_X16Y101\nEN5C0'))

d.draw()