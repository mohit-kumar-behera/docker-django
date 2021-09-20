
from django.conf import settings
import os

def create_directory(name):
    parent_dir = settings.BASE_DIR
    project_dir = os.path.join(parent_dir, name)
    print(project_dir)
    try:
        os.mkdir(project_dir)
        return project_dir, True
    except:
        print('Project with this name already exists')
        return project_dir, False

def create_reponse_obj(status, message):
    return {
        'status': status,
        'message': message
    }