def memoize(score_A, score_B, position_A, position_B):
    # A = active, B = other
    if max(score_A, score_B) > 20:
        return [1, 0] if score_A > score_B else [0, 1] # someone has already won

    cache_key = (score_A, score_B, position_A, position_B)
    if cache_key in cache:
        return cache[cache_key]

    wins = [0, 0]
    for roll_1 in (1, 2, 3):
        for roll_2 in (1, 2, 3):
            for roll_3 in (1, 2, 3):
                updated_position_A = sum([position_A, roll_1, roll_2, roll_3]) % 10
                updated_score_A = score_A + updated_position_A + 1

                wins_A, wins_B = memoize(score_B, updated_score_A, position_B, updated_position_A)
                wins[0] += wins_B
                wins[1] += wins_A

    cache[cache_key] = wins
    return wins


cache = {}
with open('case1.txt') as fin:
    starts = list(map(int, [e.strip().split(" ")[-1] for e in fin.readlines()]))

    sim = memoize(0, 0, starts[0]-1, starts[1]-1)  # 1->0-indexed positions
    print(max(sim))

