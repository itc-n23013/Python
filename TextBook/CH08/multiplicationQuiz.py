import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for questions_number in range(number_of_questions):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{questions_number + 1}: {num1} x {num2} = '

    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],
                              blockRegexes=[('.*', '不正解!')],
                              timeout=8, limit=3)

    except pyip.TimeoutException:
        print('時間切れ!')
    except pyip.RetryLimitException:
        print('回数制限超え!')

    else:
        print('正解!')
        correct_answers += 1

    time.sleep(1)
print(f'得点: {correct_answers} / {number_of_questions}')
