import logging
import sys
import re
import os
import time
from datetime import datetime
from src.ai_auto_wxgzh.utils import utils
from src.ai_auto_wxgzh.utils import comm


def strip_ansi_codes(text):
    """去除 ANSI 颜色代码"""
    ansi_pattern = r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
    return re.sub(ansi_pattern, "", text)


class QueueLoggingHandler(logging.Handler):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def emit(self, record):
        try:
            msg = self.format(record)
            msg = strip_ansi_codes(msg)  # 去除 ANSI 代码
            self.queue.put({"type": "status", "value": f"LOG: {msg}"})
        except Exception:
            self.handleError(record)


class QueueStreamHandler:
    def __init__(self, queue):
        self.queue = queue
        self.original_stdout = sys.__stdout__  # 保存原始 stdout

    def write(self, msg):
        if msg.strip():
            clean_msg = strip_ansi_codes(msg.rstrip())  # 移除尾部换行/空格
            self.queue.put({"type": "status", "value": f"PRINT: {clean_msg}"})
            self.original_stdout.write(msg.rstrip() + "\n")  # 强制换行
            self.original_stdout.flush()

    def flush(self):
        self.original_stdout.flush()


def setup_logging(log_name, queue):
    """配置日志处理器，将 CrewAI 日志发送到队列"""
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    handler = QueueLoggingHandler(queue)
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s]: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False  # 避免重复日志
    for h in logger.handlers[:]:
        if isinstance(h, logging.StreamHandler) and h is not handler:
            logger.removeHandler(h)
    # 捕获 print 输出
    sys.stdout = QueueStreamHandler(queue)


# 支持多种日志文件
def get_log_path(log_name="log"):
    log_path = utils.get_res_path("logs", os.path.dirname(__file__))
    if not utils.get_is_release_ver():
        logs_path = utils.get_res_path("..\\..\\..\\logs", os.path.dirname(__file__))
    utils.mkdir(logs_path)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(logs_path, f"{log_name}_{timestamp}.log")
    return log_path


def print_log(msg, ui_mode=False, msg_type="status"):
    if ui_mode:
        comm.send_update(msg_type, msg)
    else:
        print(f"[{time.strftime('%H:%M:%S')}] [{msg_type.upper()}]: {msg}")
