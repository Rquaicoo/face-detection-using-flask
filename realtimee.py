from flask import Flask, render_template, Response
from camera import VideoCamera
import camera
import app
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('home.html')


def gen(camera):
    while True:
        frame = camera.capture_frames()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
from app import app
