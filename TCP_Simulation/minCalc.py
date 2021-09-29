
from math import *
from copy import *

class edge:
    def __init__(self, dest, source, dist):
        self.dest = dest
        self.source = source
        self.dist = dist

class map:
    def __init__(self, state, pathCost):
        self.state = state
        self.pathCost = pathCost

def pathCalc(destination, source):
    file = open("map.txt", "r")
    #print(file.read())

    line = file.read()
    #print(line)
    line_split = line.split("\n")
    #print(line_split)
    edge_list = []
    state_list_temp = []
    node_list = []
    node_list.append(source)

    for x in range(0, len(line_split)):
        line_row = line_split[x].split()
        #print(line_row)
        edge_list.append(edge(line_row[0], line_row[1], float(line_row[2])))
        edge_list.append(edge(line_row[1], line_row[0], float(line_row[2])))
        state_list_temp.append(line_row[0])
        state_list_temp.append(line_row[1])

    state_list = sorted((set(state_list_temp)))
    #print(state_list)

    #for x in range(0, len(edge_list)):
     #   print("[%s %s %s]" % (edge_list[x].dest, edge_list[x].source, edge_list[x].dist))

    #print(edge_list[0].dist)

    map_list = []
    for x in range(0, len(state_list)):
        map_list.append(map([], 0))

    for x in range(0, len(state_list)):

        end = state_list[x]
        temp_map = []
        temp_map.append(map([source], 0))
        while source == temp_map[0].state[0] and end != temp_map[0].state[-1]:
            expandHere = temp_map[0].state[-1]
            #print(temp_map[0].state)

            for y in range(0, len(edge_list)):
                if(edge_list[y].source is expandHere and edge_list[y].dest not in deepcopy(temp_map[0].state)):
                    temp_map.append(deepcopy(temp_map[0]))
                    #temp_map[-1].state = temp_map[0].state
                    temp_map[-1].state.append(edge_list[y].dest)
                    temp_map[-1].pathCost = float(deepcopy(temp_map[0].pathCost)) + float(edge_list[y].dist)
                    #print(deepcopy(temp_map[0].pathCost))
                    #print(edge_list[y].dist)
                    #print("in for loop %s" % y)
                    #print(temp_map[-1].state)
                    #print(temp_map[-1].pathCost)
                    #print(temp_map[0].pathCost)
                    #print("temp_map length: %s" % len(temp_map))

            #print("------ %s" % temp_map[0].state)
            del temp_map[0]
            temp_map = sorted(temp_map, key=lambda temp_map: temp_map.pathCost)
            #print("P----- %s" % temp_map[0].state)

            #print(temp_map[0].pathCost)

        map_list[x].state.append(deepcopy(temp_map[0].state))
        map_list[x].pathCost = deepcopy(temp_map[0].pathCost)


    print("From %s to:" % source)
    for x in range(0, len(map_list)) :
        print("%s\t%s distance: %s" % (state_list[x], map_list[x].state[0], map_list[x].pathCost))
        #print("%s\t%s" % (map_list[x].state[0][0], map_list[x].state[0][-1]))
        if (map_list[x].state[0][0] == source and map_list[x].state[0][-1] == destination):
            flagThis = int(x)

    if(source == destination):
        return map_list[flagThis].state[0][0]
    else:
        return map_list[flagThis].state[0][1]



def main():
    print("hi\n")
    source = "A"
    desti = "E"
    print(pathCalc(desti, source))





if ( __name__ == "__main__" ) :
  main()
