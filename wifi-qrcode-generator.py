import pyqrcode

#Nom du wifi
ssid = ""
#Type de sécurité
security = ""
#Mot de passe du wifi
mdp = ""

qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{mdp};;')
qr.png('wificode.png', scale=6, module_color=[251, 123, 0, 128], background=[0xff, 0xff, 0xff])