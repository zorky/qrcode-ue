# qrcode-ue

* Construire l'image : `docker build -t qrcode .`
* Créer un fichier `qr-code.txt` dans lequel est mis le code du qrcode (scanner avec un lecteur QRCode), indication : le code commence par HC1:
* Exécuter : `docker-compose run --rm qrcode`
