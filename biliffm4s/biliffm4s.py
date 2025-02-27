r"""
:author: WaterRun
:date: 2025-02-27
:description: biliffm4s的源码
:file: biliffm4s.py
:version: 1.1
"""

import subprocess
import os


def _ensure_suffix(filename: str, suffix: str) -> str:
    """
    确保文件名以指定的后缀结尾，如果没有则自动补全
    :param filename: 文件名
    :param suffix: 期望的后缀 (如: '.m4s', '.mp4')
    :return: 带正确后缀的文件名
    """
    if not filename.lower().endswith(suffix):
        return filename + suffix
    return filename


def convert(video: str = 'video.m4s', audio: str = 'audio.m4s', output: str = 'output.mp4') -> bool:
    r"""
    将Android设备缓存的哔哩哔哩视频(音视频分开两个.m4s文件)合并为.mp4文件
    :param video: 输入的视频文件路径 (支持绝对路径或相对路径，必须为 .m4s)
    :param audio: 输入的音频文件路径 (支持绝对路径或相对路径，必须为 .m4s)
    :param output: 输出的MP4文件路径 (支持绝对路径或相对路径，必须为 .mp4)
    :return: 执行情况 (True 表示成功, False 表示失败)
    """
    # 获取 ffmpeg 可执行文件路径
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg.exe')

    # 检查 ffmpeg 是否存在
    if not os.path.exists(ffmpeg_path):
        print(f"错误: 未找到 ffmpeg.exe，请确保 ffmpeg 文件夹位于安装目录下。")
        return False

    # 检查并补全输入文件的后缀
    video = _ensure_suffix(video, '.m4s')
    audio = _ensure_suffix(audio, '.m4s')
    output = _ensure_suffix(output, '.mp4')

    # 转换为绝对路径
    video = os.path.abspath(video)
    audio = os.path.abspath(audio)
    output = os.path.abspath(output)

    # 检查输入文件是否存在
    if not os.path.exists(video):
        print(f"错误: 输入视频文件不存在: {video}")
        return False

    if not os.path.exists(audio):
        print(f"错误: 输入音频文件不存在: {audio}")
        return False

    try:
        # 调用 ffmpeg 命令，将音频和视频合并为输出文件
        command = [
            ffmpeg_path,
            '-i', audio,
            '-i', video,
            '-codec', 'copy',
            output
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 检查返回码是否成功
        if result.returncode == 0:
            print(f"合并成功: {output}")
            return True
        else:
            # 如果失败，打印详细错误信息
            print(f"合并失败: {result.stderr.decode('utf-8')}")
            return False
    except Exception as e:
        print(f"发生异常: {e}")
        return False


def combine(directory: str, output: str = 'output.mp4') -> bool:
    ...


def auto_console(blue: bool = False):
    ...
