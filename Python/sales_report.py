sales = []
for _ in range(1,8):
  daily_sales = float(input(f"Enter Day- {_} sales : "))
  sales.append(daily_sales)

total = 0
for i in sales:
  total += i

print(f"\nTotal sales of the week : {total}")