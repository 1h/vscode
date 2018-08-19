
class check_response():
    @staticmethod
    def check_result(response, params, expectNum=None):
        # 由于搜索结果存在模糊匹配的情况，这里简单处理只校验第一个返回结果的正确性
        if expectNum is not None:
            # 期望结果数目不为None时，只判断返回结果数目
            eq_(expectNum, len(response['subjects']), '{0}!={1}'.format(
                expectNum, len(response['subjects'])))
        else:
            if not response['subjects']:
                # 结果为空，直接返回失败
                assert False
            else:
                # 结果不为空，校验第一个结果
                subject = response['subjects'][0]
                # 先校验搜索条件tag
                if params.get('tag'):
                    for word in params['tag'].split(','):
                        genres = subject['genres']
                        ok_(word in genres, 'Check {0} failed!'.format(
                            word.encode('utf-8')))

                # 再校验搜索条件q
                elif params.get('q'):
                    # 依次判断片名，导演或演员中是否含有搜索词，任意一个含有则返回成功
                    for word in params['q'].split(','):
                        title = [subject['title']]
                        casts = [i['name'] for i in subject['casts']]
                        directors = [i['name'] for i in subject['directors']]
                        total = title + casts + directors
                        ok_(any(word.lower() in i.lower() for i in total),
                            'Check {0} failed!'.format(word.encode('utf-8')))

    @staticmethod
    def check_pageSize(response):
        # 判断分页结果数目是否正确
        count = response.get('count')
        start = response.get('start')
        total = response.get('total')
        diff = total - start

        if diff >= count:
            expectPageSize = count
        elif count > diff > 0:
            expectPageSize = diff
        else:
            expectPageSize = 0

        eq_(expectPageSize, len(response['subjects']), '{0}!={1}'.format(
            expectPageSize, len(response['subjects'])))
