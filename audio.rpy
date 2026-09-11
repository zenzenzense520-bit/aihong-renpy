## 哀鸿 - 音频资源与播放通道
## 2026-09-11：只保留已落盘且许可明确的音频，避免运行时缺文件。

define audio_dark_ambient = "audio/ambient/deep_humidity.ogg"
define sfx_fire_crackle = "audio/sfx/fire_crackle.ogg"

init python:
    renpy.music.register_channel("ambient", mixer="sfx", loop=True)

    def play_ambient(track, fadein=1.5):
        """在独立环境声通道循环播放，避免覆盖一次性音效。"""
        renpy.music.play(track, channel="ambient", fadein=fadein, loop=True)

    def stop_ambient(fadeout=1.0):
        """平滑停止环境声。"""
        renpy.music.stop(channel="ambient", fadeout=fadeout)

    def play_se(track):
        """播放一次性音效。"""
        renpy.sound.play(track)
