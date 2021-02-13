import utils
import sys
import databaseOperation
import cv2 as cv
import os
import re
import face_recognition
import numpy as np

from video import create_capture
from common import draw_str

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

known_face_encodings = []
known_face_names = []
known_face_filenames = []

# Arborescence des fichiers
for (dirpath, dirnames, filenames) in os.walk('src/'):
  known_face_filenames.extend(filenames)
  break

# Création des données des visages qui existent déjà
for filename in known_face_filenames:
  face = face_recognition.load_image_file('src/' + filename)
  known_face_names.append(re.sub("[0-9]", '', filename[:-4]))
  known_face_encodings.append(face_recognition.face_encodings(face)[0])

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# get pluged camera, otherwise, default image. 
cam = create_capture(0, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('src/image/image.jpg')))

while True:
  _, frame = cam.read()

  if process_this_frame:
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []

  for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Inconnu"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
      name = known_face_names[best_match_index]

    face_names.append(name)

  process_this_frame = not process_this_frame

  for (top, right, bottom, left), name in zip(face_locations, face_names):
    # construction du rectangle autour du visage
    cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # on attribut le nom du rectangle
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(frame, name, (left + 6, bottom -6), font, 1.0, (255, 255, 255), 1)

  cv.imshow('sensor', frame)

  # break loop if 'ESC' button is pressed
  if cv.waitKey(5) == 27:
    break 

# close windows
cv.destroyAllWindows()

# close the connection
databaseOperation.closeConnection(dbConnection)