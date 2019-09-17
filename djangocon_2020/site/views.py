from django.shortcuts import render
from os import walk

from config.settings.base import APPS_DIR


def default_view(request, menu='simple', submenu=None):
    path = APPS_DIR.__str__() + '/content/' + menu + ('/' + submenu if submenu else '')
    page = ''
    ctx = {}
    files = []

    for dirpath, dirname, filenames in walk(path):
        files.extend(filenames)
        break

    ctx['files'] = []
    for f in sorted(files):
        content = '%s/%s' % (path, f)
        ctx['files'].append(content)

    if menu == 'home' or menu == 'simple':
        page = menu
    else:
        page = 'default'

    return render(request, 'pages/' + page + '.html', ctx)