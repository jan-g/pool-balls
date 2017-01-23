import os.path
from setuptools import setup, find_packages

def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()

setup(
    name="pool",
    version="0.0.1",
    description="Look for balls",
    long_description=read_file("README.md"),
    author="jan grant",
    author_email="jang@ioctl.org",
    license=read_file("LICENCE.md"),

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'balls = pool.cmd:main',
        ],
    },

    install_requires=[
                      "opencv-python",
                      "pyyaml",
                      "termcolor",
                     ],
)
