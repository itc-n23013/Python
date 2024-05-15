import random

def generate_coin_flips(length):
    return [random.choice(['裏', '表']) for _ in range(length)]

def has_six_in_a_row(sequence):
    return any(sequence[i:i+6] == ['裏'] * 6 or sequence[i:i+6] == ['表'] * 6 for i in range(len(sequence) - 5))

number_of_streaks = sum(has_six_in_a_row(generate_coin_flips(100)) for _ in range(10000))

print(f'同じ面が6連続出現する確率: {number_of_streaks / 10000 * 100:.2f}%')
