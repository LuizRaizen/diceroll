from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='diceroll',
    version='0.0.2',
    url='https://github.com/LuizRaizen/diceroll.git',
    license='MIT License',
    author='Luiz R. Dererita',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='luizdererita02@gmail.com',
    keywords='dice roll diceroll',
    description=u'This is dice roll simulator for games.',
    py_modules=['diceroll'],)