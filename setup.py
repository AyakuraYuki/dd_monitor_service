import setuptools

with open('README.md', mode='r', encoding='utf-8') as readme:
    description = readme.read()

setuptools.setup(
    name='dd-monitor',
    version='0.1.0',
    author='AyakuraYuki',
    author_email='AyakuraYuki@users.noreply.github.com',
    description='DD streams monitor, DD means 誰でも大好き',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/AyakuraYuki/dd_monitor',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
        'flask',
        'python-dotenv',
    ],
)
