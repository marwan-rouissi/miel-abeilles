import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import networkx as nx


class Hive:
    """Hive class to create a hive and run the genetic algorithm"""
    
    def __init__(self, flowers):
        self.generation = 1
        self.pos = (500, 500)
        self.flowers = flowers
        
        self.bees = []
        self.fitness_history = []
        self.h = []

    
    """generate population of bees"""
    def generate_population(self):
        for x in range(100):
            self.bees.append(Bee(self.flowers))
            self.bees[x].id = x+1
            self.bees[x].generation = self.generation
    

    """calculate fitness of bees by calculating the distance between each flower"""
    def evaluate(self): 
        for bee in self.bees:
            fitness_temp = 0
            for i in range(len(bee.genes)-1):
                fitness_temp += np.sqrt((bee.genes[i+1][0] - bee.genes[i][0])**2 + (bee.genes[i+1][1] - bee.genes[i][1])**2)
            fitness_temp += np.sqrt((bee.genes[-1][0] - bee.genes[0][0])**2 + (bee.genes[-1][1] - bee.genes[0][1])**2)
            bee.fitness = int(fitness_temp)


    """calculate fitness average of generation"""
    def evaluate_average(self):
        fitness_sum = 0
        for bee in self.bees:
            fitness_sum += bee.fitness
        fitness_average = fitness_sum / len(self.bees)
        self.fitness_history.append([int(fitness_average)])


    """select best bees and remove the others from the bees list
    add the best bee's fitness to the h list"""
    def selection(self):
        sorted_bees = sorted(self.bees, key=lambda x: x.fitness)
        self.bees = sorted_bees[:50]
        self.h.append(self.bees[0].fitness)


    """crossover of bees genes to create new bees genes
    add the new bees to the bees list
    remove the 2 selected bees from the bees list
    add the new bees to the bees list"""
    def crossover(self):
        parent_bees = self.bees.copy()
        babies = []
        self.generation += 1

        while len(babies) < 50:
            sorted_bees = sorted(parent_bees, key=lambda x: x.fitness)
            bee1 = sorted_bees[0]
            bee2 = sorted_bees[1]
            index = rd.randint(1, 25)
            new_bee1 = Bee(self.flowers)
            new_bee2 = Bee(self.flowers)
            new_bee1.id = len(babies) + 1
            new_bee2.id = len(babies) + 2
            new_bee1.generation = self.generation
            new_bee2.generation = self.generation
            new_bee1.genes = bee1.genes[:index]
            new_bee2.genes = bee2.genes[:index]
            for i in bee2.genes:
                if i not in new_bee1.genes:
                    new_bee1.genes.append(i)
            for i in bee1.genes:
                if i not in new_bee2.genes:
                    new_bee2.genes.append(i)
            new_bee1.parents = [(bee1.id, bee1.generation), (bee2.id, bee2.generation)]
            new_bee2.parents = [(bee1.id, bee1.generation), (bee2.id, bee2.generation)]
            new_bee1.parent1 = bee1
            new_bee1.parent2 = bee2
            new_bee2.parent1 = bee1
            new_bee2.parent2 = bee2

            """keep track of the genealogical tree of each bee"""
            new_bee1.genealogical_tree.append({(new_bee1.id, new_bee1.generation) : [(bee1.id, bee1.generation), (bee2.id, bee2.generation)]})
            new_bee2.genealogical_tree.append({(new_bee2.id, new_bee2.generation) : [(bee1.id, bee1.generation), (bee2.id, bee2.generation)]})

            babies.append(new_bee1)
            babies.append(new_bee2)
            parent_bees.remove(bee1)
            parent_bees.remove(bee2)
        self.bees.extend(babies)


    """mutation of 10 random bees by swapping 2 random genes of each bee
    this function is called every 10 generations"""
    def mutation(self):
        for _ in range(10):
            bee = rd.choice(self.bees)
            index1 = rd.randint(0, len(bee.genes)-1)
            index2 = rd.randint(0, len(bee.genes)-1)
            bee.genes[index1], bee.genes[index2] = bee.genes[index2], bee.genes[index1]


    """reconstruct the genealogical tree of the best bee by itereating through each bee's parents for 4 generations"""
    def recontruct_tree(self, bee):
        current_bee = bee
        tree = []
        temp = []
        temp.append(current_bee)
        n = 0
        # while temp != []:
        while n < 10:
            current_bee = temp[0]
            if current_bee.parent1 != None:
                temp.append(current_bee.parent1)
            if current_bee.parent2 != None:
                temp.append(current_bee.parent2)

            temp.remove(current_bee)
            if {(current_bee.id, current_bee.generation) : current_bee.parents} not in tree:
                try:
                    tree.append({(current_bee.id, current_bee.generation) : current_bee.parents})
                except:
                    tree.append({(current_bee.id, current_bee.generation) : None})
            n += 1
        return tree 


    """visualize best bee's path"""
    def visualize_best_bee(self):
        sorted_bees = sorted(self.bees, key=lambda x: x.fitness)
        best_bee = sorted_bees[0]
        plt.scatter(self.pos[0], self.pos[1], c='brown', s=150, marker="h", label='Hive', edgecolors='black')
        plt.scatter([i[0] for i in self.flowers], [i[1] for i in self.flowers], c='green', s=10, marker=".", label='Flowers', edgecolors='black')
        plt.scatter(best_bee.genes[0][0], best_bee.genes[0][1], c='green', s=150, marker=".", label='Start', edgecolors='black')
        plt.scatter(best_bee.genes[-1][0], best_bee.genes[-1][1], c='red', s=150, marker=".", label='End', edgecolors='black')
        for i in range(len(best_bee.genes)-1):
            plt.plot([best_bee.genes[i][0], best_bee.genes[i+1][0]], [best_bee.genes[i][1], best_bee.genes[i+1][1]], linestyle="dotted", c='yellow')

        plt.legend()
        plt.title("Best Bee Path")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    

    """visualize average fitness of generation"""
    def visualize_average_fitness(self):
        plt.plot(self.fitness_history)
        plt.title("Average Fitness of Generation")
        plt.xlabel("Generation")
        plt.ylabel("Average Fitness")
        plt.show()


    """visualize best bee through generations"""
    def visualize_best_bee_through_generations(self):
        plt.plot(self.h)
        plt.title("Best Bee through Generations")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.show()

    
    """visualize genealogical tree of best bee as a graph from the recontructed tree as a list of dictionaries
    each dictionary contains the bee's id and generation as a key and the bee's parents as a value"""
    def visualize_genealogical_tree_of_best_bee(self):
        G = nx.DiGraph()
        for i in self.recontruct_tree(self.bees[0]):
            key = list(i.keys())[0]
            value = list(i.values())[0]
            G.add_node(key)
            G.add_node(value[0])
            G.add_node(value[1])
        
        for i in self.recontruct_tree(self.bees[0]):
            key = list(i.keys())[0]
            value = list(i.values())[0]
            if value != None:
                G.add_edge(key, value[0])
                G.add_edge(key, value[1])

        first_key = list(self.recontruct_tree(self.bees[0])[0].keys())[0]
        root_node = first_key

        node_colors = ['red' if node == root_node else 'orange' for node in G.nodes()]

        """keep the root node at the bottom of the graph"""
        pos = nx.spring_layout(G, k=50, iterations=50, scale=1, center=(0,0))
        pos[root_node][1] = -2.0
        pos[root_node][0] = 0.0
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, arrows=True, arrowstyle='->', arrowsize=20, width=1, linewidths=2, font_size=10, font_color='black', font_weight='bold')


        """legend for the graph
        red = best bee from last generation
        blue = other bees
        node = (id, generation)"""
        plt.scatter([], [], c='red', s=150, marker=".", label='Last Bee', edgecolors='black')
        plt.scatter([], [], c='orange', s=150, marker=".", label='Other Bees', edgecolors='black')
        
        plt.legend()

        """add labels to edges"""
        edge_labels = {edge: "Parent" for edge in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5, font_color='black')

        plt.show()



class Bee(Hive):
    """Bee class to create a bee
    a bee is characterized by:
    - an id
    - a name
    - a list of genes
    - a fitness
    - a generation"""

    def __init__(self, flowers):
        super().__init__(flowers)
        self.id = None
        self.genes = rd.sample(flowers, len(flowers))
        self.fitness = 0
        self.parent1 = None
        self.parent2 = None
        self.parents = []

        self.genealogical_tree = []