import os

# Importing Django Dependencies
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Importing other dependencies
import json

# Importing Utils
from home.utils import create_directory, create_reponse_obj


import docker

def ui_view(request):
    client = docker.from_env()
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


# def get_capabilities(request):
#     # GET request to recieve Capabilities list from server, from SQlite DB.
#     r

@csrf_exempt
def test_django_body(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    print(body)
    response_message = {
            "message": "success"
        }
    return HttpResponse(json.dumps(response_message))

