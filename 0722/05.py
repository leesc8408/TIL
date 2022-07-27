import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    chu_list = {}
    id_list = []
    cast_list = []
    crew_list = []

    url = f'https://api.themoviedb.org/3'
    path = f'/search/movie'
    params = {
        'api_key' : 'a275979c03887da2638b3b3aabee6ccf',
        'language' : 'ko',
        'query' : title
    }
    respon1 = requests.get(url + path, params = params).json()
    # print(respon1, type(respon))
    
    if respon1['results']:
        for i in respon1.get('results'):
            id_list.append(i.get('id'))
        # print(id_list)
        movie_id = id_list[0]

        url = f'https://api.themoviedb.org/3'
        path = f'/movie/{movie_id}/credits' 
        params = {
            'api_key' : 'a275979c03887da2638b3b3aabee6ccf',
            'language' : 'ko',
            'movie_id' : movie_id
        }
        respon2 = requests.get(url + path, params = params).json()
        # print(respon2.keys())

        for i in respon2.get('cast'):
            # print(i, type(i))
            if i.get('cast_id') < 10:
                cast_list.append(i.get('name'))
        # print(cast_list)
        for i in respon2.get('crew'):
            # print(i, type(i))
            if i.get('department') == 'Directing':
                crew_list.append(i.get('name'))
        # print(crew_list)

        chu_list['cast'] = cast_list
        chu_list['crew'] = crew_list        

        return chu_list
    else:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
