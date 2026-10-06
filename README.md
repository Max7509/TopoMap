# TopoMap

Ce code python permet de créer une carte topographique d'une "tuile" de 1° par 1° aux coordonnées choisies par l'utilisateur. 
Les données topographiques sont issues de la base de données Copernicus DEM GLO-30. 
Le résultat est une image de 3600$\time$3600 pixels avec l'altitude de la zone en nuance de gris.

## Dépendences
Pour télécharger les dépendances, écrire dans le terminal : 
```bash
pip install rasterio numpy pillow
```

## Utilisation
```bash
python topoMap.py
```
Le code demande ensuite deux input : Latitude et Longitude (à 1° près)
On rentre donc les coordonnées dans la forme \texttt{N27} (N/S 0-90) puis \texttt{E086} (E/W 0-180)
Cet exemple de coordonnées donne l'Hymalaya autour dans la tuile où se situe l'Everest.
Les cartes sont enregistrées dans le dossier "resultats".

Les coordonnées possible sont seulement des degrés entier.
La carte couvre une surface d'un degré vers l'est et un degré vers le nord. 
La précision des données est d'un points tout les 30m.

## Exemple
Deux exemples sont disponible dans le dossier "resultats" : 
Les entrées \texttt{N27} puis \texttt{E086} donne la carte exemple_everest.png.
Les entrées \texttt{N48} puis \texttt{E002} donne la carte exemple_paris.png.
