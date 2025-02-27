r"""
:author: WaterRun
:date: 2025-02-27
:description: biliffm4s的源码，支持多系统兼容
:file: biliffm4s.py
:version: 1.1
"""

import subprocess
import os
import platform


def _ensure_suffix(filename: str, suffix: str) -> str:
    r"""
    确保文件名以指定的后缀结尾，如果没有则自动补全
    :param filename: 文件名
    :param suffix: 期望的后缀 (如: '.m4s', '.mp4')
    :return: 带正确后缀的文件名
    """
    if not filename.lower().endswith(suffix):
        return filename + suffix
    return filename


def _get_ffmpeg_path() -> str:
    r"""
    动态获取当前系统的 ffmpeg 可执行文件路径
    :return: ffmpeg 的完整路径
    """
    base_dir = os.path.dirname(__file__)  # 当前文件所在目录
    system = platform.system().lower()  # 获取系统名称

    if system == "windows":  # Windows 系统
        ffmpeg_path = os.path.join(base_dir, "ffmpeg", "win", "ffmpeg.exe")
    elif system == "linux":  # Linux 系统
        ffmpeg_path = os.path.join(base_dir, "ffmpeg", "linux", "ffmpeg")
    elif system == "darwin":  # macOS 系统
        ffmpeg_path = os.path.join(base_dir, "ffmpeg", "mac", "ffmpeg_mac")
    else:  # 不支持的系统
        raise OSError(f"不支持的操作系统: {system}")

    if not os.path.exists(ffmpeg_path):  # 检查文件是否存在
        raise FileNotFoundError(f"未找到 ffmpeg 可执行文件: {ffmpeg_path}")

    return ffmpeg_path


def convert(video: str = 'video.m4s', audio: str = 'audio.m4s', output: str = 'output.mp4') -> bool:
    r"""
    将音视频.m4s合并为.mp4文件
    :param video: 输入的视频文件路径 (支持绝对路径或相对路径，必须为 .m4s)
    :param audio: 输入的音频文件路径 (支持绝对路径或相对路径，必须为 .m4s)
    :param output: 输出的MP4文件路径 (支持绝对路径或相对路径，必须为 .mp4)
    :return: 执行情况 (True 表示成功, False 表示失败)
    """
    try:
        ffmpeg_path = _get_ffmpeg_path()  # 动态获取 ffmpeg 路径

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
    r"""
    自动对指定目录进行查找 video.m4s 和 audio.m4s，并合并为 .mp4
    :param directory: 查找的路径
    :param output: 输出的MP4文件路径 (支持绝对路径或相对路径，必须为 .mp4)
    :return: 执行情况 (True 表示成功, False 表示失败)
    """
    # 转换为绝对路径
    directory = os.path.abspath(directory)
    output = _ensure_suffix(output, '.mp4')
    output = os.path.abspath(output)

    # 检查目录是否存在
    if not os.path.isdir(directory):
        print(f"错误: 目录不存在: {directory}")
        return False

    # 查找 video.m4s 和 audio.m4s
    video_files = [f for f in os.listdir(directory) if f.lower() == 'video.m4s']
    audio_files = [f for f in os.listdir(directory) if f.lower() == 'audio.m4s']

    if len(video_files) != 1:
        print(f"错误: 找到 {len(video_files)} 个 video.m4s 文件，请确保目录中有且仅有一个 video.m4s 文件。")
        return False

    if len(audio_files) != 1:
        print(f"错误: 找到 {len(audio_files)} 个 audio.m4s 文件，请确保目录中有且仅有一个 audio.m4s 文件。")
        return False

    # 获取完整路径
    video_path = os.path.join(directory, video_files[0])
    audio_path = os.path.join(directory, audio_files[0])

    # 调用 convert 函数进行合并
    return convert(video=video_path, audio=audio_path, output=output)
