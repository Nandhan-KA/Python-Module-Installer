from setuptools import setup, find_packages

setup(
    name="pymodins",
    version="2.1.1",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "pymodins=pymodins.installer:run",
        ],
    },
    author="Nandhan K",
    author_email="nandhan2003alamelu@gmail.com",
    description="A module to install various Python packages.",
    maintainer="Nandhan K",
    maintainer_email="nandhan2003alamelu@gmail.com",
    keywords=[
        "Python Module Installer", 
        "Python Package Installer", 
        "python modules installer", 
        "python package installer", 
        "Nandhan-KA", 
        "PYMODINS", 
        "pymodins"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Nandhan-KA/pymodins",
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Win32 (MS Windows)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    platforms=["win32"],  
)
