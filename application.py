import os
from flask import Flask, request, send_from_directory, Response

application = app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/mp3')
def mp3getter():
    filename = request.args.get('filename')
    return send_from_directory('public_files',filename, mimetype='audio/mpeg')

@app.route('/png')
def pnggetter():
    filename = request.args.get('filename')
    return send_from_directory('public_files',filename, mimetype='image/png')

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})


@app.route('/rss')
def feed_show():
    with open('/public_files/podcast.xml') as f1:
        text=f1.read()
    return Response(text, mimetype='text/xml')

if __name__ == '__main__':
 app.run()
