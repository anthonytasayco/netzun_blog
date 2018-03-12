from django.db import models
from apps.core.models import AuditableModel, SlugModel

# Create your models here.


class Publication(AuditableModel, SlugModel):
    description = models.TextField('Description', blank=True)
    image = models.ImageField(upload_to='pulication')
    featured = models.BooleanField('Destacado', default=False)

    class Meta:
        verbose_name = u'Publicacion'
        verbose_name_plural = u'Publicaciones'

    def __str__(self):
        return self.name
