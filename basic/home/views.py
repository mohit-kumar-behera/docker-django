from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt

import os, json


def ui_view(request):
    return render(request, 'index.html')


def create_directory(name):
    parent_dir = settings.BASE_DIR
    project_dir = os.path.join(parent_dir, name)
    try:
        os.makedir(project_dir)
        return project_dir
    except:
        print('Project with this name already exists')
        return False

def create_reponse_obj(status, message):
    return {
        'status': status,
        'message': message
    }


@csrf_exempt # for test purpose only
def create_docker_api_handler(request):
    if request.POST:
        # Fetch Data
        proj_name = request.POST.get('project-name').replace(' ', '-')
        docker_config = request.POST.get('about')
        
        # Create Project Directory
        project_dir = create_directory(proj_name)

        if project_dir:
            # Write Dockerfile
            docker_file_path = os.path.join(project_dir, 'Dockerfile')
            with open(docker_file_path, 'w') as file:
                file.write(docker_config)
            data = create_reponse_obj('success', 'Successfully create dockerfile')
            return HttpResponse(json.dumps(data), status=201)

        print('Error creating projectdir')
        data = create_reponse_obj('fail', 'Project with this name already exists')
        return HttpResponse(json.dumps(data), status=400)

    print('Only POST method allowed')
    data = create_reponse_obj('fail', 'Only POST method allowed')
    return HttpResponse(json.dumps(data), status=400)





"""
def scandockerfile():
    # Scan Dockerfile
    cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
    os.system(cmd)

    # Fetch the Json file
    json_file_path = os.path.join(project_dir, 'result.json')
    with open(json_file_path, 'r') as file:
        print(file.read())
"""