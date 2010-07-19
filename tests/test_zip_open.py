import sys, os, doctest, unittest


def setUp(args):
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, '..', 'src'))
    os.chdir(here)


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            '../README.txt',
            setUp=setUp,
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
    ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

