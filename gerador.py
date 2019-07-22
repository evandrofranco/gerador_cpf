import random


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - val if val > 1 else 0)
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)


def generate_cpf_wth_digits():
    cpf = [random.randint(0, 9) for x in range(9)]
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - val if val > 1 else 0)
    return '%s%s%s%s%s%s%s%s%s%s%s' % tuple(cpf)


def generate_cnpj():
    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]
    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj
    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])


def calculate_special_digit(l):
    digit = 0
    for i, v in enumerate(l):
        digit += v * (i % 8 + 2)
    digit = 11 - digit % 11
    return digit if digit < 10 else 0


def write_file(amount, file):
    f = open(file, 'w')
    for i in range(amount):
        f.write(generate_cpf_wth_digits() + '\n')
    f.close()


if __name__ == "__main__":
    # Exemplos:
    write_file(1000, 'cpf.txt')
    # print(generate_cpf())
    # print(generate_cpf_wth_digits())
    # print(generate_cnpj())
