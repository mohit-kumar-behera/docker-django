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
@csrf_exempt #only for testing purpose
def ui_view(request):
    if request.POST:
        # Fetch Data
        proj_name = request.POST.get('project-name').replace(' ', '-')
        docker_content = request.POST.get('about')
        
        # Create Project Directory
        parent_dir = BASE_DIR
        project_dir = os.path.join(parent_dir, proj_name)
        try:
            os.mkdir(project_dir)
        except:
            print("Already Exists")
        
        # Write Dockerfile
        docker_file_path = os.path.join(project_dir, 'Dockerfile')
        with open(docker_file_path, 'w') as file:
            file.write(docker_content)

        # getting absolute path
        # project_dir = os.path.abspath(project_dir)
        
        print(project_dir)

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

    else:
        return render(request, 'index.html')


# def create_update_scan_dockerfile(request):
