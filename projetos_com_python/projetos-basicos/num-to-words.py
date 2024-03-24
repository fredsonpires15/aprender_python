def spell_number(number):
    # Dicionários para soletrar os números
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    thousands = ['', 'thousand', 'million', 'billion', 'trillion']

    if number == 0:
        return 'zero'

    # Função auxiliar para soletrar números menores que 1000
    def spell_below_1000(num):
        if num == 0:
            return ''
        elif num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ' ' + units[num % 10]
        else:
            return units[num // 100] + ' hundred ' + spell_below_1000(num % 100)

    # Função principal para soletrar números
    result = ''
    negative = False
    if number < 0:
        negative = True
        number = abs(number)

    # Soletrando o número por partes de milhares
    for i in range(len(thousands)):
        part = number % 1000
        if part != 0:
            if negative:
                result = '-' + spell_below_1000(part) + ' ' + thousands[i] + ' ' + result
            else:
                result = spell_below_1000(part) + ' ' + thousands[i] + ' ' + result
        number //= 1000

    return result.strip()


# Exemplo de uso
while True:
    try:
        num = float(input("Digite um número: "))
        print(spell_number(int(num)))
        break
    except ValueError:
        print("Por favor, insira um número válido.")
