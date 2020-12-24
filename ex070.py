# Product Registration
soma = qnt_mil = cheaper = count = 0

cheaper_product = ''


while True:
    product = input('Product Name: ').strip()
    price = abs(float(input('Price: R$ ').strip()))
    soma += price
    count += 1
    if price > 1000:
        qnt_mil += 1
    if count == 1:
        cheaper = price
    else:
        if price < cheaper:
            cheaper = price
            cheaper_product = product

    ask = input('Do you want to continue? [Y/N] ').strip().upper()
    while ask not in 'YN':
        ask = input('Do you want to continue? [Y/N] ').strip().upper()
    if ask == 'N':
        break
print('-' * 10 + 'PROGRAM FINISHED' + '-' * 10)
print(f'The sum of products is {soma:.2f}.')
print(f'We have {qnt_mil} products that costs more than R$ 1000,00.')
print(f'The cheaper product is {cheaper_product} with price of R$ {cheaper:.2f}.')
