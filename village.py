from score.score_checker import score_checking 

class Village : 
    def __init__(self, data=None):
        if data is None:
            data = {}  # Assure une base dictionnaire

        self.name = data.get("name", "Unnamed Village")

        # Stockage des infrastructures
        self.infrastructures = {
            "ext_roads": data.get("ext_roads", {"value": 1, "citizen_added": 2}),
            "farms": data.get("farms", {"value": 1, "citizen_added": 10}),
        }

        # Calcul de la capacité d'accueil initiale
        self.citizens = self.calculate_capacity()
        self.houses = self.citizens // 4  # correction logique : nombre de maisons entières

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
            if data is None :
                new_village = cls()
                json.dump(new_village,file)
        return cls(data)
        