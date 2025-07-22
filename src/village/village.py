from score_checker import main 

class village : 
    def __init__(self, data=None):
        data = data or self.DEFAULT_DATA

        self.name = data.get("name", "Unnamed Village")

        # Stockage des infrastructures
        self.infrastructures = {
            "ext_roads": data.get("ext_roads", {"value": 1, "citizen_added": 2}),
            "farms": data.get("farms", {"value": 1, "citizen_added": 10}),
        }

        # Calcul de la capacité d'accueil initiale
        self.citizens = self.calculate_capacity()
        self.houses = self.citizens % 4

    def calculate_capacity(self):
        """
        Calcule la capacité totale de citoyens en fonction des infrastructures.
        """
        total = 0
        for name, info in self.infrastructures.items():
            total += info["value"] * info["citizen_added"]
        return total
    
    @classmethod
    def from_json(cls,filepath) :
        import json
        with open(filepath) as file :
            data = json.load(file)
        return cls(data)
    
    def display() : 
        print(f"Welcome to {self.name}")
        print(f"population : {len(self.citizens)}")