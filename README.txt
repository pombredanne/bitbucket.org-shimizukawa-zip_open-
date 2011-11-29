`zip_open` open file from nested zip file archive.

If you use static file like as 'data.zip' and open this from your
python code, Your program will become like
``open(os.path.join(os.path.dirname(__file__), 'data.zip'))``.
But if your packages are packed into packages.zip file (zipped-egg,
or cases to gather in one file on Google App Engine matter), your
code doesn't work fine.

In this situation, the file path of data.zip becomes
`/path/to/packages.zip/data.zip`, then your program can't open the
data.zip file.

`zip_open` package solves this problem.


Features
--------

* Open file from nested zip archive file path/name.
* Open file from nested zip archive file-like-object.


Using sample1: open the file from zip file
------------------------------------------

packages1.zip is::

   packages1.zip
     + file1.txt

Open file1.txt::

   >>> from zip_open import zopen
   >>> fobj = zopen('packages1.zip/file1.txt')
   >>> data = fobj.read()
   >>> print data
   I am file1.txt, ok.

You can specifiy zopen subpath args:

   >>> fobj = zopen('packages1.zip', 'file1.txt')
   >>> print fobj.read()
   I am file1.txt, ok.

These code samples equivalent to below code::

   >>> from zipfile import ZipFile
   >>> zipobj = ZipFile('packages1.zip')
   >>> data = zipobj.read('file1.txt')
   >>> print data
   I am file1.txt, ok.


Using sample2: open the file from nested zip file
-------------------------------------------------

packages2.zip is::

   packages2.zip
     + data2.zip
        + file2.txt

Open file2.txt::

   >>> from zip_open import zopen
   >>> fobj = zopen('packages2.zip/data2.zip/file2.txt')
   >>> print fobj.read()
   I am file2.txt, ok.


If you want to open from file-like-object, you can call::

   >>> zip_fileobj = open('packages2.zip')
   >>> fobj = zopen(zip_fileobj, 'data2.zip/file2.txt')
   >>> print fobj.read()
   I am file2.txt, ok.

then you also call::

   >>> from StringIO import StringIO
   >>> zip_payload = open('packages2.zip').read()
   >>> zip_fileobj = StringIO(zip_payload)
   >>> fobj = zopen(zip_fileobj, 'data2.zip/file2.txt')
   >>> print fobj.read()
   I am file2.txt, ok.


Using sample3: open the file included in package oneself
--------------------------------------------------------

packages3.zip is::

   packages3.zip
     + foo.py
     + file1.txt
     + data3.zip
        + file3.txt

foo.py::

   import os
   from zip_open import zopen

   def loader(filename):
       fobj = zopen(os.path.join(os.path.dirname(__file__), filename))
       return fobj


execute loader() from interactive shell::

   >>> import sys
   >>> sys.path.insert(0, 'packages3.zip')
   >>> import foo
   >>> fobj = foo.loader('file1.txt')
   >>> print fobj.read()
   I am file1.txt, ok.
   >>> fobj = foo.loader('data3.zip/file3.txt')
   >>> print fobj.read()
   I am file3.txt, ok.


Requirements and dependencies
------------------------------

* Requirement: Python 2.4 or later
* Dependency: Nothing.


ToDo
-----
* Add tar.gz file support.
* Add using sample document for egg archive.
* Add module import feature.


History
-------

0.2.0 (2011-11-29)
~~~~~~~~~~~~~~~~~~
* Change license from PSL to Apache License 2.0
* Add feature: open from file-like-object.


0.1.0 (2010-7-19)
~~~~~~~~~~~~~~~~~~
* first release

