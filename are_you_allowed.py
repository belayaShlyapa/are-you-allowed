import utils
import sys
import databaseOperation
import cv2 as cv

from video import create_capture

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

# get pluged camera, otherwise, default image. 
cam = create_capture(0, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('src/image/image.jpg')))

while True:
  _, frame = cam.read()
  cv.imshow('sensor', frame)

  # break loop if 'ESC' button is pressed
  if cv.waitKey(5) == 27:
    break 

# close windows
cv.destroyAllWindows()

# close the connection
databaseOperation.closeConnection(dbConnection)