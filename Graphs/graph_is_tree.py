#__author__ = ritvikareddy2
#__date__ = 2019-02-09

from collections import defaultdict

def is_tree(graph):
    visited = defaultdict(lambda: False)

    # if is_cyclic()


    return ''






if __name__ == '__main__':
    graph = {
        0: [2, 3],
        1: [0, 4],
        2: [4],
        3: [],
        4: []
    }
    print(is_tree(graph))