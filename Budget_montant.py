#encoding:utf-8

__author__ ="Maduka David <mdsartb@gmail.com>"
__credits__ = "Acknowledgment to: Dr Cecille Mboyo"
__versions__ = "Budget version 1.0"
__date__ = "16.10.2022"


def budget(nom, montant):
	
	print(f"""
	Monsieur {nom} doit reserver pour:
		
	l'allimentation: {int(montant)*0.2}$ soit 20% de {montant} $
	la connexion: {int(montant)*0.1}$ soit 10% de {montant} $
	l'habillement: {int(montant)*0.1}$ soit 10% de {montant} $
	l'economie: {int(montant)*0.2}$ soit 20% de {montant} $
	le loyer: {int(montant)*0.3}$ soit 30% de {montant} $
	le loisir: {int(montant)*0.1}$ soit 10% de {montant} $
	
	""")
	

nom = input("entrez le nom S.V.P!!\n")

montant = input("entrez le montant S.V.P!!\n")

budget(nom, montant)