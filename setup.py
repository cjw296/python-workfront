from setuptools import setup, find_packages

setup(
    name='python-workfront',
    version='0.6.0',
    author='Chris Withers',
    author_email='chris@withers.org',
    license='MIT',
    description="Python library for accessing the Workfront REST api",
    long_description=open('docs/description.rst').read(),
    url='http://python-workfront.readthedocs.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    extras_require=dict(
        test=['nose', 'nose-cov', 'testfixtures', 'mock', 'coveralls'],
        build=['sphinx', 'pkginfo', 'setuptools-git']
    )
)
