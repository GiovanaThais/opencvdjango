from turtle import up
from django.db import models
from uuid import uuid4
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import _tkinter

#funcao pra receber as imagens e gerar endereço
def upload_image_midias(instance, filename):
    return f"{instance.id_image}-{filename}"

#criando filtro para imagens
ACTION_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'gray scale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert')
)
class Midias(models.Model):
    #criando os atributos 
    id_image = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    information = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image_midias, blank=False, null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        #abrindo imagem 
        pil_img = Image.open(self.image)

        #convertendo imagem e processando
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        #convertendo imagem em array
        im_pil = Image.fromarray(img)

        #salvando imagem
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save( *args, **kwargs)


    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'
