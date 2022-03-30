ano = int(input('digite um ano e direi se é bissexto ou nao:'))
bi = ano % 4 and ano %100 != 00 or ano % 400 == 0
if bi == 0:
    print('o ano de {} é bissexto'.format(ano))
else:
    print('o ano nao é bissexto')
