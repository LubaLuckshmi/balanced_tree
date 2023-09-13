#Необходимо превратить собранное на семинаре дерево поиска в
#бинарное дерево с балансировкой, добавление, удалением элементов.

#При реализации балансировки бинарного дерева поиска,
# нужно изменить метод add_node() и добавить новый метод balance_tree()

class Node:
    def __init__(self, value = None, left = None, right = None):
        '''Конструктор класса Node '''
        self.value = value
        self.left = left 
        self.right = right

    def __str__(self):
        '''Строковое представление узла'''
        res = f'значение нашего узла: {self.value}'
        if self.left:
             res += f', значение левого:{self.left.value}'
        if self.right:
             res += f', значение правого: {self.right.value}'
        return res

class Tree:
    def __init__(self, root = None):
        '''Конструктор класса Tree'''
        self.root = root

    def search(self, node, data, parent = None):
        ''' Поиск значения в дереве
        Args:
        node: Текущий узел
        data: Искомое значение
        parent: Родительский узел текущего узла
        Returns:
        узел, родительский узел, найден ли элеемент
        '''
    
        if node is None:
            return None, parent, False
        
        if data == node.value:
            return node, parent, True
        
        if data > node.value:
            if node.right:
                return  self.search(self.node.right, data, node)

        if data < node.value:
            if node.left:
                self.search(node.left, data, node)
        return node, parent, False

    def add_node(self, value):
        '''Вставка нового значения в дерево'''
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_node(self.root, value)

    def _add_node(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_node(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_node(node.right, value)
                
    def delete_node(self, value):
        '''Удаление элемента из дерева'''
        self.root = self._delete_node(self.root, value)
        
    def _delete_node(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_node(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        '''ПОиск минимального значения'''
        while node.left:
            node = node.left
        return node
    
    def balance_tree(self):
        '''Создание сбалансированного дерева'''
        nodes = []
        self._in_order_traversal(self.root, nodes)  # Получаем значения узлов в порядке возрастания
        self.root = self._create_balanced_tree(nodes, 0, len(nodes)-1)  # Создаем сбалансированное дерево

    def _in_order_traversal(self, node, nodes):
        '''Обход дерева в порядке возрастания'''
        if node:
            self._in_order_traversal(node.left, nodes)
            nodes.append(node.value)
            self._in_order_traversal(node.right, nodes)

    def _create_balanced_tree(self, nodes, start, end):
        '''Создание нового сбалансированного дерева (вспомогательный)'''
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = Node(nodes[mid])
        
        node.left = self._create_balanced_tree(nodes, start, mid-1)
        node.right = self._create_balanced_tree(nodes, mid+1, end)

        return node


initial_node = Node(15)
tree_1 = Tree(initial_node)
tree_1.add_node(10) 
tree_1.add_node(20) 
tree_1.add_node(5) 
tree_1.add_node(13) 
tree_1.add_node(18) 
tree_1.add_node(25) 
print(tree_1)

tree_1.delete_node(13)
print(tree_1)

tree_1.balance_tree()
print(tree_1)
