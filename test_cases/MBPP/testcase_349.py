from case_MBPP_349 import extract_quotation


def check(candidate):
    assert candidate('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    assert candidate('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    assert candidate('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
    assert candidate("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []

if __name__ == '__main__':
    check(extract_quotation)