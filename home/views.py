import os

# Importing Django Dependencies
from django.shortcuts import render
from django.conf import settings
from django.views.decorators import csrf
from django.http import HttpResponse

# Importing other dependencies
import json

#  Importing constants from settings
from basic.settings import BASE_DIR

# Importing Utils
from home.utils import create_directory, create_reponse_obj


def home_view(request):
    context = {}
    if request.POST:
        # pth = settings.MEDIA_ROOT / 'Dockerfile' # path to docker file
        # with open(pth, 'r') as file:
        #     context['content'] = file.read()
        pth = settings.MEDIA_ROOT # path to docker file directory
        cmd = f'trivy config -f json -o {pth}/result.json {pth}'
        os.system(cmd)

        json_file_path = settings.MEDIA_ROOT / 'result.json'
        with open(json_file_path, 'r') as file:
            context['result_json'] = file.read()
        
    return render(request, 'home/home.html', context)



from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #only for testing purpose
# def ui_view(request):
#     if request.POST:
#         # Fetch Data
#         proj_name = request.POST.get('project-name').replace(' ', '-')
#         docker_content = request.POST.get('about')
        
#         # Create Project Directory
#         parent_dir = BASE_DIR
#         project_dir = os.path.join(parent_dir, proj_name)
#         try:
#             os.mkdir(project_dir)
#         except:
#             print("Already Exists")
        
#         # Write Dockerfile
#         docker_file_path = os.path.join(project_dir, 'Dockerfile')
#         with open(docker_file_path, 'w') as file:
#             file.write(docker_content)

#         # getting absolute path
#         # project_dir = os.path.abspath(project_dir)
        
#         print(project_dir)

#         # Scan Dockerfile
#         cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
#         print(os.system(cmd))

#         # Fetch the Json file
#         json_file_path = os.path.join(project_dir, 'result.json')
#         response_message = {}
#         with open(json_file_path, 'r') as file:
#             # print(file.read())
#             response_message = {
#                 "message": file.read()
#             }
#         # print(response_message)
#         return HttpResponse(json.dumps(response_message))

#     else:
#         return render(request, 'index.html')

def ui_view(request):
    return render(request, 'index.html')



@csrf_exempt # for test purpose only
def create_docker_api_handler(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # Fetch Data
    proj_name = body['project_name']
    # docker_config = request.POST.get('about')
    
    # Create Project Directory
    project_dir, flag = create_directory(proj_name)

    if flag:
        # Write Dockerfile
        docker_file_path = os.path.join(project_dir, 'Dockerfile')
        with open(docker_file_path, 'w') as file:
            file.write(docker_config)
        data = create_reponse_obj('success', 'Successfully create dockerfile')
        return HttpResponse(json.dumps(data), status=201)

    # print('Error creating projectdir')
    # data = create_reponse_obj('fail', 'Project with this name already exists')
    # return HttpResponse(json.dumps(data), status=400)
    docker_file_path = os.path.join(project_dir, 'Dockerfile');

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

    proj_name = request.POST.get('project-name').replace(' ', '-')
    docker_content = request.POST.get('about')
    
    # Create Project Directory
    parent_dir = BASE_DIR
    project_dir = os.path.join(parent_dir, proj_name)

    # Scan Dockerfile
    cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
    print(os.system(cmd))

    # Fetch the Json file
    json_file_path = os.path.join(project_dir, 'result.json')
    response_message = {}
    with open(json_file_path, 'r') as file:
        # print(file.read())
        response_message = {
            "message": file.read()
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

