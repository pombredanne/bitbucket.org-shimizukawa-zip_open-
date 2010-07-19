`zip_open` open file from nested zip file archive.

If you use static file like as 'data.zip' and open this from your
python code, Your program will become like
``open(os.path.join(os.path.dirname(__file__), 'data.zip'))``.
But if your packages are packed into packages.zip file (zipped-egg,
or cases to gather in one file on Google App Engine matter), your
cord doesn't work fine.

In this situation, the file path of data.zip becomes
`/path/to/packages.zip/data.zip`, then your program can't open the
data.zip file.

`zip_open` package solves this problem.


Features
--------

* Open file from nested zip file archive.


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

This code sample equivalent to below code::

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
* Write tests.


History
-------

0.1.0 (2010-7-19)
~~~~~~~~~~~~~~~~~~
* first release

