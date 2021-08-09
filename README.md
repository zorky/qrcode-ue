# qrcode-ue

* Créer un fichier `qr-code.txt` dans lequel est mis le code du qrcode (scanner avec un lecteur QRCode)), indication : le code commence par HC1:

via docker :

* Construire l'image : `docker build -t qrcode .`
* Exécuter : `docker-compose run --rm qrcode`

en local, sans docker, python3 doit être installé :

* `pip install -r requirements.txt`
* `python decode.py`

Le code python a été trouvé sur https://alphalist.com/blog/the-use-of-blockchain-for-verification-eu-vaccines-passport-program-and-more 
