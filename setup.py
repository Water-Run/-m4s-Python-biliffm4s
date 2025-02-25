from setuptools import setup, find_packages

setup(
    name='biliffm4s',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'biliffm4s': ['ffmpeg/*']
    },
    install_requires=[],
    author='WaterRun',
    author_email='2263633954@qq.com',
    description='biliffm4s: A tool to merge Bilibili cached .m4s files into .mp4',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Water-Run/-m4s-Python-biliffm4s',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)