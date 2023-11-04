import heapq

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

class Node:
    def __init__(self, profit, weight, level, items):
        self.profit = profit
        self.weight = weight
        self.level = level
        self.items = items

    def __lt__(self, other):
        return self.profit > other.profit

def knapsack(items, capacity):
    queue = []
    heapq.heappush(queue, Node(0, 0, 0, []))

    max_profit = 0

    while queue:
        node = heapq.heappop(queue)

        if node.weight > capacity:
            continue

        if node.level == len(items):
            max_profit = max(max_profit, node.profit)
            continue

        next_node_profit = node.profit + items[node.level].profit
        next_node_weight = node.weight + items[node.level].weight
        next_node_items = node.items + [items[node.level]]

        heapq.heappush(queue, Node(next_node_profit, next_node_weight, node.level + 1, next_node_items))

        next_node_profit = node.profit
        next_node_weight = node.weight
        next_node_items = node.items[:]

        heapq.heappush(queue, Node(next_node_profit, next_node_weight, node.level + 1, next_node_items))

    return max_profit

def main():
    num_items = int(input("Enter the number of items: "))

    items = []

    for i in range(num_items):
        profit = int(input("Enter the profit of item {}: ".format(i + 1)))
        weight = int(input("Enter the weight of item {}: ".format(i + 1)))
        item = Item(profit, weight)
        items.append(item)

    capacity = int(input("Enter the capacity of the knapsack: "))

    max_profit = knapsack(items, capacity)

    print("The maximum profit that can be achieved is:", max_profit)

if __name__ == "__main__":
    main()
