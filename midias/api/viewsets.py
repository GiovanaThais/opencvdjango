from rest_framework import viewsets
from midias.api import serializers
from rest_framework import generics
from midias import models

'''class MidiasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MidiasSerializer
    queryset = models.Midias.objects.all() #chamando todos os itens do model
'''

class ListarMidiasAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.MidiasSerializer
    queryset = models.Midias.objects.all()

class MidiaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Midias.objects.all()
    serializer_class = serializers.MidiasSerializer