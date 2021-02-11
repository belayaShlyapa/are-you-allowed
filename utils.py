import hashlib
import databaseOperation
import yaml

def encodeToSha256(input):
    hash_object = hashlib.sha256(bytes(input, encoding='utf-8'))
    return hash_object.hexdigest()

def isAdmin(password, dbConnection):
    recognizedPasswords = databaseOperation.isPasswordAdmin(password, dbConnection)

    if len(recognizedPasswords) >= 1:
        return True
    else:
        return False

def readYamlConfigFile(configFilePath):
    with open(configFilePath, "r") as yamlfile:
        yamldata = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return yamldata