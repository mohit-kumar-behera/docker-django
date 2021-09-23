import os

# Importing Django Dependencies
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt

# Importing other dependencies
import json, requests

# Importing Utils
from home.utils import create_directory, create_reponse_obj

def ui_view(request):
    return render(request, 'index.html')


@csrf_exempt # for test purpose only
def create_docker_api_handler(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # Fetch Data
    proj_name = body['project_name']
    
    # Create Project Directory
    project_dir, flag = create_directory(proj_name)

    if flag:
        data = create_reponse_obj('success', 'Successfully create dockerfile')
        return HttpResponse(json.dumps(data), status=201)

    docker_file_path = os.path.join(project_dir, 'Dockerfile')

    response_data = {} #contains the response json data, here Contents of the dockerfile
    try:
        with open(docker_file_path, 'r') as file:
            response_data = {
                "dockerfile" : file.read()
            }
        return HttpResponse(json.dumps(response_data), status=200)
    except:
        response_data = create_reponse_obj('fail', 'Project with this name already exists, no dockerfile found')
        return HttpResponse(json.dumps(response_data), status=400)


@csrf_exempt
def scan_docker_file(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    proj_name = body['project_name']
    docker_content = body['docker_content']
    
    # Create Project Directory
    parent_dir = settings.BASE_DIR
    project_dir = os.path.join(parent_dir, proj_name)
    docker_file_path = os.path.join(project_dir, 'Dockerfile')

    # Write to Dockerfile
    with open(docker_file_path, 'w') as file:
        file.write(docker_content)

    # Scan Dockerfile
    cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
    print(os.system(cmd))

    # Fetch the Json file
    json_file_path = os.path.join(project_dir, 'result.json')
    response_message = {}
    with open(json_file_path, 'r') as file:
        # print(file.read())
        response_message = {
            "trivy_response": file.read()
        }
    # print(response_message)
    return HttpResponse(json.dumps(response_message))



@csrf_exempt
def build_docker_file(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    project_name = body.get('project_name')

    parent_dir = settings.BASE_DIR
    project_dir = os.path.join(parent_dir, project_name)

    # Create tar for Dockerfile
    create_tar_cmd = f'tar -cvf ./{project_name}/Dockerfile.tar.gz -C {project_dir}/ Dockerfile'
    os.system(create_tar_cmd)

    # Path to Docker tar file
    docker_tar_file_path= os.path.join(project_dir, 'Dockerfile.tar.gz')

    try:
        with open(docker_tar_file_path) as f:
            data = f.read()
    except:
        status = 404
        response_obj = create_reponse_obj('fail', 'Something went wrong')
    else:
        status = 200
        ENDPOINT_URL = 'http://127.0.0.1:2375'
        headers = {
            'Content-Type': 'application/tar'
        }
        # Send POST Request to build image
        res = requests.post(url=f'{ENDPOINT_URL}/build?t={project_name}', data=data, headers=headers)

        # Send GET Request for info about image
        img_res = requests.get(url=f'{ENDPOINT_URL}/images/{project_name}/json')
        img_json = img_res.json()
        response_obj = create_reponse_obj('success', {'id': img_json.get('Id')})
    return HttpResponse(json.dumps(response_obj), status=status)
