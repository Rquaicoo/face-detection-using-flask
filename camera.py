import cv2
import dlib


# Detect the coordinates
detector = dlib.get_frontal_face_detector()


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def capture_frames(self):
        while True:
            ret, frame = self.video.read()
            frame = cv2.flip(frame, 1)

            # RGB to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            # Iterator to count faces
            i = 0
            for face in faces:

                # Get the coordinates of faces
                x, y = face.left(), face.top()
                x1, y1 = face.right(), face.bottom()
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

                # Increment iterator for each face in faces
                i = i+1

                # Display the box and faces
                cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                print(face, i)
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
