from flask import Flask
from flask_restful import Api, reqparse, Resource
from werkzeug.datastructures import FileStorage

from cloudinary.uploader import upload, cloudinary
from cloudinary.utils import cloudinary_url

app = Flask(__name__)
api = Api(app)

#parser to flask-restful
parse = reqparse.RequestParser()
parse.add_argument('file', type=FileStorage, location='files')

#cloudinary config
cloudinary.config( 
  cloud_name = "", 
  api_key = "", 
  api_secret = "" 
)

#function define extensions image
def extensoes(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#classe uploadimage
class UploadImage(Resource):
  def post(self):
    args = parse.parse_args()
    file = args['file']
    if(extensoes(file.filename)):
        img = upload(file)
        return img
    else:
      return {'error': 'Formato de arquivo invalido'},415

api.add_resource(UploadImage, '/upload')

if __name__ == '__main__':
  app.run(debug=True)