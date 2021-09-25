
from django.conf import settings
import os, json

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

def project_creator(proj_name, file):
    # Create Project Directory
    project_dir, flag = create_directory(proj_name)

    # If project with same name already exists
    if flag:
        response_obj = create_reponse_obj('success', 'Successfully create dockerfile')
        return response_obj, 201

    docker_file_path = os.path.join(project_dir, file)

    try:
        with open(docker_file_path, 'r') as file:
            response_obj = {
                "dockerfile" : file.read()
            }
        return response_obj, 200
    except:
        response_obj = create_reponse_obj('fail', 'Project with this name already exists, no dockerfile found')
        return response_obj, 400

def docker_handler(req, file):
    response_obj, status = create_reponse_obj('fail', 'Something went wrong'), 404
    if req.method == 'POST':
        body_unicode = req.body.decode('utf-8')
        body = json.loads(body_unicode)
        proj_name = body.get('project_name')
        response_obj, status = project_creator(proj_name, file)
    return response_obj, status



def project_scanner(proj_name, file, docker_content):
    # Create Project Directory
    parent_dir = settings.BASE_DIR
    project_dir = os.path.join(parent_dir, proj_name)
    docker_file_path = os.path.join(project_dir, file)
    # Write to Dockerfile
    with open(docker_file_path, 'w') as file:
        file.write(docker_content)

    # Scan Dockerfile
    trivy_cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
    os.system(trivy_cmd)

    # Fetch the Json file
    json_file_path = os.path.join(project_dir, 'result.json')
    with open(json_file_path, 'r') as file:
        response_obj = {
            "trivy_response": file.read()
        }
    return response_obj, 200
    print(response_obj)


def scan_handler(req, file):
    response_obj, status = create_reponse_obj('fail', 'Something went wrong'), 404
    if req.method == 'POST':
        body_unicode = req.body.decode('utf-8')
        body = json.loads(body_unicode)

        proj_name = body['project_name']
        docker_content = body['docker_content']
        
        response_obj, status = project_scanner(proj_name, file, docker_content)
    return response_obj, status