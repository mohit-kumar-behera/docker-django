from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.utils import create_reponse_obj

from templ.models import Capabilities, Templates
from templ.serializers import CapabilitiesSerializer, TemplatesSerializer


@api_view(['GET'])
def get_capabilities_api_handler(request):
    if request.method == 'GET':
        capabilities = Capabilities.objects.all()
        serializer = CapabilitiesSerializer(capabilities, many=True)
        response = create_reponse_obj('success', serializer.data)
        return Response(response, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_templates_api_handler(request):
    if request.method == 'GET':
        templates = Templates.objects.all()
        serializer = TemplatesSerializer(templates, many=True)
        response = create_reponse_obj('success', serializer.data)
        return Response(response, status=status.HTTP_200_OK)

    if request.method == 'POST':
        pass