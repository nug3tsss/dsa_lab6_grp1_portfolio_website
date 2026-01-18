from flask import Flask, render_template, request, redirect, url_for
import os
import ast
from collections import deque
from modules.queue import Queue
from modules.dequeue import DeQueue
from modules.binary_tree import BinaryTree
from modules.binary_search_tree import BinarySearchTree, Node
from modules.breadth_first_search import bfs_shortest_path, adj
from modules.merge_sort import MergeSort
from modules.selection_sort import SelectionSort
from modules.insertion_sort import insertion_sort
from modules.quick_sort import QuickSort

app = Flask(__name__)

queue_structure = Queue()
deque_structure = DeQueue()
binary_tree = BinaryTree()
bst = BinarySearchTree()

@app.route('/')
def home_redirect():
    return redirect(url_for('index'))

# Home page
@app.route('/home')
def index():
    index_data = {
        "message": "SEVEN11",
        "message_1": "SEVEN members of Group ONE, united as ONE.",
        "message_2": "Welcome to the official page of Group ONE's programming works."
    }
    return render_template('home.html', index=index_data, active_page='home')

# Project page
@app.route('/works')
def works():
    return render_template('works.html',  active_page='works')

# Profile and Contact page
@app.route('/contacts')
def members_contact():
    people = [
    {
        "name": "Mark Christian Abucejo",
        "image": "static/images/members/mark.jpg",
        "links": {
                "facebook": "https://www.facebook.com/mrkchrstnsbcj",
                "email": "mailto:abucejomark11905@gmail.com",
                "github": "https://github.com/nug3tsss",
            }
    },
    {
        "name": "Zy Banez",
        "image": "static/images/members/zy.jpg",
        "links": {
                "facebook": "https://www.facebook.com/zyescote.banez.5",
                "email": "mailto:zyescotebanez@gmail.com",
                "github": "https://github.com/ITZMEXYZ",
            }
    }, 
    {
        
            "name": "Kyle Isaac Celin",
            "image": "static/images/members/kyle.png",
            "links": {
                "facebook": "https://www.facebook.com/cee.the.lin.e",
                "email": "mailto:celinkyleisaac@gmail.com",
                "github": "https://github.com/ceetheline",
        }
    }, 
    {
        
            "name": "John Luke Fabillan",
            "image": "static/images/members/jl.jpg",
            "links": {
                "facebook": "https://facebook.com/johnluke.fabillan",
                "email": "mailto:jlfabillan@gmail.com",
                "github": "https://github.com/JLFabillan",
        }
    }, 
    {
        
            "name": "Princess Sophia Manalo",
            "image": "static/images/members/sophia.jpg",
            "links": {
                "facebook": "https://www.facebook.com/soapymk/",
                "email": "mailto:manaloprincesssophia@gmail.com",
                "github": "https://github.com/S0PHIA18",
        }
    }, 
    {
        
            "name": "Isaac Christian Pelingen",
            "image": "static/images/members/isaac.jpg",
            "links": {
                "facebook": "https://www.facebook.com/share/1FmtJqYkC4/",
                "email": "mailto:pelingenisaac@gmail.com",
                "github": "https://github.com/xiin112",
        }
    }, 
    {
        
            "name": "Gian Carlos Tumanan",
            "image": "static/images/members/GIAN.png",
            "links": {
                "facebook": "https://facebook.com/giancarlos.tumanan",
                "email": "mailto:giancarlostumanan@gmail.com",
                "github": "https://github.com/GIANT0808",
        }
    }
    ]
    
    return render_template("contacts.html", people=people)


# Queue visualizer page
@app.route('/works/queue-visualizer', methods=['GET', 'POST'])
def queue_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enqueue" in request.form:
            queue_structure.enqueue(value)
        elif "dequeue" in request.form:
            queue_structure.dequeue()

    if request.args.get("dequeue"):
        queue_structure.dequeue()

    return render_template(
        "queuevisualizer.html",
        items=queue_structure.get_items(),
        active_page="works"
    )

