import schemdraw
from schemdraw import flow
import re

file_name = 'INT_X14Y100'

line = '[wire  EN5A0  8] : [INT_X13Y100  -->  EN5BEG0] : [INT_X15Y100  -->  EN5B0] : [INT_X16Y100  -->  EN5MID0] : [INT_X16Y101  -->  EN5C0] : [INT_X16Y102  -->  EN5END0]'

wn = 'EN5A0'


def get_overall_direction(wire_name):
    way = wire_name[0:2]
    dir_dict = {
        'ER':0,#向右
        'EL':0,#向右
        'EN':1,#先右后上
        'NE':2,#先上后右
        'NR':3,#向上
        'NL':3,#向上
        'NW':4,#先上后左
        'WN':5,#先左后上
        'WL':6,#向左
        'WR':6,#向左
        'WS':7,#先左后下
        'SW':8,#先下后左
        'SL':9,#向下
        'SR':9,#向下
        'SE':10,#先下后右
        'ES':11,#先右后下
    }
    direction = dir_dict.get(way, -1)
    return direction
    #return dir_dict.get(way, "Invalid Direction")

def get_coordinates(INT_X):#获得一个INT的坐标
    x = re.compile('X')
    y = re.compile('Y')
    span_x = x.search(INT_X).span()
    span_y = y.search(INT_X).span()

    val_x = INT_X[span_x[1]:span_y[0]]
    val_y = INT_X[span_y[1]:]

    return (int(val_x), int(val_y))

#def get_alphabet_order(WIRE_NAME):
    #if WIRE_NAME[-2] == 'A':

def parse_line(in_line, intx_name): #将当前的INT名和wire名插入当前一行文本，然后将文本分解为二元组（INT名，wire名），并将这些元组存入新的列表
    in_line = line.replace(':','')
    in_line = in_line.replace('[','')
    in_line = in_line.replace(']','')
    in_line = in_line.split()
    wire_name = in_line[1]
    in_line.append(intx_name)
    in_line.append(' --> ')
    in_line.append(wire_name)

    nodes_list = []
    index = 3
    while index <= len(in_line) - 3:
        nodes_list.append((in_line[index],in_line[index+2]))
        index = index + 3
    
    return nodes_list

class node_tuple:
    def __init__(self, int_name, wire_name, direction, xval, yval):
        self.int_name = int_name
        self.wire_name = wire_name
        self.direction = direction
        self.x = xval
        self.y = yval

    def __repr__(self):
        return repr((self.int_name,self.wire_name,self.direction,self.x,self.y))

def sort_nodes_list(nodes_list,direction):
    option = direction
    l = len(nodes_list)
    #temp = []
    
    def err():
        return -1

    def sort_x():#0
        nodes_list.sort(key=lambda node: node.x)
        
    def sort_x_y():#1
        nodes_list.sort(key=lambda node: node.x)
        i = 0
        while i < l -1:
            if nodes_list[i].x == nodes_list[i + 1].x :
                nodes_list[i:l].sort(key=lambda node: node.y)
                break
            else:i = i + 1

    def sort_y_x():#2
        nodes_list.sort(key=lambda node: node.y)
        i = 0
        while i < l -1:
            if nodes_list[i].y == nodes_list[i + 1].y :
                nodes_list[i:l].sort(key=lambda node: node.x)
                break
            else:i = i + 1

    def sort_y():#3
        nodes_list.sort(key=lambda node: node.y)

    def sort_y_xr():#4
        nodes_list.sort(key=lambda node: node.y)
        i = 0
        while i < l -1:
            if nodes_list[i].y == nodes_list[i + 1].y :
                nodes_list[i:l].sort(key=lambda node: node.x, reverse = True)
                break
            else:i = i + 1

    def sort_xr_y():#5
        nodes_list.sort(key=lambda node: node.x, reverse = True)
        i = 0
        while i < l -1:
            if nodes_list[i].x == nodes_list[i + 1].x :
                nodes_list[i:l].sort(key=lambda node: node.y)
                break
            else:i = i + 1

    def sort_xr():#6
        nodes_list.sort(key=lambda node: node.x, reverse = True)#True为降序

    def sort_xr_yr():#7
        nodes_list.sort(key=lambda node: node.x, reverse = True)
        i = 0
        while i < l -1:
            if nodes_list[i].x == nodes_list[i + 1].x :
                nodes_list[i:l].sort(key=lambda node: node.y, reverse = True)
                break
            else:i = i + 1

    def sort_yr_xr():#8
        nodes_list.sort(key=lambda node: node.y, reverse = True)
        i = 0
        while i < l -1:
            if nodes_list[i].y == nodes_list[i + 1].y :
                nodes_list[i:l].sort(key=lambda node: node.x, reverse = True)
                break
            else:i = i + 1 

    def sort_yr():#9
        nodes_list.sort(key=lambda node: node.y, reverse = True)

    def sort_yr_x(): #10
        nodes_list.sort(key=lambda node: node.y, reverse = True)
        i = 0
        while i < l -1:
            if nodes_list[i].y == nodes_list[i + 1].y :
                nodes_list[i:l].sort(key=lambda node: node.x)
                break
            else:i = i + 1

    def sort_x_yr():#11
        nodes_list.sort(key=lambda node: node.x)
        i = 0
        while i < l -1:
            if nodes_list[i].x == nodes_list[i + 1].x :
                nodes_list[i:l].sort(key=lambda node: node.y, reverse = True)
                break
            else:i = i + 1

    dict = {
        -1:err,
        0:sort_x,
        1:sort_x_y,
        2:sort_y_x,
        3:sort_y,
        4:sort_y_xr,
        5:sort_xr_y,
        6:sort_xr,
        7:sort_xr_yr,
        8:sort_yr_xr,
        9:sort_yr,
        10:sort_yr_x,
        11:sort_x_yr
    }

    dict.get(option,err)()

    print(nodes_list)
    return nodes_list

    #for node in nodes_list:
    #    xy = get_coordinates(node[0])

