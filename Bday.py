import random
import math

def simulate_birthday_paradox(num_bits, num_trials):
    space_size = 2 ** num_bits #количество "дней" в году
    attempt_nums = []

    for _ in range(num_trials):
        seen = set()
        steps = 0
        while True:
            value = random.randint(0, space_size - 1)
            steps += 1

            if value in seen:
                attempt_nums.append(steps)
                break
            else:
                seen.add(value)

    avg_steps = sum(attempt_nums) / len(attempt_nums)
    theoretical = math.sqrt(math.pi / 2) * math.sqrt(space_size)

    print(f"Бит: {num_bits}, вариантов: {space_size}")
    print(f"  Среднее число шагов до коллизии: {avg_steps:.2f}")
    print(f"  Теоретическая оценка (√(πN/2)):  {theoretical:.2f}")
    print(f"  Наивная оценка (√N):             {math.sqrt(space_size):.2f}")
    print()

random.seed(10)
for x in [8, 12, 16, 20]:
    simulate_birthday_paradox(x, 200)
