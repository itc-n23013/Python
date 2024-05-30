import pyinputplus as pyip

bread_prices = {'小麦パン':100,'白パン':90,'サワー種':110}
tanpaku_prices = {'チキン':80,'ターキー':80,'ハム':70,'豆腐':60}
cheese_prices = {'チェダー':40,'スイス':50,'モッツァレラ':45}

bread_choice = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='パンの種類を選んでください:\n', numbered=True)
tanpaku_choice = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n', numbered=True)

want_cheese = pyip.inputYesNo('チーズが必要ですか？(yes/no):\n')
cheese_choice = None
if want_cheese == 'yes':
    cheese_choice = pyip.inputMenu(['チェダー','スイス','モッツァレラ'], prompt='チーズの種類を選んでください:\n', numbered=True)

num_sandwiches = pyip.inputInt('サンドイッチがいくつ欲しいですか？:\n',min=1)

total_cost = (bread_prices[bread_choice] + tanpaku_prices[tanpaku_choice]) * num_sandwiches
if cheese_choice:
    total_cost += cheese_prices[cheese_choice] * num_sandwiches

print(f'\nサンドイッチの合計金額は{total_cost}円です。')
