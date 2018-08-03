def refine_user_info(user_info=None):
    # todo : complete the code
    try:
        refined_user_info = {
            'media_count': user_info['media_count'],
            'followers_count': None,
            'following_count': None,
            'user_name': None,
            'user_id': None,
            'full_name': None,
        }
    except KeyError:
        refined_user_info = dict()
    return refined_user_info


def refine_user_list(user_list=None):
    refined_user_list = []
    # todo : complete the variables
    for user in user_list:
        try:
            refined_user_list.append(
                {
                    'user_id': user['pk'],
                    'user_name': None,
                    'full_name': None,
                    'is_private': None
                }
            )
        except KeyError:
            print("There is an error.")

    return refined_user_list


def engagement_calculator(user_posts=None, user_info=None):
    sum_likes = 0
    sum_comments = 0
    # todo : set variables:
    followers_count = None
    posts_count = None

    for post in user_posts['posts']:
        try:
            like_count = None
        except KeyError:
            like_count = 0
        try:
            comment_count = None
        except KeyError:
            comment_count = 0
        sum_likes += like_count
        sum_comments += comment_count

    sum_engagement = sum_comments + sum_likes
    # todo : implement the engagement formula
    engagement_rate = None
    engagement_rate = round(engagement_rate, 2)
    engagement_info = {
        'engagement_rate': engagement_rate,
        'likes': int(sum_likes / posts_count),
        'comments': int(sum_comments / posts_count)
    }
    # todo : add enagement rate to user info
    # search the web : how to add two dictionaries or how to update a dictionary

    return user_info