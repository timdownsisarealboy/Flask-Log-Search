from setuptools import setup
import os
import distutils.sysconfig
pre = distutils.sysconfig.get_config_var("prefix")
bindir = os.path.join(pre, "bin/activate")

setup(
    name='log_search',
    version='0.0.1',
    description='Log Search Beta',
    author='Tim Downs',
    author_email='tim@sociagram.com',
    zip_safe=False,
    include_package_data=True,
    url='http://framestack.com',
    platforms=["any"],
    dependency_links=[],
    install_requires=[
        'flask',
    ]
)