# DeQueue visualizer page
@app.route('/works/dequeue-visualizer', methods=['GET', 'POST'])
def dequeue_visualizer():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "left":  # Insert Left
            value = request.form.get("value")
            if value:
                deque_structure.insert_left(value)
        elif action == "right": 
            value = request.form.get("value")
            if value:
                deque_structure.insert_right(value)
        elif action == "remove_left":
            deque_structure.remove_left()
        elif action == "remove_right":
            deque_structure.remove_right()

    return render_template(
        "dequeuevisualizer.html",
        items=deque_structure.get_items(),
        active_page="works")

# Binary Tree visualizer page
@app.route('/works/binary-tree-visualizer', methods=['GET', 'POST'])
def binary_tree_visualizer():
    global binary_tree

    tree_items = ""

    if request.method == "POST":
        value = request.form.get("value")
        target = request.form.get("target")

    if "insert-root" in request.form and value:
        binary_tree.insert_root(value)

    if "insert-left" in request.form and value and target:
        binary_tree.insert_left(binary_tree.search(target), value)

    if "insert-right" in request.form and value and target:
        binary_tree.insert_right(binary_tree.search(target), value)
    
    if "delete-node" in request.form and target:
        binary_tree.delete_node(target)
    
    if "reset-tree" in request.form:
        binary_tree = BinaryTree()
    
    if "preorder" in request.form:
        tree_items = binary_tree.preorder_traversal(binary_tree.root, "")

    if "inorder" in request.form:
        tree_items = binary_tree.inorder_traversal(binary_tree.root, "")
        
    if "postorder" in request.form:
        tree_items = binary_tree.postorder_traversal(binary_tree.root, "")

    # use the new serializer that produces a list of dicts with index/parent/level/value
    tree_nodes = binary_tree.serialize_for_visualizer()

    return render_template(
        "binarytreevisualizer.html",
        tree_items=tree_items.split(),
        tree_nodes=tree_nodes,
        tree_root=binary_tree.root,
        active_page="works"
    )

# Binary Search Tree Visualizer
@app.route('/works/bst-visualizer', methods=['GET', 'POST'])
def bst_visualizer():
    global bst
    output = ""
    search_value = None
    max_value = None
    height_value = None
    height_path = []


    if request.method == "POST":
        value = request.form.get("value")
        try:
            value = int(value) if value else None
        except ValueError:
            value = None

        # INSERT
        if "insert" in request.form and value is not None:
            bst.insert(value)
            output = f"Inserted {value}."

        # SEARCH
        elif "search" in request.form and value is not None:
            node = bst.search(bst.root, value)
            if node:
                output = f"Value {value} found in the tree."
                search_value = value
            else:
                output = f"Value {value} not found."

        # DELETE
        elif "delete" in request.form and value is not None:
            bst.root = bst.delete(bst.root, value)
            output = f"Deleted {value} (if it existed)."

        # GET MAX
        elif "max" in request.form:
            max_val = bst.get_max_value(bst.root)
            output = f"Max value in tree: {max_val}" if max_val is not None else "Tree is empty."
            max_value = max_val

        # GET HEIGHT
        elif "height" in request.form:
            try:
                value = int(value)
            except:
                value = None

            if value is not None:
                height, path = bst.get_height_with_path(value)

                if height is None:
                    output = f"Node {value} not found."
                    height_value = None
                    height_path = []
                else:
                    output = f"Height of node {value}: {height}"
                    height_value = height
                    height_path = path
            else:
                output = "Please enter a valid number."
                height_value = None
                height_path = []


        # RESET
        elif "reset" in request.form:
            bst = BinarySearchTree()
            output = "Tree has been reset."

    # Serialize the tree for frontend visualizer
    tree_nodes = []
    if bst.root:
        # Flatten the tree to a list of dicts for your HTML
        def serialize(node, index=0, level=0, parent=None):
            if node is None:
                return []
            data = [{
                "value": node.value,
                "index": index,
                "level": level,
                "parent": parent
            }]
            data += serialize(node.left, index*2+1, level+1, index)
            data += serialize(node.right, index*2+2, level+1, index)
            return data
        tree_nodes = serialize(bst.root)

    return render_template(
        "binarysearchtreevisualizer.html",
        output=output,
        tree_nodes=tree_nodes,
        search_value=search_value,
        max_value=max_value,
        height_value=height_value,
        height_path=height_path,
        active_page="works"
    )

