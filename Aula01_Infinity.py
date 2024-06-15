nome = input("Digite seu primeiro nome.: ")
filhos = int(input("Quantos filhos você tem.: "))
mensalidade = float(input("Qual o valor da mensalidade.: "))
vlr_total_mes = (mensalidade*filhos)
opniao = input("Você teria interesse em algum dos nossos curso? (sim/não).: ")
resposta_opniao = opniao == "sim"
print(f"Saudações Sr(a) {nome}, de acordo com a quantidade de filhos: {filhos}, o valor total da mensalidade seria: R$ {vlr_total_mes}. Agradecemos sua opnião {resposta_opniao} sobre conhecer nossos cursos.")
