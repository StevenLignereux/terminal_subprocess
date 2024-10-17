# CREER UN TERMINAL AVEC PYTHON
import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat
resultat = subprocess.run(
    "dir", shell=True, capture_output=True, universal_newlines=True
)  # ls sur mac

print(resultat.stdout)
print(resultat.stderr)
