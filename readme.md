# Are You Allowed

L'idée de ce projet est de faire de la reconnaissance de visage en temps réel, à partir d'une caméra, afin de déterminer si une personne est autorisée à utiliser une machine ou si elle est autorisée à prendre connaissance de certaines informations pouvant être affichées sur un écran d'ordinateur par exemple.

Pour cela, le visage des personnes autorisées est enregistré en base de données.
La possibilité d'ajouter une personne qui serait autorisées peut-être fait à l'aide d'un mot de passe administrateur stocké en base de données étant crypté.

1. Le but est d'**envoyer une notification** sur téléphone si la caméra détecte **uniquement des visages inconnus** (des visages qui ne sont pas en base de données).
2. Si **une personne autorisées** est détectée mais que d'**autres personnes** autour d'elle **ne le sont pas**, alors il lui est demandé de **rentrer le mot de passe** administrateur. **En cas d'échec, une notification est envoyée**.
3. Si **uniquement des personnes autorisées** sont détectées, alors l'**environnement est sécurisé**.

## Bibliothèques

Ce projet a été développé en Python avec sa version en 3.9.1.

Vous trouverez ci-dessous la liste des bibliothèques utilisées :
- [Pycrypto](https://www.dlitz.net/software/pycrypto/)
- [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- [Yaml](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [OpenCV](https://github.com/opencv/opencv-python)

Pour les installer, vous pouvez vous aider des commandes suivantes :

```bash
# Pycrypto
pip install pycrypto

# MySQL Connector
pip install mysql-connector-python

# Yaml
pip install pyyaml

# OpenCV
pip install opencv-python
```
## Fichier de configuration

Un fichier de configuration `config.yaml` est nécessaire afin de configurer, par exemple, les identifiants de connexions à la base de données.
Voici un exemple de ce à quoi il devrait ressembler :

```yaml
- Database:
    host: host
    user: user
    password: password
    database: database
```
:warning: **Vous devez modifier ce fichier.**
> Veuillez modifier ces données selon votre environnement de travail.

## Execution du programme
Pour lancer le programme il suffit d’être à la racine du fichier `are_you_allowed.py` et de lancer la
commande suivante :
```bash
# Pycrypto
python are_you_allowed.py config/file/path/config.yaml
```

:warning: **Vous devez remplacer config/file/path/config.yaml par le chemin de où se trouve le fichier de configuration préalablement modifié.**