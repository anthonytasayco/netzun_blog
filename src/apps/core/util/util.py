# -*- coding: utf-8 -*-

from logging import getLogger
from os.path import normpath
import hashlib
import unicodedata, re

from django.views.generic import TemplateView

log = getLogger('django')


def cache_fragment(fragment_name='', *args):
    '''
        Obtiene la llave para un fragmento de cache de un template
    '''
    return 'template.cache.%s.%s' % (fragment_name, hashlib.md5(
        u':'.join([arg for arg in args])).hexdigest())


def choice_to_dict(choice):
    '''
        Convierte una tupla en formato del tipo choices a un diccionario en el
         que el primer elemento de cada par es la llave del diccionario.
    '''

    d = {}
    for c in choice:
        if c[0] not in d.keys():
            d[c[0]] = c[1]

    return d


def chunks(l, n):
    '''
        Retorna un subgrupos de la lista l de n elementos.
    '''

    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def fix_path(path):
    '''
        Normaliza una ruta y se asegura de que termine en un slash
    '''
    path = normpath(path)
    if path[:-1] != '/':
        path = path + '/'
    return path


def get_ip(request):
    '''
        Retorna la IP de un request, considerando la posibilidad de que el
         usuario puede estar detras de un proxy.
    '''

    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip


def model_to_choice(model, value='nombre', text=''):
    '''
        Convierte los datos de un modelo en una lista que puede ser usada
         como 'choices'.
    '''

    if not text:
        text = value

    total = model.objects.all().order_by(text)
    choice = []
    for el in total:
        choice.append((getattr(el, value), getattr(el, text)))

    return choice


class TextTemplateView(TemplateView):
    '''
        TemplateView que usa el mimetype: text/plain
    '''

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain;charset="utf-8"'

        return super(TemplateView, self).render_to_response(context,
            **response_kwargs)


def slugify(str):
    slug = unicodedata.normalize("NFKD", unicode(str)).encode("ascii", "ignore")
    slug = re.sub(r"[^\w]+", " ", slug)
    slug = "-".join(slug.lower().strip().split())
    return slug[0:175]


def get_uuslug_translation(Model, title, slug):
    nro = 1
    volver = True
    slug_base = slugify(title)
    slug_new = slug_base
    while volver:
        res = Model.objects.filter(slug=slug_new)
        if res.count() > 0:
            if slug == slug_new:
                return slug_new
        else:
            return slug_new
        slug_new = '%s-%s' % (slug_base, nro)
        nro = nro + 1
