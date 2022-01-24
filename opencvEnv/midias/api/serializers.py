from rest_framework import serializers
from midias import models

class MidiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Midias
        fields = '__all__' #serializando todos os campos do model