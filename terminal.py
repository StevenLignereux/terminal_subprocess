# CREER UN TERMINAL AVEC PYTHON
import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat

while True:
    commande = input("Tapez quelque chose (ou 'exit' pour quitter) : ")

    if commande == "exit":
        print("Au revoir!")
        break

    resultat = subprocess.run(
        commande, shell=True, capture_output=True, universal_newlines=True
    )  # ls sur mac

    print(resultat.stdout)
    print(resultat.stderr)
