import requests
import json
from functools import partial


class test_doubanSearch(object):
    @staticmethod
    def search(params, expectNum=None):
        url = 'https://api.douban.com/v2/movie/search'
        r = requests.get(url, params=params)
        print('Search Params:\n', json.dumps(params, ensure_ascii=False))
        print('Search Response:\n', json.dumps(
            r.json(), ensure_ascii=False, indent=4))

    def test_q(self):
        # 校验搜索条件 q
        qs = [u'白夜追凶', u'大话西游', u'周星驰', u'张艺谋', u'周星驰,吴孟达',
              u'张艺谋,巩俐', u'周星驰,大话西游', u'白夜追凶,潘粤明']
        for q in qs:
            params = dict(q=q)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(
                params, ensure_ascii=False).encode('utf-8')
            yield (f,)
