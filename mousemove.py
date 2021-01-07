#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
File:mousemove.py
Author:T
Description:スクリーンセーバー防止スクリプト
-----------------------------------------------
〔変更履歴〕
2020/09/26 T 新規作成
"""
import pyautogui as pg
import time

try:
    while True:
        time.sleep(3)
        pg.moveTo(100, 100, 0.5)
        pg.moveTo(100, 200, 0.5)
        pg.moveTo(200, 200, 0.5)
        pg.moveTo(200, 100, 0.5)
except KeyboardInterrupt:
    print('job!')
