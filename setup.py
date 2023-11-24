from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='snailDB',
    version='0.0.2',
    author='SREERAJ V RAJESH',
    author_email='cyberkutti@gmail.com',
    description='SnailDB is a lightweight, non-SQL database for Python, designed for simplicity and ease of use',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cyberkutti-iedc/snailDB',
    packages=find_packages(),
    keywords=["non-sql","database","python-database","lightwight database","non-sql database"],
    install_requires=[
        'fastjsonschema',
        'ujson',
        'orjson',
        'jsonschema',
        'fastjsonschema',
        'pathspec',
        'repath',
        'typing_extensions',
        'Flask',
        'Flask-SocketIO'
    ],
    entry_points={
        'console_scripts': [
            'snaildb = snaildb.snaildb:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
