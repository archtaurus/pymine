#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mixer.py
"""
Mixer
sound and music modules for the game PyMine.
"""
import pygame
from pygame.locals import *

pygame.mixer.init()
channels = pygame.mixer.get_num_channels()
sound = {
    "boom": pygame.mixer.Sound('resource/sound/boom.wav'),
    "dig": pygame.mixer.Sound('resource/sound/dig.wav'),
    "flag": pygame.mixer.Sound('resource/sound/flag.wav'),
    "win": pygame.mixer.Sound('resource/sound/win.wav'),
    "loss": pygame.mixer.Sound('resource/sound/loss.wav')}
music = {
    "bgm": 'resource/music/bgm.wav'}


def play_sound(sound_name, ch = None):
    if ch == None:
        sound[sound_name].play()
    else:
        channel = pygame.mixer.Channel(ch)
        channel.stop()
        channel.play(sound[sound_name])


def stop_sound():
    for i in range(channels):
        channel = pygame.mixer.Channel(i)
        channel.stop()


def load_music(music_name):
    pygame.mixer.music.load(music[music_name])


def play_music():
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()


def _test():
    from sys import exit
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("mixer -> _test()")
    screen = pygame.display.set_mode((320, 200), 0, 32)
    screen.fill((255, 255, 255))
    pygame.display.flip()
    load_music("bgm")
    play_music()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    play_sound("boom")
                elif event.button == 3:
                    play_sound("dig")

if __name__ == "__main__":
    _test()

'''
音效:pygame.mixer
要在游戏中播放碰撞、爆炸、语音等音效，

这个模块支持同时播放多个音效文件，多个文件在多个不同的通道Channel中播放，一个通道一次只能播放一个音效文件。

pygame.init() 进行全部模块初始化
pygame.mixer.init() 只初始化音频部分
pygame.mixer.get_num_channels() 可以这样查看总共有多少个通道
channel = pygame.mixer.Channel(i) 使用取得第i个通道。
channel = pygame.mixer.find_channel() 自动取得一个空闲的通道（没有音效正在播放的通道）。
sound = pygame.mixer.Sound('/home/liumin/love.wav')使用指定文件名载入一个音频文件，并创建一个Sound对象。 音频文件可以是wav,ogg等格 式。音频文件的内容会被全部载入到内存中。
channel.play(sound) 使用在一个通道中播放一个音效。
sound.play() 自动找一个空闲的通道播放音效。
sound.stop() 停止音效sound的播放。或者用
channel.stop() 停止在通道channel中播放的音效。正在播放音效的通道还可以用
channel.pause() 暂停通道中的音效。
channel.unpause() 继续播放。
channel.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。 对于一个通道可以用 channel.get_busy() 检查它是否正在播放音效。当一个通道中的音效播放完成时，可以通过事件通知给用户程序。
channel.set_endevent(pygame.USEREVENT + 1) 来设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。
channel.queue(sound) 为正在播放音效的通道指定下一个要播放的音效。当前的音效播放完成后，下一个音效会自动播放。一个通道只能有一个等待播放的音效。
channel.set_volume(value) 来设置通道中播放的音效的音量。
sound.set_volume(value) 来设置单个音效的音量。两者的取值范围都是0.0到1.0。音效播放的实际音量是通道音量和音效音量的乘积，比如通道音量0.5，音效音量0.6，则实际播放的音量为0.3。
NOTE： 音效和音乐的区别是：音效要整个文件载入到Sound对象中才能播放，而音乐不用完全载入，而以流的方式播放。
'''