from datetime import datetime

class AssetIT:
    """
    Classe représentant un actif informatique générique.
    Concept Achat : Gestion du cycle de vie (Lifecycle Management).
    """
    def __init__(self, nom : str,prix_achat : float, date_achat : str, duree_vie_annees : int): #def __init__ est le constructeur de la classe
        self.nom = nom
        self.prix_achat = prix_achat
        self.duree_vie_annees = duree_vie_annees

        try:
            self.date_achat = datetime.strptime(date_achat, "%Y-%m-%d")
        except ValueError:
            print(f"Erreur: La date pour '{nom}' n'est pas valide. Utilisation de la date du jour.")
            self.date_achat = datetime.now()
    

    def calculer_valeur_actuelle(self):
        """
        Calcule la valeur actuelle de l'actif en fonction de sa durée de vie.
        Utilise l'amortissement linéaire.
        """
        age_actif_jours = (datetime.now() - self.date_achat).days
        age_actif_annees = age_actif_jours / 365.25

        if age_actif_annees >= self.duree_vie_annees:
            return 0 #pour eviter les valeurs negatives
        
        devaluation_annuelle = self.prix_achat / self.duree_vie_annees
        valeur_actuelle = self.prix_achat - (devaluation_annuelle * age_actif_annees)
        return round(max(valeur_actuelle, 0), 2) #pour eviter les valeurs negatives et arrondir a 2 decimales
    
    def __str__(self):
        valeur = self.calculer_valeur_actuelle()
        date_propre = self.date_achat.strftime("%d/%m/%Y")
        return f"Matériel : {self.nom} | Acheté le : {date_propre} | Valeur actuelle : {valeur} €"
    



class GestionnaireParc:
    def __init__(self):
        self.inventaire = [] 

    def ajouter_asset(self, asset):
        self.inventaire.append(asset)
        print(f"Asset '{asset}' ajouté à l'inventaire.")

    def afficher_rapport_financier(self):
        print("--- Bilan du Parc ---")
        total_investi = 0
        total_valeur_actuelle = 0

        if not self.inventaire:
            print("Le parc est vide.")
            return

        print(f"{'Nom':<25} | {'Investissement':<15} | {'Val. Actuelle':<15}")
        print("-" * 60)
        
        for asset in self.inventaire:
        # On récupère les infos de L'ASSET (pas de self)
            valeur_reelle = asset.calculer_valeur_actuelle()


            total_investi = total_investi + asset.prix_achat
            total_valeur_actuelle = total_valeur_actuelle + valeur_reelle    
            # Affichage formaté (le <25 sert à aligner le texte)
            print(f"{asset.nom:<25} | {asset.prix_achat:>10} €    | {valeur_reelle:>10} €")
        
        # SEPARATION
        print("-" * 30)

        print(f"Total Investi : {total_investi} €") 
        print(f"Valeur Restante : {total_valeur_actuelle} €")

    def supprimer_asset(self, nom_asset_a_supprimer):
        # On reconstruit la liste en gardant tout ce qui n'est PAS le nom à supprimer
        self.inventaire = [a for a in self.inventaire if a.nom != nom_asset_a_supprimer]
        
        # Et le petit print de confirmation
        print(f"🗑️ Asset supprimé : {nom_asset_a_supprimer}")
    

# --- ZONE DE TEST ---
if __name__ == "__main__":
    # 1. On instancie le gestionnaire
    mon_parc = GestionnaireParc()

    # 2. On crée des équipements
    pc1 = AssetIT("Dell XPS 15", 1500, "2023-06-01", 3)
    pc2 = AssetIT("MacBook Pro M2", 2500, "2024-01-10", 3)
    server = AssetIT("Serveur Dell PowerEdge", 4000, "2020-05-20", 5)
    ecran = AssetIT("Ecran Samsung 27", 200, "2021-02-15", 3)

    # 3. On les ajoute au gestionnaire
    mon_parc.ajouter_asset(pc1)
    mon_parc.ajouter_asset(pc2)
    mon_parc.ajouter_asset(server)
    mon_parc.ajouter_asset(ecran)

    # 4. On demande le rapport
    mon_parc.afficher_rapport_financier()

    # 5. Test de suppression (Mise au rebut de l'écran)
    mon_parc.supprimer_asset("Ecran Samsung 27")
    
    # On revérifie le total
    print("--- Après suppression ---")
    mon_parc.afficher_rapport_financier()
    

