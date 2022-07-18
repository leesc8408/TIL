import json
from pprint import pprint
from webbrowser import get


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    review = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview')
    }
    names = []   
    for i in movie['genre_ids']:
        for a in genres:
            if a['id'] == i:
                names.append(a.get('name'))
    review['genre_names'] = names

    return review



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))