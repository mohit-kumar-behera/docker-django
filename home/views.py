import os

# Importing Django Dependencies
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Importing other dependencies
import json, requests

# Importing Utils
from home.utils import create_reponse_obj, docker_handler, scan_handler

DOCKER_FILE = 'Dockerfile'
DOCKER_YML_FILE = 'DockerCmps.yml'
ENDPOINT_URL = 'http://127.0.0.1:2375'

def ui_view(request):
    return render(request, 'index.html')


@csrf_exempt
def create_docker_api_handler(request):
    response_obj, status = docker_handler(request, DOCKER_FILE)
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def compose_docker_api_handler(request):
    response_obj, status = docker_handler(request, DOCKER_YML_FILE)
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def scan_docker_file(request):
    response_obj, status = scan_handler(request, DOCKER_FILE)
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def scan_composed_docker_file(request):
    response_obj, status = scan_handler(request, DOCKER_YML_FILE)
    return HttpResponse(json.dumps(response_obj), status=status)


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
        response_obj, status = create_reponse_obj('fail', 'Something went wrong'), 404
    else:
        headers = {
            'Content-Type': 'application/tar'
        }
        # Send POST Request to build image
        res = requests.post(url=f'{ENDPOINT_URL}/build?t={project_name}', data=data, headers=headers)

        # Send GET Request for info about image
        img_res = requests.get(url=f'{ENDPOINT_URL}/images/{project_name}/json')
        img_json = img_res.json()
        response_obj, status = create_reponse_obj('success', {'id': img_json.get('Id')}), 200
        
    return HttpResponse(json.dumps(response_obj), status=status)

@csrf_exempt
def image_list(request):
    res = requests.get(url=f'{ENDPOINT_URL}/images/json')
    res_json = res.json()
    response_obj, status = create_reponse_obj('success', res_json), 200
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def delete_image(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    image_id = body.get('image_id')
    if image_id:
        delete_cmd = f'docker rmi {image_id}'
        try:
            os.system(delete_cmd)
        except:
            response_obj, status = create_reponse_obj('failure', 'Sorry ID is wrong'), 400
            return HttpResponse(json.dumps(response_obj), status=status)
        else:
            response_obj, status = create_reponse_obj('success', f'Image with ID {image_id} deleted'), 200
            print(image_id)
            return HttpResponse(json.dumps(response_obj), status=status)
    response_obj, status = create_reponse_obj('failure', 'Sorry ID is wrong'), 400
    print(image_id)
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def push_image_to_repo(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    image_id = body.get('image_id')
    repo_name = body.get('repo_name')
    tag_cmd = f'docker tag {image_id} {repo_name}'
    os.system(tag_cmd)
    push_cmd = f'docker push {repo_name}'
    os.system(push_cmd)
    response_obj, status = create_reponse_obj('success', f'Image with ID {image_id} pushed to Repo {repo_name}'), 200
    return HttpResponse(json.dumps(response_obj), status=status)    





    #image delete
    #img = 'Selected image'
    #cmd1 = 'docker rmi {}'.format(img)
    #os.system(cmd1)
    
    #Preparing for image push
    #repo = 'Take input from user'
    #cmd2 = 'docker tag {} {}'.format(img,repo)
    #os.system(cmd2)
    #cmd3 = 'docker push {}'.format(repo)
    #os.system(cmd3)