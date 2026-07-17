import pandas as pd

# Charger le fichier Excel
file_path = "votre_fichier_modifie2.xlsx"   # Remplace par le chemin de ton fichier

df = pd.read_excel(file_path)

# Remplacer "Tea" par "Thé" dans tout le DataFrame
df = df.replace("Salt", "Confiture")

# Sauvegarder le résultat
output_path = "votre_fichier_modifie3.xlsx"
df.to_excel(output_path, index=False)

print("Remplacement terminé avec succès !")