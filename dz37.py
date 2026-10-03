import requests
import json
from datetime import datetime, timezone
from collections import Counter


def analyze_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке данных: {e}")
        return



    processed_posts = []
    user_post_counts = Counter()
    title_lengths = []

    for post in posts:
        title_len = len(post['title'])
        body_len = len(post['body'])
        total_len = title_len + body_len

        processed_posts.append({
            'id': post['id'],
            'userId': post['userId'],
            'total_length': total_len
        })

        user_post_counts[post['userId']] += 1
        title_lengths.append(title_len)


    top_longest_posts = sorted(processed_posts, key=lambda x: x['total_length'], reverse=True)[:5]


    total_posts = len(posts)


    avg_body_length = sum(len(p['body']) for p in posts) / total_posts if total_posts > 0 else 0


    most_active_user_id = user_post_counts.most_common(1)[0][0]


    sorted_title_lengths = sorted(title_lengths)
    n = len(sorted_title_lengths)
    if n % 2 == 1:
        median_title_length = sorted_title_lengths[n // 2]
    else:
        median_title_length = (sorted_title_lengths[n // 2 - 1] + sorted_title_lengths[n // 2]) / 2


    posts_per_user_map = {}
    for p in processed_posts:
        uid = p['userId']
        if uid not in posts_per_user_map:
            posts_per_user_map[uid] = []
        posts_per_user_map[uid].append(p)


    posts_per_user_list = []
    for uid, user_posts in posts_per_user_map.items():
        posts_per_user_list.append({
            "userId": uid,
            "count": len(user_posts),
            "posts": user_posts
        })



    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": url,
        "summary": {
            "total_posts": total_posts,
            "avg_body_length": round(avg_body_length, 1),
            "most_active_user_id": most_active_user_id,
            "median_title_length": int(median_title_length) if median_title_length == int(
                median_title_length) else median_title_length
        },
        "posts_per_user": posts_per_user_list,
        "top_longest_posts": top_longest_posts
    }


    output_filename = "report.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"Отчет успешно сохранен в файл '{output_filename}'")
    print(f"Всего постов: {total_posts}")
    print(f"Самый активный пользователь: ID {most_active_user_id}")


if __name__ == '__main__':
    analyze_posts()