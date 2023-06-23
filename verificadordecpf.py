import re # Importei re que serve
import sys # Importei o sys
import os # Importei o os 

def validarCPF(): # Crie uma função.
    try: # Se não de eros ele vai exibir isso. 
        entrada = input('CPF [746.824.890-70]: ') # pegando a informação do usuario.
        cpf = re.sub(r'[^0-9]','',entrada) # 

        entrada_e_sequencial = entrada == entrada[0] * len(entrada)

        if entrada_e_sequencial:
            print('Você enviou dados sequenciais.')
            sys.exit()

        nove_digitos = cpf [:9]
        contador_regressivo_1 = 10

        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
        os.system('CLS')
        if cpf == cpf_gerado_pelo_calculo:
            print(f'{cpf} é válido')
        else:
            print('CPF inválido')
       
    except:
        print('É permitido apenas numeors!')
 
    validarCPF() # Chamei a função para inicia que der o resultado.
validarCPF() # Chamei novamente para iniciar o looping.
