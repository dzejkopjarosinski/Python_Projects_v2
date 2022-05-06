import cv2


#Our Image
img_file = "Images/Car_Image.jpg"
video = cv2.VideoCapture("Images/Tesla_Dashcam_trimed.mp4")

#Pre-trained car classifier
classifier_file = 'car_detector.xml'

#Create Car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)



#Turn video into grayscale, and detect car frame by frame
while True:
    #Read one frame from the video
    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #Detect cars - regaldless of the scale
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    
    
    #Display the image
    cv2.imshow('Car Detector', frame)
    cv2.waitKey(1)




"""
#Create OpenCV image
img = cv2.imread(img_file)


#Create Car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#Convert to grayscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Detect cars
cars = car_tracker.detectMultiScale(black_n_white)
for (x,y,w,h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


#Display the image
cv2.imshow('Car Detector', img)
cv2.waitKey()


print("Program colmpleted")
"""
