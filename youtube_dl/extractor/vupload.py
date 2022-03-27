# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import (
    parse_duration,
    parse_filesize,
    extract_attributes,
    int_or_none,
)


class VuploadIE(InfoExtractor):
    _VALID_URL = r'https://vupload\.com/(?:[ve]/)?(?P<id>[a-z0-9]+)'
    _TESTS = [
        {
            'url': 'https://vupload.com/v/u28d0pl2tphy',
            'md5': '9b42a4a193cca64d80248e58527d83c8',
            'info_dict': {
                'id': 'u28d0pl2tphy',
                'ext': 'mp4',
                'description': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
                'title': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
            }
        },
        {
            'url': 'https://vupload.com/u28d0pl2tphy',
            'md5': '9b42a4a193cca64d80248e58527d83c8',
            'info_dict': {
                'id': 'u28d0pl2tphy',
                'ext': 'mp4',
                'description': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
                'title': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
            }
        },
        {
            'url': 'https://vupload.com/e/u28d0pl2tphy',
            'md5': '9b42a4a193cca64d80248e58527d83c8',
            'info_dict': {
                'id': 'u28d0pl2tphy',
                'ext': 'mp4',
                'description': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
                'title': 'md5:e9e6c0045c78cbf0d5bb19a55ce199fb',
            }
        },
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage("https://vupload.com/" + video_id, video_id)
        title = self._html_search_regex(r'<title>(.+?)</title>', webpage, 'title')
        video_url = self._html_search_regex(r'(https?://.*.megaupload.[a-z]+/hls/,[^/]+/master\.m3u8)', webpage, 'video')
        duration = parse_duration(self._html_search_regex(
            r'<i\s*class=["\']fad\s*fa-clock["\']></i>\s*([\d:]+)\s*</div>', webpage, 'duration', fatal=False))
        filesize_approx = parse_filesize(self._html_search_regex(
            r'<i\s*class=["\']fad\s*fa-save["\']></i>\s*([^<]+)\s*</div>', webpage, 'filesize', fatal=False))
        extra_video_info = extract_attributes(self._html_search_regex(
            r'(<video[^>]+>)', webpage, 'video_info', fatal=False))
        description = self._html_search_meta('description', webpage)

        return {
            'id': video_id,
            'url': video_url,
            'duration': duration,
            'filesize_approx': filesize_approx,
            'width': int_or_none(extra_video_info.get('width')),
            'height': int_or_none(extra_video_info.get('height')),
            'format_id': extra_video_info.get('height', '') + 'p',
            'title': title,
            'ext': "mp4",
            'description': description,
        }
