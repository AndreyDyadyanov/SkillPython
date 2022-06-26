pack_amt = int(input('Кол-во пакетов: '))
pack_list = []
decoding_list = []
raw_packs = 0

for i in range(pack_amt):
    print('\nПакет номер', i + 1)
    for bit_num in range(1, 5):
        print(bit_num, 'бит:', end=' ')
        bit = int(input())
        pack_list.append(bit)
    if pack_list.count(-1) <= 1:
        decoding_list.extend(pack_list)
    else:
        raw_packs += 1
        print('Много ошибок в пакете.')

    pack_list = []

print('\nПолученное сообщение:', decoding_list)
print('Кол-во ошибок в сообщении:', decoding_list.count(-1))
print('Кол-во потерянных пакетов:', raw_packs)

