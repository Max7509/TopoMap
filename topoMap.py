import numpy as np
import rasterio
import rasterio.enums
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image

BASE = "https://copernicus-dem-30m.s3.amazonaws.com/{t}/{t}.tif"

def telecharger(nom, dossier="."):
    dest = Path(dossier) / f"{nom}.tif"
    if dest.exists():
        return dest
    try:
        urllib.request.urlretrieve(BASE.format(t=nom), dest)
    except urllib.error.HTTPError as e:
        dest.unlink(missing_ok=True)
        raise SystemExit(f"Tuile {nom} inaccessible (HTTP {e.code}) : "
                         "nom erroné, océan, ou tuile non publique")
    return dest

while True:
    Lat = input('Latitude (Exemple: N27°59\' --> N27): ')
    if (len(Lat) == 3 and Lat[0] in ('N', 'S') and Lat[1:].isdigit()):
        if int(Lat[1:3]) > 90:
            print(f"La latitude '{Lat}' est hors limites (S90-N90)")
        else:
            break
    else:
        print(f"La latitude '{Lat}' doit commencer par 'N' ou 'S' et être suivie de deux chiffres")
while True:
    Lon = input('Longitude (Exemple: E086°55\' --> E086): ')
    if (len(Lon) == 4 and Lon[0] in ('E', 'W') and Lon[1:].isdigit()):
        if int(Lon[1:4]) > 180:
            print(f"La longitude '{Lon}' est hors limites (E000-E180 ou W000-W180)")
        else:
            break
    else:
        print(f"La longitude '{Lon}' doit commencer par 'E' ou 'W' et être suivie de trois chiffres")
while True:
    N = input('Resolution NxN (1-3600): ')
    if N.isdigit() and 1 <= int(N) <= 3600:
        N = int(N)
        break
    else:
        print(f"La résolution '{N}' doit être un nombre entre 1 et 3600")

mapName = telecharger(f"Copernicus_DSM_COG_10_{Lat}_00_{Lon}_00_DEM", dossier="tif_data")
with rasterio.open(mapName) as src:
    print(src.bounds)
    z = src.read(1, out_shape=(N, N), resampling=rasterio.enums.Resampling.average)
    print(z.min(), z.max())
    print(z.shape)

zmin, zmax = np.nanmin(z), np.nanmax(z)
t = (z - zmin) / max(zmax - zmin, 1e-9)
t = np.nan_to_num(t)

img8 = (t * 255).round().astype(np.uint8)  
img = Image.fromarray(img8)

img.save(Path("resultats") / f"{Lat}_{Lon}_N{N}.png")
print(f"Image enregistrée")
img.show()