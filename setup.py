from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='snaildb',
    version='0.0.1',
    author='SREERAJ V RAJESH',
    author_email='cyberkutti@gmail.com',
    description='A simple non-SQL database like TinyDB or MongoDB using Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cyberkutti-iedc/snaildb',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
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
