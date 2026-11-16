class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def roar(self):
        return f"{self.name} the {self.species} roars loudly!"

    def eat(self, food):
        if food.lower() in self.diet:
            return f"{self.name} is eating {food}."
        else:
            return f"{self.name} does not eat {food}."

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.species} that eats {', '.join(self.diet)}."

dino1 = Dinosaur("Rex", "Tyrannosaurus Rex", ["meat"], 12)

print(dino1.info())