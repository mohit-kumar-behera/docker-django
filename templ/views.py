from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.utils import create_reponse_obj

from templ.models import Capabilities, Templates
from templ.serializers import CapabilitiesSerializer, TemplatesSerializer

import json

@api_view(['GET'])
def get_capabilities_api_handler(request):
    if request.method == 'GET':
        capabilities = Capabilities.objects.all()
        serializer = CapabilitiesSerializer(capabilities, many=True)
        response = create_reponse_obj('success', serializer.data)
        return Response(response, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def templates_api_handler(request):
    if request.method == 'GET':
        # Fetch Templates
        templates = Templates.objects.all()
        serializer = TemplatesSerializer(templates, many=True)
        response = create_reponse_obj('success', serializer.data)
        return Response(response, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # Create Templates
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        template_name = body.get('temp')
        try:
            Templates.objects.get(Name_of_template=template_name)
        except Templates.DoesNotExist:
            template = Templates.objects.create(Name_of_template=template_name)
            template.save()
            capabilities = body.get('caps')

            for cap in capabilities:
                try:
                    cp = Capabilities.objects.get(CAP_Id=cap.get('CAP_Id'))
                except Capabilities.DoesNotExist:
                    pass
                else:
                    template.capabilities.add(cp) 

            serializer = TemplatesSerializer(template, many=False)
            response = create_reponse_obj('success', serializer.data)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = create_reponse_obj('fail', 'Template with name already exists')
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
