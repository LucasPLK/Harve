import json

# Dicionáro com informações dos Estados
estados_dict = {
        "AC" :  {
                "nome": "Acre",
                "capital": "Rio Branco",
				"populacao":  364756 },
        "AL" :  {
                "nome": "Alagoas",
                "capital": "Maceió",
				"populacao":  957916},
        "AP" :  {
                "nome": "Amapá",
                "capital": "Macapá",
				"populacao":  442933},
        "AM" :  {
                "nome": "Amazonas",
                "capital": "Manaus",
				"populacao":  2063547},
        "BA" :  {
                "nome": "Bahia",
                "capital": "Salvador",
				"populacao":  2417678},
        "CE" :  {
                "nome": "Ceará",
                "capital": "Fortaleza",
				"populacao":  2428708},
        "ES" :  {
                "nome": "Espírito Santo",
                "capital": "Vitória",
				"populacao":  322869},
        "GO" :  {
                "nome": "Goiás",
                "capital": "Goiânia",
				"populacao":  1437237},
        "MA" :  {
                "nome": "Maranhão",
                "capital": "São Luíz",
				"populacao":  1037775},
        "MT" :  {
                "nome": "Mato Grosso",
                "capital": "Cuiabá",
				"populacao":  650912},
        "MS" :  {
                "nome": "Mato Grosso do Sul",
                "capital": "Campo Grande",
				"populacao":  897938},
        "MG" :  {
                "nome": "Minas Gerais",
                "capital": "Belo Horizonte",
				"populacao":  2315560},
        "PA" :  {
                "nome": "Pará",
                "capital": "Belém",
				"populacao":  2428708},
        "PB" :  {
                "nome": "Paraíba",
                "capital": "João Pessoa",
				"populacao":  833932},
        "PR" :  {
                "nome": "Paraná",
                "capital": "Curitiba",
				"populacao":  1773733},
        "PE" :  {
                "nome": "Pernambuco",
                "capital": "Recife",
				"populacao":  1488920},
        "PI" :  {
                "nome": "Piauí",
                "capital": "Teresina",
				"populacao":  866300},
        "RJ" :  {
                "nome": "Rio de Janeiro",
                "capital": "Rio de Janeiro",
				"populacao":  6211423},
        "RN" :  {
                "nome": "Rio Grande do Norte",
                "capital": "Natal",
				"populacao":  751300},
        "RS" :  {
                "nome": "Rio Grande do Sul",
                "capital": "Porto Alegre",
				"populacao":  1332833},
        "RO" :  {
                "nome": "Rondônia",
                "capital": "Porto Velho",
				"populacao":  460413},
        "RR" :  {
                "nome": "Roraima",
                "capital": "Boa Vista",
				"populacao":  413486},
        "SC" :  {
                "nome": "Santa Catarina",
                "capital": "Florianópolis",
				"populacao":  537213},
        "SP" :  {
                "nome": "São Paulo",
                "capital": "São Paulo",
				"populacao":  11451245},
        "SE" :  {
                "nome": "Sergipe",
                "capital": "Aracajú",
				"populacao":  602757},
        "TO" :  {
                "nome": "Tocantins",
                "capital": "Palmas",
				"populacao":  302692},
        "DF" :  {
                "nome": "Distrito Federal",
                "capital": "Brasília",
				"populacao":  2817068},
}

# variável de controle do loop
continuar = 'sim'

while continuar == "sim":
    # captura da sigla do Estado para busca nas chaves do dicionário
    # .upper() transforma toda a string em caixa alta, de forma que se alguem digitar "pr", o resultado será "PR"
    # .strip() remove os espaços antes e depois da string
    sigla = input("Digite a Sigla do Estado que deseja informações: ").upper().strip()

    # verifico se a sigla digitada está presente no dicionário
    if sigla not in estados_dict.keys():
        # caso a sigla não exista nas chaves do dicioário, pedimos para o usuário digitarnovamente uma sigla válida
        print("Sigla inválida para estados Brasileiros. Digite uma das siglas da lista abaixo:\n", estados_dict.keys(), end='\n\n')
        # continue faz com que todo o restante do loop seja pulado e o c´odigo colta para a linha de verificação da condição do while
        continue

    # pergunta qual a informação sobre a sigla o usuário deseja saber
    # .lower() transforma toda a estring em caixa baixa, ou seja, se  usuário digitar "NoMe", a string será transformada em "nome"
    informacao = input("Qual informação você deseja (nome/populacao/ambas)? ").lower().strip()
    
    # se o usuário pediu para ver amnas as informações entro no "if"
    if informacao == 'ambas':
        #json.dumps(<variável>, indent=3) formata o dicionário para o print
        print(json.dumps(estados_dict[sigla], indent=3), end='\n\n')
    elif informacao in list(estados_dict[sigla].keys()):
        # se a informação requisitada é válida, então apresento ela para o usuário
        print(informacao, ":", estados_dict[sigla][informacao], end='\n\n')
    else:
        # se a informação desejada não é encontrada no dicionário, voltamos para o começo do loop
        print("informação desejada não encontrada.\nDigite uma das opções a seguir: (nome/populacao/ambas)", end='\n\n')
        continue
    continuar = input("Deseja continuar (sim/não)? ")