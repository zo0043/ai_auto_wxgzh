# 注意： 打包安装软件时，所有用到的模块都要在此处导入

import asyncio  # noqa 841
import shutil  # noqa 841
from collections import deque  # noqa 841
import threading  # noqa 841
import queue  # noqa 841
import os  # noqa 841
import webbrowser  # noqa 841
import ctypes  # noqa 841
import sys  # noqa 841
import PySimpleGUI as sg  # noqa 841
import warnings  # noqa 841
import yaml  # noqa 841
import re  # noqa 841
import random  # noqa 841
from bs4 import BeautifulSoup  # noqa 841
import requests  # noqa 841
import time  # noqa 841
from typing import Optional, List, Dict  # noqa 841
from dataclasses import dataclass  # noqa 841
from enum import Enum  # noqa 841
from datetime import datetime, timedelta  # noqa 841
from io import BytesIO  # noqa 841
from http import HTTPStatus  # noqa 841
from urllib.parse import urlparse, unquote  # noqa 841
from pathlib import PurePosixPath  # noqa 841
from dashscope import ImageSynthesis  # noqa 841
import mimetypes  # noqa 841
import json  # noqa 841
import logging  # noqa 841

from crewai.tools import BaseTool  # noqa 841
from typing import Type  # noqa 841
from pydantic import BaseModel, Field  # noqa 841
import glob  # noqa 841
from crewai import Agent, Crew, Process, Task  # noqa 841
from crewai.project import CrewBase, agent, crew, task  # noqa 841


import src.ai_auto_wxgzh.gui.MainGUI as MainGUI


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:  # noqa841
        return False


def run():
    MainGUI.gui_start()


def admin_run():
    if is_admin():
        run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 0)


if __name__ == "__main__":

    if len(sys.argv) > 1:  # 第一个是文件名，如果多于1个，说明其他模式启动
        if sys.argv[1] == "-d":
            run()
        else:
            admin_run()
    else:
        admin_run()
