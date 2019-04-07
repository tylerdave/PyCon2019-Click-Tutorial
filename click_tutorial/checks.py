import sys

def get_python_version():
    return sys.version.replace('\n', '')

def check_python_35_plus():
    if sys.version_info.major == 3 and sys.version_info.minor >=5:
        return True
    else:
        return False

def check_pytest():
    import pytest
    return True

ALL_CHECKS = {
    'Python Version': get_python_version,
    'Python 3.5+': check_python_35_plus,
    'PyTest Installed': check_pytest,
}