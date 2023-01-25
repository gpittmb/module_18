total_price = 0
tickets = int(input('Введите кол-во билетов: '))
for i in range(tickets):
    i += 1
    age = int(input(f'Введите возраст для билета №{i}: '))
    if age < 18:
            print('Билет бесплатный')
    elif 18 <= age < 25:
            total_price += 990
            print('Стоимость билета - 990 руб.')
    else:
            total_price += 1390
            print('Стоимость билета - 1390 руб.')
if tickets > 3:
    total_price = total_price * 0.9
    print(f'Сумма к оплате - {total_price} руб. (с учетом скидки 10%, т.к. вы зарегистрировали больше 3-х человек)!')
else:
    print(f'Сумма к оплате - {total_price} руб.')
