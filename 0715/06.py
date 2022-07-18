import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    many_review = []
    for movie in movies:
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
        many_review.append(review)

    return many_review
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))