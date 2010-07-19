import os
from zipimport import zipimporter
from zipfile import ZipFile
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

__all__ = ['zopen', 'zip_open']

def zopen(path):
    if os.path.exists(path):
        return open(path, 'rb')
    else:
        importer = zipimporter(path)
        zipobj = ZipFile(importer.archive)
        path = importer.prefix
        return zip_open(zipobj, path)


def path_finder(path):
    def finder(name):
        l = len(name)
        return bool(path.startswith(name) and path[l:l+1] in ('','/'))
    return finder


def zip_open(zipobj, subpath):
    assert isinstance(zipobj, ZipFile)

    subpath = subpath.replace(os.path.sep, '/').strip('/')
    prefixes = filter(path_finder(subpath), zipobj.namelist())

    if not prefixes:
        raise IOError(2, 'No such file or directory',
                      os.path.join(zipobj.filename, subpath))

    prefix = prefixes[0] # select first file
    fileobj = StringIO(zipobj.read(prefix))
    new_subpath = subpath[len(prefix):]

    if new_subpath:
        new_zipobj = ZipFile(fileobj)
        return zip_open(new_zipobj, new_subpath)
    else:
        return fileobj