def draw_flow(nodes_list):
    #flow.Arrow()有4个方向：up()、down()、right()、left()和4个起始点：.at(WESN)
    #flow.Box()只需(w=4, h=2)一种即可，但是要自动起名字，可以将文本读为列表后获取列表长度，按索引号进行编号。另外还要设定锚点.anchor(WESN)
    #每个元素的结构为(self, int_name, wire_name, direction, xval, yval)
    d = schemdraw.Drawing()
    draw_1stbox = 'd += (' + nodes_list[0].int_name + ' := flow.Box(w=4, h=2).label(' + "'" + nodes_list[0].int_name + '\\n' + nodes_list[0].wire_name + "'" '))'
    #d += (INT_X13Y100 := flow.Box(w=4, h=2).label('INT_X13Y100\nEN5BEG0'))
    print(draw_1stbox)
    exec(draw_1stbox)
    n = 1
    node_no = len(nodes_list)
    while n <= len(nodes_list) - 1:
        xy_now = (nodes_list[n].x,nodes_list[n].y)
        xy_prev = (nodes_list[n-1].x,nodes_list[n-1].y)

        arrow_dir = 'warning'
        arrow_dest = "warning"
        anchor = "warning"

        if xy_prev[0] < xy_now[0]:
            arrow_dir = 'right'
            arrow_dest = "E"
            anchor = "'W'"

        if xy_prev[0] == xy_now[0]:
            if xy_prev[1] < xy_now[1]:
                arrow_dir = 'up'
                arrow_dest = "N"
                anchor = "'S'"
            if xy_prev[1] > xy_now[1]:
                arrow_dir = 'down'
                arrow_dest = "S"
                anchor = "'N'"

        if xy_prev[0] > xy_now[0]:
            arrow_dir = 'left'
            arrow_dest = "W"
            anchor = "'E'"


        draw_arrow = 'd += ' + 'flow.Arrow().' + arrow_dir + '().at(' + nodes_list[n-1].int_name + '.' + arrow_dest + ').length(d.unit*2)'
        draw_box = 'd += (' + nodes_list[n].int_name + ' := flow.Box(w=4, h=2)' + '.anchor(' + anchor + ').label(' + "'" +  nodes_list[n].int_name + '\\n' + nodes_list[n].wire_name + "'" +  '))' #nodes_list[n][0]为第n个INT的名字，nodes_list[n][1]为与之对应的wire的名字
        
        print(draw_arrow)
        print(draw_box)
        
        
        exec(draw_arrow)
        exec(draw_box)
        n = n + 1
        #print(draw_box)

    #d.draw()
    #draw_pic = "d.save(" + file_name + "-" + w + '.svg' + ")"
    #exec(draw_pic)
    d.save(file_name + '-' + wn +'.svg')

n_list = parse_line(line, file_name)

tuple_list = []
for w in n_list:
    d = get_overall_direction(w[1])
    xy = get_coordinates(w[0])
    tuple_list.append(node_tuple(w[0],w[1],d,xy[0],xy[1]))#五元组格式为（INT名，wire名，方向代号，x坐标，y坐标）
    #print((w[0],w[1],d,xy[0],xy[1]))

sorted_list = sort_nodes_list(tuple_list,tuple_list[0].direction)
#sorted_list = sort_nodes_list(n_list)
#ovdir = get_overall_direction(sorted_list)
#print(ovdir)
draw_flow(sorted_list)

    


'''
为上述的line手工绘制图形的代码应该是这样的：
d = schemdraw.Drawing()

d += (d0 := flow.Box(w=4, h=2).label('INT_X13Y100' + '\n' + 'EN5BEG0'))
d += flow.Arrow().right().at(d0.E).length(d.unit*2)
d += (d2 := flow.Box(w=4, h=2).anchor('W').label('*INT_X14Y100' + '\n' + 'EN5A0*'))

d += flow.Arrow().right().at(d2.E).length(d.unit*2)
d += (d3 := flow.Box(w=4, h=2).anchor('W').label('INT_X15Y100' + '\n' + 'EN5B0'))
d += flow.Arrow().right().at(d3.E).length(d.unit*2)

d += (d4 := flow.Box(w=4, h=2).anchor('W').label('INT_X16Y100' + '\n' + 'EN5MID0'))
d += flow.Arrow().up().at(d4.N).length(d.unit*2)
d += (d6 := flow.Box(w=4, h=2).anchor('S').label('INT_X16Y101' + '\n' + 'EN5C0'))
d += flow.Arrow().up().at(d6.N).length(d.unit*2)
d += (d8 := flow.Box(w=4, h=2).anchor('S').label('INT_X16Y102' + '\n' + 'EN5END0'))

d.draw()
'''