from beehive import *

"""function to convert the csv file into a list of flower's positions"""
def convert_csv_to_list(file):
    flowers_list = pd.read_csv(file)
    flowers_list = np.array(flowers_list)
    flowers_list = flowers_list.tolist()
    return flowers_list

"""create a list of flowers and a hive """
flowers_list = convert_csv_to_list('flowers_position.csv')
hive = Hive(flowers_list)


"""main function to run the genetic algorithm
generate the first population of bees
run the genetic algorithm for x generations doing the following:
- evaluate the fitness of the bees
- evaluate the average fitness of the generation
- select the best bees and remove the others
- crossover the best bees to create new bees with new genes and add them to the bees list
- mutate the bees every 10 generations to prevent the algorithm from getting stuck in a local optimum
- visualize the best bee, the average fitness and the best bee of the last generation"""
def GA():
    
    hive.generate_population()

    for x in range(1000):
        hive.evaluate()
        hive.evaluate_average()
        hive.selection()
        hive.crossover()
        if x % 10 == 0:
            hive.mutation()

    """Comment lines 39-41 if you don't want to visualize the results
    This way you can see the exact time of the execution of the algorithm"""
  
    # hive.visualize_best_bee()
    # hive.visualize_best_bee_through_generations()
    # hive.visualize_average_fitness()


if __name__ == '__main__':
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    GA()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime').print_stats(20)