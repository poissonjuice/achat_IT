from datetime import datetime

class AssetIT:
    """
    Classe représentant un actif informatique générique.
    Concept Achat : Gestion du cycle de vie (Lifecycle Management).
    """
    def __init__(self, nom,prix_achat, date_achat, duree_vie_annees):
        self.nom = nom
        self.prix_achat = prix_achat
        self.date_achat = datetime.strptime(date_achat, "%Y-%m-%d")
        self.duree_vie_annees = duree_vie_annees
    
    def calculer_valeur_actuelle(self):
        """
        Calcule la valeur actuelle de l'actif en fonction de sa durée de vie.
        Utilise l'amortissement linéaire.
        """
        age_actif_jours = (datetime.now() - self.date_achat).days
        age_actif_annees = age_actif_jours / 365.25
        if age_actif_annees >= self.duree_vie_annees:
            return 0
        devaluation_annuelle = self.prix_achat / self.duree_vie_annees
        valeur_actuelle = self.prix_achat - (devaluation_annuelle * age_actif_annees)
        return round(max(valeur_actuelle, 0), 2)
    
    

