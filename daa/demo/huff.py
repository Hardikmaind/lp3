class Node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=""

def print_nodes(node,val=""):
    newvaul=val+str(node.huff)
    if node.left:
        print_nodes(node.left,newvaul)
    if node.right:
        print_nodes(node.right,newvaul)
    if not  node.left and not node.right:
        print(f"{node.symbol}=> {newvaul}") 
def build_huffman_tree(chars,freq):
    nodes = [Node(freq[x],chars[x])for x in range(len(chars))]
    while len(nodes)>1:
        nodes =sorted(nodes,key=lambda x:x.freq)
        left=nodes[0]
        right=nodes[1]
        left.huff=0
        left.huff=1
        newnode=Node(left.freq+right.freq,left.symbol+right.symbol,left,right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
    return nodes[0]

def huffmanmenu():
    while True:
        print("huffman encoding")
        print("1. huffman coding")
        print("2.ext")
        choice=(int)(input("enter your choicec"))
        if choice==1:
            chars=input("enter the  characters").split()
            freq=[int(x) for x in input("enter the freqencies").split()]
            if len(chars)!=len(freq):
                print("error:number of character and freaquencies")
                continue
            root=build_huffman_tree(chars,freq)
            print_nodes(root)
        elif choice==2:
            print("exiting the program")
            break
        else:
            print("invalid choice")
            
if __name__=="__main__":
    huffmanmenu()
            