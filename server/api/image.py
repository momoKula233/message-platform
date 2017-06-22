import os
import random
import string

from flask import send_from_directory, request, Blueprint

image = Blueprint('image', __name__)

UPLOAD_FOLDER  = '/Users/momo/Documents/workspace/python-issues-platform/server/images'
EXTENSIONS = frozenset(['png', 'jpg', 'jpeg', 'PNG'])

def check_extension(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS

def get_filename():
  return ''.join(random.sample(string.ascii_lowercase + string.digits, 15))

@image.route('/upload', methods=['POST'])
def upload():
  pre_url = 'http://127.0.0.1:5000/images/'
  try:
    file = request.files['']
  except:
    file=request.files['file']
  if file and check_extension(file.filename):
    print(file, 'trick1')
    name = get_filename() + '.' + file.filename.rsplit('.', 1)[1]
    path = os.path.join(UPLOAD_FOLDER, name)
    if not os.path.exists(UPLOAD_FOLDER):
      os.mkdir(UPLOAD_FOLDER)
    file.save(path)
    return name
  return False

@image.route('/image/<string:id>')
def get_img(id):
  path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)), 'images')
  print (path, id)
  return send_from_directory(path, id, as_attachment=True)