import utils
import sys
import databaseOperation

# Read yaml config file
yamldata = utils.readYamlConfigFile(sys.argv[1])

# Get data from 'Database' list of yaml config file
databaseYamlData = yamldata[0]['Database']
dbConnection = databaseOperation.openConnection(databaseYamlData)

print('Mot de passe:')
inputPassword = input()

encodedInputPassword = utils.encodeToSha256(inputPassword)

if utils.isAdmin(encodedInputPassword, dbConnection):
  print('Oui')
else:
  print('Non')

# close the connection
databaseOperation.closeConnection(dbConnection)