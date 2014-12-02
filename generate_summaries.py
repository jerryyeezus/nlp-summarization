import heapq

__author__ = 'yee'
from model import ParsingModel
from tree import RSTTree
from evaluation import Metrics
from os import listdir
from evalparser import parse
from buildtree import BFTbin

def calc_marcu(rst, summary_factor=0.2):
    top_scoring = [] # return list

    elem_units = []
    bft_nodelist = []
    p = 0

    # STEP 1: First, do BFT and add leaves (elementary units) to the list
    queue = [rst.tree]
    while queue:
        node = queue.pop(0)
        p += 1

        # Update total depth of tree
        rst.tree_depth = max(node.depth, rst.tree_depth)

        bft_nodelist.append(node)
        if node.lnode is not None:
            node.lnode.depth = node.depth + 1
            queue.append(node.lnode)
        if node.rnode is not None:
            queue.append(node.rnode)
            node.rnode.depth = node.depth + 1
        if node.rnode is None and node.lnode is None:
            #Leaf node
            #Add to elementary unit list
            elem_units.append(node)

    # STEP 2
    # Recursively calculate promotional sets for intermediate nodes by BFT again
    treenodes = BFTbin(rst.tree)
    treenodes.reverse()
    for node in treenodes:
        # Non-leaf
        if node.lnode is not None and node.rnode is not None:
            if node.lnode.prop == 'Nucleus':
                for elem in node.lnode.promotional:
                    node.promotional.add(elem)
            if node.rnode.prop == 'Nucleus':
                for elem in node.rnode.promotional:
                    node.promotional.add(elem)
        # Leaf
        else:
            node.promotional.add(node)


    # STEP 3
    # Calculate marcu score for each elementary unit based on promotional sets
    for elem in elem_units:
        for subtree in bft_nodelist:
            if elem in subtree.promotional:
                elem.marcu = rst.tree_depth - subtree.depth + 1
                heapq.heappush(top_scoring, (-elem.marcu, elem))
                break;
            if elem.marcu == 0:
                print "Shouldn't have happened."

    p = max(1, int(round(summary_factor * p)))

    # ret = heapq.nsmallest(p, top_scoring) ## TODO

    ret = []
    last_score = None
    # Pop off last two
    while p > 0 or last_score == top_scoring[0][1].marcu:
        tmp = heapq.heappop(top_scoring)[1]
        ret.append(tmp)
        last_score = tmp.marcu
        p = p - 1
    return ret

def generate_summaries(path):
    from os.path import join as joinpath
    # ----------------------------------------
    # Load the parsing model
    pm = ParsingModel()
    pm.loadmodel("parsing-model.pickle.gz")

    # ----------------------------------------
    # Read all files from the given path
    doclist = [joinpath(path, fname) for fname in listdir(path) if fname.endswith('.edus')]
    for fedus in doclist:
        pred_rst = parse(pm, fedus=fedus)
        top_scoring = calc_marcu(pred_rst, summary_factor=0.2)
        for edu in top_scoring:
            print edu.text

    # TODO order it by eduspan

