def analyze_user_activity(log_file_path: str) -> dict:
    users = set()
    action_counts = {}
    user_duration = {}

    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split()

            if len(data) != 4:
                continue

            timestamp, user_id, action, duration = data

            try:
                duration = float(duration)
            except ValueError:
                continue

            users.add(user_id)

            if action not in action_counts:
                action_counts[action] = 0
            action_counts[action] += 1

            if user_id not in user_duration:
                user_duration[user_id] = 0
            user_duration[user_id] += duration

    if user_duration:
        most_active_user = max(user_duration, key=user_duration.get)
        average_session_time = sum(user_duration.values()) / len(user_duration)
    else:
        most_active_user = None
        average_session_time = 0.0

    return {
        "action_counts": action_counts,
        "average_session_time": average_session_time,
        "most_active_user": most_active_user,
        "total_users": len(users)
    }
if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
