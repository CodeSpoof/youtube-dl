# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class VOEIE(InfoExtractor):
    IE_NAME = 'voe'
    IE_DESC = 'VOE.SX'
    _VALID_URL = r'https?://voe\.sx/(e/)?(?P<id>[a-z0-9]+)'
    _TESTS = [
        {
            'url': 'https://voe.sx/e/for0ra8at5al',
            'info_dict': {
                'id': 'for0ra8at5al',
                'title': 'pexels maksim goncharenok 5642529',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        },
        {
            'url': 'https://voe.sx/for0ra8at5al',
            'info_dict': {
                'id': 'for0ra8at5al',
                'title': 'pexels maksim goncharenok 5642529',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        },
        {
            'url': 'https://voe.sx/e/coerjif32dkc',
            'info_dict': {
                'id': 'coerjif32dkc',
                'title': 'production ID:4010941',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        },
        {
            'url': 'https://voe.sx/coerjif32dkc',
            'info_dict': {
                'id': 'coerjif32dkc',
                'title': 'production ID:4010941',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        },
        {
            'url': 'https://voe.sx/e/rj5rlqvz8lfg',
            'info_dict': {
                'id': 'rj5rlqvz8lfg',
                'title': 'pexels zura narimanishvili 5490419',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        },
        {
            'url': 'https://voe.sx/rj5rlqvz8lfg',
            'info_dict': {
                'id': 'rj5rlqvz8lfg',
                'title': 'pexels zura narimanishvili 5490419',
                'thumbnail': r're:^https?://.*\.jpg$',
                'ext': 'mp4',
            },
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(
            'https://voe.sx/e/%s' % video_id, video_id)

        m3u8 = self._search_regex(
            r'(https.+m3u8)',
            webpage, 'm3u8')

        title = self._search_regex(
            r'<title>Watch (?P<title>.+)<\/title>',
            webpage, 'title', group='title')
        print(title)
        thumbnail = self._search_regex(
            r'data-poster=["\'](?P<thumbnail>https.+)["\']',
            webpage, 'thumbnail', group='thumbnail')

        formats = self._extract_m3u8_formats(m3u8, video_id)
        self._sort_formats(formats)

        return {
            'id': video_id,
            'title': title,
            'formats': formats,
            'thumbnail': thumbnail,
            'ext': "mp4",
        }
