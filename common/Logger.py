# coding = "utf-8"

import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='debug', when='D', backCount=5,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(level))
        format_str = logging.Formatter(fmt)
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = TimedRotatingFileHandler(filename=filename, when=when, interval=1, backupCount=3, encoding="utf-8")
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)
