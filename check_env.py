import os
import sys

requirements = [
    ('numpy', '1.8.1'),
    ('pandas', '0.14.0'),
    ('sklearn', '0.14'),
    ('scipy', '0.14.0'),
    ('matplotlib', '1.3.1'),
    ('IPython', '2.1.0'),
]

if sys.version_info[:2] != (2, 7):
    print("\nWarning: Tutorial tested with python2.7")

def try_import(package_name, suggested_version):
    try:
        module = __import__(package_name)
    except ImportError:
        print("\nError: couldn't import %s" % package_name)
    else:
        if module.__version__ != suggested_version:
            print("\nWarning: Tutorial tested with %s=%s" %(package_name, suggested_version))
            print("You have %s=%s" %(package_name, module.__version__))


[try_import(package_name, suggested_version) for package_name, suggested_version in requirements]

try:
    import IPython.html.notebookapp
except ImportError:
    print("ERROR: You can't seem to start up an IPython notebook")
