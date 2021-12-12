import face_recognition
import numpy as np
import os, re
from termcolor import colored

def identify_citizen(imagename):
    print(colored("Recognition  initiated","red"))
    known_face_encodings = []
    known_face_names = []
    known_faces_filenames = []
    
    #adds filenames to list
    print(colored("Loading images of known faces ...", "yellow"))
    for (dirpath, dirnames, filenames) in os.walk('assets/img/users/'):
        known_faces_filenames.extend(filenames)
        break

        print(colored('Loading complete',"green"))
    #loads face encoding
        print(".................")
        print(colored('Loading face encodings ...',"red"))
    for filename in known_faces_filenames:
        face = face_recognition.load_image_file('assets/img/users/' + filename)
        known_face_names.append(re.sub("[0-9]",'', filename[:-4]))
        known_face_encodings.append(face_recognition.face_encodings(face)[0])
        
    print(colored('Face encodings loaded',"green"))
    face_locations = []
    face_encodings = []
    face_names = []
    imagename_new =  face_recognition.load_image_file(imagename)
    face_locations = face_recognition.face_locations(imagename_new)
    face_encodings = face_recognition.face_encodings(imagename_new, face_locations)

    print(colored('Loading unkown image ...',"red"))

    print(colored('Commencing matching phase ...',"red"))
    #initiates face matching process
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        print(colored('Checking best match index ....',"yellow"))
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            

        face_names.append(name)
    print('Matching process complete ... ')
    return name
