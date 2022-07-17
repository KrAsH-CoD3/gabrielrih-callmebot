import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='callmebot',
    version='1.0.0',
    author='Gabriel Richter',
    author_email='gabrielrih@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gabrielrih/callMeBot',
    license='MIT',
    packages=['callmebot'],
    install_requires=['requests', 'yaml'],
)