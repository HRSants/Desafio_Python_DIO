
LIMITE_SAQUES = 3
saldo = 1500
extrato = ''
saques_realizados = 0

while True:
	print("""
=====MENU=====
[s] = saque
[d] = deposito
[e] = extrato
[f] = sair
=>""")
	opcao = str(input())

	if opcao == 's':
		print('Digite o valor do saque: ')
		qtd_saque = float(input())

		if (saldo < qtd_saque) or (qtd_saque > saldo):
			print('Saldo insuficiente!')
			continue

		elif qtd_saque <= 0:
			print('Digite um valor válido')
			qtd_saque = int(input())
			continue

		elif qtd_saque > 500:
			print('O valor nao pode ultrapassar R$500.00')
			continue

		elif saques_realizados >= LIMITE_SAQUES:
			print('Número máximo de saques atingidos')
			continue

		else:
			saldo -= qtd_saque
			saques_realizados += 1
			extrato += f'Saque: R${qtd_saque} | '
			print('Realizado com sucesso')
			continue

	if opcao == 'd':
		print('Digite o valor a ser depositado: ')
		qtd_deposito = int(input())

		if qtd_deposito <= 0:
			print('Digite um valor válido')
			qtd_deposito = int(input())

		else:
			saldo += qtd_deposito
			extrato += f'Deposito: R${qtd_deposito} | '
			print('Realizado com sucesso')
			continue

	if opcao == 'e':
		print(f"""
Saldo:R${saldo} 
Extrato => {extrato}
""")
		continue

	if opcao == 'sair':
		break

	else:
		print('Digite uma opcao valida')

