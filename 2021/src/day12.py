from common import get_input
import collections

test_input_1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

test_input_2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

test_input_3 = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW',
]

class Cave:
    def __init__(self, id):
        self.id = id
        if self.id.upper() == self.id:
            self.big = True
        else:
            self.big = False
        self.connections = set()
    
    def connect(self, destination):
        self.connections.add(destination)

class CaveGraph:
    def __init__(self, input):
        self.caves = {}
        for line in input:
            nodes = line.split('-')
            for i,n in enumerate(nodes):
                if not n in self.caves.keys():
                    self.caves[n] = Cave(n)
                self.caves[n].connect(nodes[i-1])
        self.routes = []
        self.find_all_routes()
    
    def is_valid_step(self, route, connection):
        if self.caves[connection].big:
            return True
        elif not connection in route:
            return True
        else:
            if connection in ['start','end']:
                return False
            small_counter = collections.Counter([c for c  in route if c.lower() == c])
            return small_counter.most_common()[0][1] == 1

    def route_step(self):
        if len(self.routes) == 0:
            self.routes.append([self.caves['start'].id])
            return True
        new_routes = []
        for route in self.routes:
            last_node = self.caves[route[-1]]
            if self.caves[route[-1]].id == self.caves['end'].id:
                #print(f'route {route} is already complete')
                new_routes.append(route)
                continue
            possible_branches = [conn for conn in last_node.connections if self.is_valid_step(route,conn)]
            if len(possible_branches) == 0:
                # dead route
                continue
            elif len(possible_branches) == 1:
                # only one valid way to go
                #print(f'extending route to {route+possible_branches}')
                new_routes.append(route + possible_branches)
            else:
                for b in possible_branches:
                    #print(f'adding branch {route+[b]}')
                    new_routes.append(route + [b])
        if len(self.routes) != len(new_routes):
            # routes have changed, need to keep going
            self.routes = new_routes
            return True
        # route count has remained constant, we're done
        return False

    def find_all_routes(self):
        while self.route_step():
            continue
        return self
    
    def route_count(self):
        return len(self.routes)
    
test1 = CaveGraph(test_input_1)
test2 = CaveGraph(test_input_2)
test3 = CaveGraph(test_input_3)
realdeal = CaveGraph(get_input(12))

print(test1.route_count(), test2.route_count(), test3.route_count(), realdeal.route_count())
