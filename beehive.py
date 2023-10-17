import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd


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