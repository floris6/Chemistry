# Calculate the pH of an acidic solution (either completion or equilibrium) by entering the concentration
# The program uses the .txt file to request Ka from 98 different acids, if your acid is not included you can enter the Ka manually

import math

# Retreive Ka from .txt
def get_ka(formula):

    input_file = 'acid_constants.txt'

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # print(lines)

    for line in lines[1:]:  # Skip HEADER
            parts = line.strip().split('\t')  # Split by TAB
            acid_name, acid_formula, ka_value = parts[0], parts[1], parts[2]

            if acid_formula == formula:
                return acid_name, acid_formula, ka_value

    return "easteregg123_1"
# Format input
def format_formula(formula_input):

    # CHARGE
    superscript_map = {
        '+': '⁺',
        '-': '⁻',
        '1+': '¹⁺', '2+': '²⁺', '3+': '³⁺',
        '1-': '¹⁻', '2-': '²⁻', '3-': '³⁻'
    }

    for plain, pretty in superscript_map.items():
        if formula_input.endswith(' ' + plain):
            formula_input = formula_input.replace(' ' + plain, pretty)
            break

    # Digits
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    formatted = ''
    for char in formula_input:
        if char.isdigit():
            formatted += char.translate(subscript_map)
        else:
            formatted += char

    return formatted



print('A tool to calculate the pH of acidic reactions')
print("\t1. Type '1' to calculate the pH of a complete acidic reaction (strong acid)\t\tHA + H₂O ⇌ H₃O⁺ + A")
print("\t2. Type '2' to calculate the pH of a INcomplete acidic reaction (weak acid)\t\tHA + H₂O → H₃O⁺ + A")

rea = input('\nEnter Here: ')


if rea == '1':
    print("\n\n1. Complete reaction HA + H₂O → H₃O⁺ + A")
    print("\ta. Set up the reaction equation and provide the ratio between HA : H₃O⁺")
    HA = int(input('\t\tHA: '))
    H3O = int(input('\t\tH₃O⁺: '))

    ratio = H3O / HA
    print("\tb. Provide the concentration of the HA (in mole/L) example: 1.2e-2")
    HA_concentration = float(input('\t\t[HA]: '))

    pH = -math.log10(HA_concentration)
    print(f"\n\tpH = {pH}")


if rea == '2':
    print("\n\n2. Incomplete reaction HA + H₂O ⇌ H₃O⁺ + A")
    print("\ta. Provide the HA formula\t!!! H₂P₂O₇²⁻ --> H2P3O7 2- (seperate the charge)")
    formula_input = str(input('\t\tHA: '))

    formatted_formula = format_formula(formula_input)

    result = get_ka(formatted_formula)

    if result == 'easteregg123_1':
        print(f'\tb. Formula not found!\n\t\t1. You have make an error typing the formula: {formatted_formula}\n\t\t2. We use 98 acids and have not included ({formatted_formula}) in our system')
        print("\t\t3.Wish to manualy enter the Ka? Provide the Ka in such way: 2.2e-3. If you wish to stop type: '1' or 'stop' ")
        ka = input('\t\t\tKa = ')
        if ka == '1' or ka == 'stop':
            print('\n\t\tStopped!')
        else:
            print(f"\tc. Now provide the concentration (in mole/L) for example: HA = :1.2e-2")
            HA_concentration = float(input('\t\t[HA]: '))
            ka = float(ka)
            # CALCULATION [H₃O⁺]
            a = 1
            b = ka
            c = -HA_concentration * ka

            D = b * b - 4 * a * c
            x = (-b + math.sqrt(D)) / (2 * a)
            if x > 0:
                pH = -math.log10(x)
                print(f'\n\t[H₃O⁺] = {x}\t\tpH = {pH}')
            else:
                print('Error occurred during calculations')
    else:
        acid_name, acid_formula, ka_value = result
        print(f"\tb. Formula found! {acid_name} ─ ({acid_formula}) ─ Ka: {ka_value}. Now provide its concentration (in mole/L) for example: HA = :1.2e-2")
        HA_concentration = float(input('\t\t[HA]: '))

        ka_num = ka_value.split('×')[0]
        ka_num = float(ka_num)
        ka_power_sup = ka_value.split('×10')[1]

        superscript_map = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
        ka_power = ka_power_sup.translate(superscript_map)
        ka_power = float(ka_power)

        ka = ka_num * 10 ** ka_power

        # CALCULATION [H₃O⁺]

        a = 1
        b = ka
        c = -HA_concentration * ka

        D = b * b - 4 * a * c
        x = (-b + math.sqrt(D)) / (2 * a)
        if x > 0:
            pH = -math.log10(x)
            print(f'\n\t[H₃O⁺] = {x}\t\tpH = {pH}')
        else:
            print('Error occurred during calculations')

else:
    print("")
