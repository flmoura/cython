import os
#import fnmatch
import sysconfig

from setuptools import (
    setup,
    find_packages
)
from Cython.Build import cythonize
from setuptools.command.build_py import build_py as _build_py

EXCLUDE_FILES = [
    # 'app/main.py'
]

def get_ext_paths(root_dir, exclude_files):
    """get filepaths for compilation"""
    paths = []

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[1] != '.py':
                continue

            file_path = os.path.join(root, filename)
            if file_path in exclude_files:
                continue

            paths.append(file_path)
    print(paths)
    return paths

# noinspection PyPep8Naming
class build_py(_build_py):
    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            if os.path.exists(filepath.replace('.py', ext_suffix)):
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules

# noinspection PyPep8Naming
class build_py(_build_py):

    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            if os.path.exists(filepath.replace('.py', ext_suffix)):
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules


setup(
    name = "My Package App",
    version="0.1.0",
    packages = find_packages(),
    install_requires = [
        "numpy"
    ],

    ext_modules=cythonize(
        get_ext_paths('mypkg', EXCLUDE_FILES),
        compiler_directives={'language_level': 3}
    ),

    cmdclass={
        'build_py': build_py
    }
)
