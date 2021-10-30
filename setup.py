import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pysherlock',                           # should match the package folder
    packages=['pysherlock'],                     # should match the package folder
    version='0.0.1',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Multipurpose Python Module',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Sachit Ramesh',
    author_email='quantechlxxi.corp@gmail.com',
    url='https://github.com/Sachit71/rudra', 
    project_urls = {                                # Optional
        "Headless Chrome": "https://github.com/Sachit71/pysherlock/issues"
    },
    install_requires=['requests','qrcode','wikipedia','beautifulsoup4'],                  # list all packages that your package uses
    keywords=["pypi", "headless chrome", "chrome", "rendertron"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Scraping',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/Sachit71/pysherlock/archive/refs/tags/hacktober.tar.gz",
