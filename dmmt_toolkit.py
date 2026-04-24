# BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None

    def insert(self,root,val):
        if root is None:
            return Node(val)

        if val<root.data:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)

        return root

    def search(self,root,key):
        if root is None:
            return False

        if root.data==key:
            return True

        if key<root.data:
            return self.search(root.left,key)

        return self.search(root.right,key)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def minNode(self,node):
        temp=node
        while temp.left is not None:
            temp=temp.left
        return temp

    def delete(self,root,key):
        if root is None:
            return root

        if key<root.data:
            root.left=self.delete(root.left,key)

        elif key>root.data:
            root.right=self.delete(root.right,key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp=self.minNode(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)

        return root


# GRAPH

class Graph:
    def __init__(self):
        self.g={
            "A":[("B",2),("C",4)],
            "B":[("D",7),("E",3)],
            "C":[("E",1),("F",8)],
            "D":[("F",5)],
            "E":[("D",2),("F",6)],
            "F":[]
        }

    def show(self):
        print("\nAdjacency List")
        for i in self.g:
            print(i,"->",self.g[i])

    def bfs(self,start):
        visited=[]
        queue=[start]

        while queue:
            node=queue.pop(0)

            if node not in visited:
                visited.append(node)

                for n,w in self.g[node]:
                    if n not in visited:
                        queue.append(n)

        print("BFS:",visited)

    def dfs(self,start,visited=None):
        if visited is None:
            visited=[]

        if start not in visited:
            visited.append(start)

            for n,w in self.g[start]:
                self.dfs(n,visited)

        return visited


# HASH TABLE

class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[]

        for i in range(size):
            self.table.append([])

    def hashfun(self,key):
        return key%self.size

    def insert(self,key,val):
        index=self.hashfun(key)
        self.table[index].append((key,val))

    def get(self,key):
        index=self.hashfun(key)

        for k,v in self.table[index]:
            if k==key:
                return v

    def delete(self,key):
        index=self.hashfun(key)

        for i in range(len(self.table[index])):
            if self.table[index][i][0]==key:
                del self.table[index][i]
                break

    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])


# MAIN

print("BST OPERATIONS")

b=BST()

nums=[50,30,70,20,40,60,80]

for x in nums:
    b.root=b.insert(b.root,x)

print("Initial Inorder:")
b.inorder(b.root)

print("\nSearch 20 =",b.search(b.root,20))
print("Search 90 =",b.search(b.root,90))

b.root=b.delete(b.root,20)
print("\nAfter deleting 20")
b.inorder(b.root)

b.root=b.insert(b.root,65)

b.root=b.delete(b.root,60)
print("\nAfter deleting 60")
b.inorder(b.root)

b.root=b.delete(b.root,30)
print("\nAfter deleting 30")
b.inorder(b.root)



print("\n\nGRAPH OPERATIONS")

g=Graph()

g.show()

g.bfs("A")

print("DFS:",g.dfs("A"))



print("\nHASH TABLE")

h=HashTable(5)

keys=[10,15,20,7,12]

for i in keys:
    h.insert(i,"Value"+str(i))

h.display()

print("Get 10 =",h.get(10))
print("Get 15 =",h.get(15))
print("Get 12 =",h.get(12))

h.delete(15)

print("\nAfter deleting 15")
h.display()