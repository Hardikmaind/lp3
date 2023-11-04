class Node:
    """A Huffman Tree Node"""
    def __init__(self, freq_, symbol_, left_=None, right_=None):
        # frequency of symbol
        self.freq = freq_
        # symbol name (character)
        self.symbol = symbol_
        # node left of current node
        self.left = left_
        # node right of current node
        self.right = right_
        # tree direction (0/1)
        self.huff = ""

def print_nodes(node, val=""):
    """Utility function to print Huffman codes for all symbols in the newly created Huffman tree"""
    # Huffman code for the current node
    new_val = val + str(node.huff)
    # if the node is not an edge node, then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # if the node is an edge node, then display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

def build_huffman_tree(chars, freq):
    nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    return nodes[0]

def huffman_menu():
    while True:
        print("\nHuffman Encoding Menu:")
        print("1. Encode")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            chars = input("Enter characters (e.g., a b c d e f): ").split()
            freq = [int(x) for x in input("Enter frequencies (e.g., 5 9 12 13 16 45): ").split()]
            if len(chars) != len(freq):
                print("Error: Number of characters and frequencies should match.\n")
                continue
            root = build_huffman_tree(chars, freq)
            print("Huffman Encoding:")
            print_nodes(root)  # Corrected this line
            print("\n")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 to Encode or 2 to Exit.")

if __name__ == "__main__":
    huffman_menu()
