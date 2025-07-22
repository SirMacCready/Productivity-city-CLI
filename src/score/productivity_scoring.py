import json
import re
class ScoringEngine:
    """
    Classe de scoring d'activité à partir d'un fichier de configuration JSON.
    Chaque activité est scorée selon une regex associée à une catégorie et un multiplicateur.
    """

    def __init__(self, config_path="config_files.config.json"):
        self.categories = {}

        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # On prépare les catégories avec leurs regex précompilées
        for item in data.get("categories", []):
            name = item["name"]
            self.categories[name] = {
                "regex": re.compile(item["regex"], re.IGNORECASE) if item.get("regex") else None,
                "multiplier": item.get("multiplier", 1),
                "parent": item.get("parent")
            }

        # Valeur par défaut si aucune catégorie ne matche
        self.default_multiplier = self.categories.get("uncategorized", {}).get("multiplier", 1)

    def score(self, input_text: str, base_value: float) -> float:
        """
        Calcule le score d'une activité à partir du texte et de la valeur de base.
        :param input_text: texte à analyser (nom de l'activité)
        :param base_value: durée ou valeur de base
        :return: score final (float)
        """
        for cat_data in self.categories.values():
            if cat_data["regex"] and cat_data["regex"].search(input_text):
                return base_value * cat_data["multiplier"]

        return base_value * self.default_multiplier
