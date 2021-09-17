from django.shortcuts import render
from django.conf import settings
import os
from django.views.decorators import csrf

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
        parent_dir = "/home/mohit/PROJ"
        project_dir = os.path.join(parent_dir, proj_name)
        os.mkdir(project_dir)

        # Write Dockerfile
        with open(os.path.join(project_dir, 'Dockerfile'), 'w') as file:
            file.write(docker_content)

        # Scan Dockerfile
        cmd = f'trivy config -f json -o {project_dir}/result.json {project_dir}'
        os.system(cmd)

        # Fetch the Json file
        json_file_path = os.path.join(project_dir, 'result.json')
        with open(json_file_path, 'r') as file:
            print(file.read())

    return render(request, 'index.html')