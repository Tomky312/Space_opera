import pyglet
import resources
import random

class Asteroid:
    def __init__(self, asteroid_cluster, world_pos, mass):
        # chain setup
        self.asteroid_cluster = asteroid_cluster
        self.asteroid_cluster.asteroids.append(self)
        # ---
        self.world_pos = world_pos
        self.mass = mass

        if self.mass >= 3000:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_medium)
        if self.mass >= 8000:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_large)
        else:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_small)

        self.chemical_fuel_resources = 0
        self.fission_fuel_resources = 0
        self.fusion_fuel_resources = 0
        self.common_material_resources = 0
        self.rare_material_resources = 0

        self.generate_composition()

    def update(self, TICK):
        pass

    def generate_composition(self):
        # distribution table (% of resource-rich mass)
        distributions = {
            "C-Type": [70, 5, 5, 15, 5],  # Carbonaceous
            "S-Type": [10, 5, 5, 70, 10],  # Silicaceous
            "M-Type": [5, 5, 5, 35, 50],  # Metallic
            "R-Type": [5, 60, 5, 5, 25],  # Radioactive
            "I-Type": [25, 2, 65, 5, 3],  # Icy
        }

        # richness: 5–10% of mass
        richness = random.uniform(0.05, 0.10)
        resource_mass = self.mass * richness

        # split resource_mass into categories
        dist = distributions[self.asteroid_cluster.type]
        self.chemical_fuel_resources = resource_mass * dist[0] / 100
        self.fission_fuel_resources = resource_mass * dist[1] / 100
        self.fusion_fuel_resources = resource_mass * dist[2] / 100
        self.common_material_resources = resource_mass * dist[3] / 100
        self.rare_material_resources = resource_mass * dist[4] / 100