### Breadth-First Search
@app.route('/works/bfs', methods=['GET', 'POST'])
def bfs_page():
    global bfs_shortest_path
    # line colors
    line_colors = {
        "LRT-1": "#00FF00",
        "LRT-2": "#1E90FF",
        "MRT-3": "#FFFF00"
    }

    def get_line_color(station):
        for line in line_colors:
            if line in station:
                return line_colors[line]
        return "#FFFFFF"

    path = []
    start = goal = ""
    if request.method == "POST":
        start = request.form.get("start")
        goal = request.form.get("goal")
        path = bfs_shortest_path(adj, start, goal)

    return render_template("breadthfirst.html", path=path, start=start, goal=goal, get_color=get_line_color, adj=adj)

# Sorting Algorithms Section
@app.route('/works/sorting-algorithms')
def sorting_algorithm():
    return render_template('sortingalgorithms.html', active_page='sorting-algorithms')

# Bubble Sort Visualizer
@app.route("/works/sorting-algorithms/bubble-sort-visualizer", methods=["GET", "POST"])
def bubble_sort_page():
    steps = None
    if request.method == "POST":
        data = request.form.get("array")
        algorithm = request.form.get("algorithm")
        if data and algorithm == "bubble":
            arr = list(map(int, data.split(",")))
            steps = bubble_sort(arr)
    return render_template("bubblesortvisualizer.html", steps=steps)

# Merge Sort Visualizer
merge_sort_array = []
@app.route('/works/sorting-algorithms/merge-sort-visualizer', methods=['GET', 'POST'])
def merge_sort_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enter" in request.form:
            merge_sort_array.append(value)
        elif "sort" in request.form:
            MergeSort(merge_sort_array)

    return render_template(
        "mergesortvisualizer.html",
        items=merge_sort_array,
        active_page="works"
    )

# Selection Sort Visualizer
selection_sort_array = []

@app.route('/works/sorting-algorithms/selection-sort-visualizer', methods=['GET', 'POST'])
def selection_sort_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enter" in request.form:
            if value:
                selection_sort_array.append(int(value))
        elif "sort" in request.form:
            SelectionSort(selection_sort_array)

    return render_template(
        "selectionsortvisualizer.html",
        items=selection_sort_array,
        active_page="works"
    )

# Insertion Sort Visualizer
@app.route("/works/sorting-algorithms/insertion-sort-visualizer", methods=["GET", "POST"])
def insertion_sort_page():
    sorted_list = None
    original_list = None
    error = None

    if request.method == "POST":
        user_input = request.form.get("numbers")

        try:
            # Convert user input into list of integers
            original_list = [int(x.strip()) for x in user_input.split(",")]
            sorted_list = insertion_sort(original_list.copy())
        except ValueError:
            error = "Please enter only numbers separated by commas."

    return render_template(
        "insertionsortvisualizer.html",
        original_list=original_list,
        sorted_list=sorted_list,
        error=error,
        active_page="works"
    )

# Quick Sort Visualizer
quick_sort_array = []
@app.route('/works/sorting-algorithms/quick-sort-visualizer', methods=['GET', 'POST'])
def quick_sort_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enter" in request.form:
            quick_sort_array.append(value)
        elif "sort" in request.form:
            sorter = QuickSort(quick_sort_array)
            quick_sort_array[:] = sorter.sorted_array

    return render_template(
        "quicksortvisualizer.html",
        items=quick_sort_array,
        active_page="works"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


