from setuptools import setup, find_packages

setup(
    name='amplitude-python',
    keywords='python wrapper for amplitude.com HTTP API',
    version='0.1',
    packages=find_packages(),
    long_description=open('README.md').read(),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['requests','nose','requests-mock[fixture]','testtools','twine'],
    url='https://github.com/atveit/amplitude-python',
    author='Amund Tveit',
    author_email='atveit@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        ],
)
