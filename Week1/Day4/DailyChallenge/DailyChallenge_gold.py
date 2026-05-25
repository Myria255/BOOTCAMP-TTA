import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])
    
    def mutate(self):
        self.value = 1 - self.value

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
    
    def mutate(self):
        num_to_mutate = random.randint(1, 10)
        genes_to_mutate = random.sample(self.genes, num_to_mutate)
        for gene in genes_to_mutate:
            gene.mutate()

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        num_to_mutate = random.randint(1, 10)
        chromosomes_to_mutate = random.sample(self.chromosomes, num_to_mutate)
        for chromosome in chromosomes_to_mutate:
            chromosome.mutate()   

dna = DNA()
print("Before mutation:")
for i, chromosome in enumerate(dna.chromosomes):
    gene_values = [gene.value for gene in chromosome.genes]
    print(f"Chromosome {i + 1}: {gene_values}")
dna.mutate()
print("\nAfter mutation:")  
for i, chromosome in enumerate(dna.chromosomes):
    gene_values = [gene.value for gene in chromosome.genes]
    print(f"Chromosome {i + 1}: {gene_values}")
    
class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment  # Probabilité de mutation
    
    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()
    
    def is_all_ones(self):
        return all(gene.value == 1 for chromosome in self.dna.chromosomes for gene in chromosome.genes)

# Simulation
def simulate_until_all_ones():
    population_size = 100
    environment = 0.8  # Probabilité de mutation
    organisms = [Organism(DNA(), environment) for _ in range(population_size)]
    generations = 0

    while True:
        generations += 1
        for organism in organisms:
            organism.mutate()
            if organism.is_all_ones():
                return generations

# Exécuter la simulation
result = simulate_until_all_ones()
print(f"Nombre de générations pour atteindre un ADN entièrement composé de 1 : {result}")