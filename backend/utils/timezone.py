#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zoneinfo

from datetime import datetime
from datetime import timezone as datetime_timezone

from backend.core.conf import settings


class TimeZone:
    def __init__(self, tz: str = settings.DATETIME_TIMEZONE):
        self.tz_info = zoneinfo.ZoneInfo(tz)

    def now(self) -> datetime:
        """
        获取时区时间

        :return:
        """
        return datetime.now(self.tz_info)

    def f_datetime(self, dt: datetime) -> datetime:
        """
        datetime 时间转时区时间

        :param dt:
        :return:
        """
        return dt.astimezone(self.tz_info)

    def f_str(self, date_str: str, format_str: str = settings.DATETIME_FORMAT) -> datetime:
        """
        时间字符串转时区时间

        :param date_str:
        :param format_str:
        :return:
        """
        return datetime.strptime(date_str, format_str).replace(tzinfo=self.tz_info)

    @staticmethod
    def t_str(dt: datetime, format_str: str = settings.DATETIME_FORMAT) -> str:
        """
        时间转时间字符串

        :param dt:
        :param format_str:
        :return:
        """
        return dt.strftime(format_str)

    @staticmethod
    def f_utc(dt: datetime) -> datetime:
        """
        时区时间转 UTC（GMT）时区

        :param dt:
        :return:
        """
        return dt.astimezone(datetime_timezone.utc)


timezone: TimeZone = TimeZone()
