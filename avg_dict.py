# data = [
#     {"team": "A", "points": 10},
#     {"team": "A", "points": 20},
#     {"team": "B", "points": 15}
# ]

# Return average points per team


def getavg(listofdic):
    agg_pts = {}
    avg_pts = []
    for team in listofdic:
        name = team.get("team")
        point = team.get("points")

        if name not in agg_pts:
            agg_pts[name] = [point,1]
        else:
            agg_pts.get(name)[0]+= point
            agg_pts.get(name)[1]+= 1

    for k,v in agg_pts.items():
        avg_pts.append({k: v[0]/v[1]})

    return avg_pts

# If they ask:
# “Can you optimize this?”
#
# Say:
# “Yes—instead of storing all values and recomputing sums, we can maintain a running sum and count
# to reduce memory usage and avoid repeated computations.”


if __name__ == '__main__':

    data = [
        {"team": "A", "points": 10},
        {"team": "A", "points": 20},
        {"team": "B", "points": 15}
    ]

    # Return average points per team
    print(getavg(data))
