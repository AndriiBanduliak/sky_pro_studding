medals = [
    'gold', 'silver', 'bronze', 'gold', 'gold', 'silver', 'silver', 'silver',
    'bronze', 'bronze', 'bronze', 'bronze'
]
gold_medal = 0
silver_medal = 0
bronze_medal = 0


for medal in medals:
    if medal == 'gold':
        gold_medal +=1
    elif medal == 'silver':
        silver_medal +=1
    else: bronze_medal +=1

print(f"Золотых: {gold_medal}")
print(f"Серебрянных: {silver_medal}")
print(f"Бронзовых: {bronze_medal}")