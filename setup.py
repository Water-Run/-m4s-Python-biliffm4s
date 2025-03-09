from setuptools import setup, find_packages
import platform
import os

# 检查系统架构是否为 64 位
if platform.architecture()[0] != '64bit':
    raise RuntimeError("biliffm4s 仅支持 64 位系统。")

# 检查系统是否支持
supported_systems = ['Windows']
current_system = platform.system()
if current_system not in supported_systems:
    raise RuntimeError("biliffm4s 仅支持 Windows系统。")

# 动态生成 ffmpeg 文件的路径
def get_ffmpeg_files():
    ffmpeg_dir = os.path.join('biliffm4s', 'ffmpeg')
    file_list = []
    for root, _, files in os.walk(ffmpeg_dir):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), 'biliffm4s'))
    return file_list

setup(
    name='biliffm4s',
    version='1.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'biliffm4s': get_ffmpeg_files(),  # 动态添加 ffmpeg 文件
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
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
    python_requires='>=3.6',
)