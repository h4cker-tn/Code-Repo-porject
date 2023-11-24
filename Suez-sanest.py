class Entreprise:
    def __init__(self, nom):
        self.nom = nom
        self.factures = []

    def generer_facture(self, projet, cout):
        self.factures.append((projet, cout))
        return f"Facture de {self.nom} pour le projet '{projet}': {cout}$"


class Projet:
    def __init__(self, nom, cout_initial):
        self.nom = nom
        self.cout_initial = cout_initial
        self.cout_actuel = cout_initial
        self.taches = []

    def ajouter_tache(self, nom_tache, cout_tache):
        self.taches.append((nom_tache, cout_tache))
        self.cout_actuel += cout_tache

    def generer_facture(self):
        facture = f"Facture pour le projet '{self.nom}':\n"
        facture += f"Coût initial du projet : {self.cout_initial}$\n"
        facture += f"Coût actuel du projet : {self.cout_actuel}$\n"
        facture += "Tâches réalisées :\n"
        for nom_tache, cout_tache in self.taches:
            facture += f"- {nom_tache} : {cout_tache}$\n"
        return facture


# Création des entreprises
suez = Entreprise("SUEZ")
sanest = Entreprise("SANEST")
conseko_safege = Entreprise("CONSEKO SAFEGE")

# Création des projets pour chaque entreprise
projet_suez = Projet("Projet SUEZ", 5000)
projet_suez.ajouter_tache("Analyse des besoins", 1500)
projet_suez.ajouter_tache("Développement", 2500)

projet_sanest = Projet("Projet SANEST", 4000)
projet_sanest.ajouter_tache("Tests initiaux", 1000)
projet_sanest.ajouter_tache("Implémentation", 2000)

projet_conseko = Projet("Projet CONSEKO SAFEGE", 7000)
projet_conseko.ajouter_tache("Conception", 3000)
projet_conseko.ajouter_tache("Tests finaux", 2000)

# Génération des factures pour chaque entreprise
facture_suez = suez.generer_facture(projet_suez.nom, projet_suez.cout_actuel)
facture_sanest = sanest.generer_facture(projet_sanest.nom, projet_sanest.cout_actuel)
facture_conseko = conseko_safege.generer_facture(projet_conseko.nom, projet_conseko.cout_actuel)

# Affichage des factures générées pour chaque entreprise
print("Facture pour SUEZ :")
print(facture_suez)
print("Facture pour SANEST :")
print(facture_sanest)
print("Facture pour CONSEKO SAFEGE :")
print(facture_conseko)
