# /bin/python
class BinTree():
    def __init__(self, root=''):
        self.left = None
        self.right = None
        self.root = root

    def LeftChild(self):
        return self.left

    def RightChild(self):
        return self.right

    def setValue(self, value):
        self.root = value

    def getValue(self):
        return self.root

    def insRight(self, node):
        if self.right == None:
            self.right = BinTree(node)
        else:
            self.RightChild().insRight(node)
    def insLeft(self, node):
        if self.left == None:
            self.left = BinTree(node)
        else:
            self.LeftChild().insLeft(node)


    def valPush(self, food):
       self.setValue(food[0])
       food=food[1:]
       leftpart = ''
       rightpart = ''
       i=0
       while len(leftpart)+len(rightpart)<len(food)-2:
            leftpart+=food[(2**i)*2-2:(2**i)*2+(2**i)-2]
            rightpart += food[(2**i)*2+(2**i)-1:((2**i)*2+(2**i)-1)+i**2]
            i+=1
       self.left = BinTree(leftpart)
       self.right = BinTree(rightpart)


def TreeOut(tree):
    if tree != None:
        if tree.LeftChild==None:
            return([tree.root])
        else:
            return([TreeOut(tree.LeftChild()),TreeOut(tree.RightChild())])



# def TreeOut(tree):
#     if tree != None:
#         print(TreeOut(tree.LeftChild()))
#         print(tree.getValue())
#         print(TreeOut(tree.RightChild()))


def TreeOutABCD(tree):
    if tree != None:
        print(tree.getValue,end='')
        lefttree=tree.LeftChild()
        righttree=tree.RightChild()
        print(lefttree.root)
        print(righttree.root)





tree_pipeline = 'ABCDEFG12345678'

testtree = BinTree()

testtree.valPush(tree_pipeline)

TreeOut(testtree)
