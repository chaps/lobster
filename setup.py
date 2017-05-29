from setuptools import setup, find_packages
setup(
    name="lobster",
    version="0.1.0",
    packages=["lobster"],
    package_data={'': ['LICENSE']},
    package_dir={'lobster': 'lobster'},
    scripts=['bin/lobster'],
    install_requires=['pafy>=0.5.2', 'pydub'],
    author="Josue Ortega",
    author_email="josueortega@protonmail.ch",
    description="Split audio files into tracks with a single command",
    long_description=open('README.md', 'rt').read(),
    license="MIT",
    keywords="audio track edit cut youtube ffmpeg mp3 ogg",
    url="https://github.com/noahfx/lobster",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio",
    ],
)
