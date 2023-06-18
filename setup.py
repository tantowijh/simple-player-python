from setuptools import setup

# Read the contents of README.md file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='simpleplayer',
    version='1.0.1',
    description='Module for playing audio files using soundfile and sounddevice.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='TOWDIO',
    author_email='thowiestudio@gmail.com',
    packages=['simpleplayer'],
    install_requires=[
        'soundfile',
        'sounddevice',
        'numpy',
    ],
)
