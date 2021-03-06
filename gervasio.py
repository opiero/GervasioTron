import random
from instapy import InstaPy
from datetime import datetime

def Gervasio(username, password):
    session = InstaPy(username=username, password=password, headless_browser=True)
    session.login()

    session.set_relationship_bounds(enabled=True, max_followers=12500)

    session.set_do_like(enabled=True, percentage=80)
    session.set_dont_like(['bolsonaro', 'b17', 'bolsonaro2022', 'b22', 'direita'])

    session.set_do_follow(enabled=True, percentage=3)

    session.set_do_story(enabled = True, percentage=50, simulate = True)

    session.set_user_interact(randomize=True, percentage=40, media='Photo')
    #session.set_smart_hashtags(['golang', 'softwaredeveloper', 'python', 'tech', 'programming'], limit=10, sort='top', log_tags=True)


    session.set_quota_supervisor(enabled=True,
                                sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                sleepyhead=True,
                                stochastic_flow=True,
                                notify_me=True,
                                peak_likes_hourly=57,
                                peak_likes_daily=585,
                                peak_comments_hourly=21,
                                peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                peak_unfollows_hourly=35,
                                peak_unfollows_daily=402,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=4700)

    tags = ['sp', 'saopaulo', 'sampa', 'splovers', 'saopaulocity', 'sp4you',
        'amosp', '011', 'spdagaroa', 'saopaulowalk', 'serpaulistano', 'olharesdesampa',
        'sãopaulo', 'coolsampa', 'estadao', 'igerssaopaulo', 'ig_saopaulo', 'sousampa',
        'saopaulonline', 'ilovesp', 'cidadedagaroa', 'sampacity', 'sampalovers',
        'amorpaulista', 'saopaulo_originals', 'igerssp', 'spcity', 'brazil', 'paulista', 'ibira']

    number_of_tags = len(tags)


    random.seed(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    session.story_by_tags(random.sample(tags, number_of_tags))

    session.like_by_tags(random.sample(tags, number_of_tags), amount=30, randomize=True)

    session.end()