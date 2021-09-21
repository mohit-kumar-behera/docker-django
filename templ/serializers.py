from rest_framework import serializers
from templ.models import Capabilities, Templates

class CapabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capabilities
        fields = '__all__'


class TemplatesSerializer(serializers.ModelSerializer):
    capabilities = CapabilitiesSerializer(many=True)

    class Meta:
        model = Templates
        fields = '__all__'