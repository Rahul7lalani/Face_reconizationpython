# Face_reconizationpython

# This Project was one of the statement of Microsoft Engage 2022 

### Face Recognition "Tracking the Attendence of students"

A window with eight buttons will open after running the main.py, attendence.py, classifier.xml, developer.py, face recognition.py, Haar cascade frontal face default.xml, student.py, and train.py along with the folder Images and Image data in the same folder. The first button, 1.) Student details, takes us to a new window where we can manually save a student's data along with his Note: The Student ID is keeping a record of your photo sample (about 100 photos is captured for the data training) A face classifier is used to recognize faces in this case. By cascading the "Haar cascade frontal face default classifier," a cropped black-and-white picture of the faces is also displayed.

2.) Train Face: When this button is clicked, a window with another button that is used to train the face picture sample that was taken in the previous window is redirected. The LBPH algorithm, which employs four parameters including Radius (a circular binary pattern is generated around the central pixel), Neighbors, or the number of sample points, is used to save the trained data of the Faces in the file "classifier.xml." Grid x and Grid y, which represent the number of cells in the horizontal and vertical directions, are the following two parameters. The programme will detect an input image using a student ID and then provide you an output after handling LBP operations and extracting the Histograms.More details can be found here:"https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b"

3.) Face Detector This button also has a button that, when clicked, recognises a face by mentioning his or her details in the green. If the person is not recognized or trained to the model, a red box with an unknown tag is mentioned. As soon as a person is recognized, the date and time of the person's attendance are saved along with the person's attendance. csv file

4.) Attendance: Using this button, we can import a csv file to show the data for the attendees, which we can then change in the designated spaces and export to another csv file.


5.) Developer My information is provided here:

6.) Photos This button was intended to go to the Image data folder where the sample data is being captured, however it is not yet operational.

7.) Contact information for the developer may be found here.

8.) Exit - Clicking this will close all windows. so you leave and go to the project

Note:- If you don't input the password and other host information for your MySQL server, an error will be generated, therefore adjust the path of the photos.

###### The requirements.txt section provides the prerequisites of the modules to be imported for this project, and the language used is Python with mySQL queries for database access.The requirements.txt section provides the prerequisites of the modules to be imported for this project, and the language used is Python with mySQL queries for database access.

