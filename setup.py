# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', mode='r', encoding='utf-8') as _readme:
    readme = _readme.read()

with open('LICENSE', mode='r', encoding='utf-8') as _license:
    app_license = _license.read()

setup(
    name='dd-monitor',
    version='0.1.0',
    packages=find_packages(),
    author='Ayakura Yuki',
    author_email='AyakuraYuki@users.noreply.github.com',
    description='DD streams monitor, DD means 誰でも大好き',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/AyakuraYuki/dd_monitor',
    license=app_license,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask',
        'flask_cors',
        'flask_restful',
        'sqlalchemy',
        'fire',
    ],
)
