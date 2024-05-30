import random
import time

def mulquiz():
    questions = random.sample([(i, j) for i in range(10) for j in range(10)], 10)

    for num1, num2 in questions:
        correct_answer = num1 * num2
        attempts = 3

        while attempts > 0:
            print(f"{num1} x {num2} = ?")
            start_time = time.time()

            try:
                answer = int(input())
                if time.time() - start_time > 8:
                    print("時間切れ!")
                    break
                if answer == correct_answer:
                    print("正解!")
                    time.sleep(1)
                    break
                else:
                    attempts -= 1
                    print(f"不正解！残り{attempts}回回答できます。")
            except ValueError:
                print("数字を入力してください。")
                attempts -= 1
                print(f"不正解！残り{attempts}回回答できます。")
            if attempts == 0:
                print(f"答えは{correct_answer}")
                time.sleep(1)
                break

if __name__ == "__main__":
    mulquiz()

