import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="flamapy-fm-dist",
    version="1.6.0.dev0",
    author="Flamapy",
    author_email="flamapy@us.es",
    description="Flamapy feature model is a distribution of the flama framework containing all plugins required to analyze feature models. It also offers a richier API and a complete command line interface and documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flamapy/flamapy-feature-model",
    packages=setuptools.find_namespace_packages(include=['flamapy.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        "wheel",
        "Flask",
        "gunicorn",
        "flamapy~=1.6.0.dev0",
        "flamapy-fm~=1.6.0.dev0",
        "flamapy-sat~=1.6.0.dev0",
        "flask-swagger-ui",
        "flask-restplus",
        "pytest",
        "flask_cors",
        "flasgger",
        "Fire"
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock',
            'prospector',
            'mypy',
            'coverage',
        ]
    },
    entry_points={
        'console_scripts': [
            'flamapy-fm-cli = flamapy.interfaces.command_line:flama_fm',
        ],
    },
)
