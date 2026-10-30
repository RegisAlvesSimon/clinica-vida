# Sistema de Gestão da Clínica Vida
# Cadastro, busca, listagem e estatísticas de pacientes,
# com os dados salvos em arquivo JSON.

import json
import os

ARQUIVO_DADOS = "pacientes.json"

pacientes = []


def carregar_pacientes():
    """Carrega os pacientes salvos no arquivo JSON, se ele existir"""
    global pacientes
    if not os.path.exists(ARQUIVO_DADOS):
        pacientes = []
        return
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            pacientes = json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        print("Aviso: não foi possível ler o arquivo de dados. Iniciando lista vazia.")
        pacientes = []


def salvar_pacientes():
    """Salva a lista de pacientes no arquivo JSON"""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(pacientes, arquivo, ensure_ascii=False, indent=2)
    except OSError:
        print("Erro: não foi possível salvar os dados!")


def validar_telefone(telefone):
    """Retorna o telefone só com números se for válido (10 ou 11 dígitos com DDD)"""
    numeros = "".join(c for c in telefone if c.isdigit())
    if len(numeros) in (10, 11):
        return numeros
    return None


def formatar_telefone(numeros):
    """Formata o telefone como (DD) 99999-9999 ou (DD) 9999-9999"""
    if len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"


def paciente_ja_cadastrado(nome):
    """Verifica se já existe um paciente com o mesmo nome"""
    return any(p["nome"].lower() == nome.lower() for p in pacientes)


def cadastrar_paciente():
    """Função para cadastrar um novo paciente"""
    print("\n--- CADASTRAR PACIENTE ---")
    try:
        nome = input("Nome do paciente: ").strip()
        if not nome:
            print("Erro: Nome não pode ser vazio!")
            return
        if paciente_ja_cadastrado(nome):
            print(f"Erro: o paciente {nome} já está cadastrado!")
            return

        idade = int(input("Idade: "))
        if idade <= 0 or idade > 150:
            print("Erro: Idade deve estar entre 1 e 150 anos!")
            return

        telefone = validar_telefone(input("Telefone com DDD: ").strip())
        if not telefone:
            print("Erro: Telefone inválido! Use o DDD + número, ex.: (18) 99999-9999")
            return

        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }

        pacientes.append(paciente)
        salvar_pacientes()
        print(f"Paciente {nome} cadastrado com sucesso!")

    except ValueError:
        print("Erro: Idade deve ser um número inteiro!")


def ver_estatisticas():
    """Função para exibir estatísticas dos pacientes"""
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    if not pacientes:
        print("Nenhum paciente cadastrado!")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    idade_media = sum(idades) / total
    paciente_novo = min(pacientes, key=lambda p: p["idade"])
    paciente_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {idade_media:.1f} anos")
    print(f"Paciente mais novo: {paciente_novo['nome']} ({paciente_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_velho['nome']} ({paciente_velho['idade']} anos)")


def buscar_paciente():
    """Função para buscar pacientes por nome completo ou parte do nome"""
    print("\n--- BUSCAR PACIENTE ---")
    termo = input("Nome ou parte do nome: ").strip()
    if not termo:
        print("Erro: digite pelo menos uma letra para buscar!")
        return

    encontrados = [p for p in pacientes if termo.lower() in p["nome"].lower()]

    if encontrados:
        print(f"{len(encontrados)} paciente(s) encontrado(s):")
        for p in encontrados:
            print(f"  Nome: {p['nome']}")
            print(f"  Idade: {p['idade']}")
            print(f"  Telefone: {formatar_telefone(p['telefone'])}")
            print()
    else:
        print("Paciente não encontrado!")


def listar_pacientes():
    """Função para listar todos os pacientes em ordem alfabética"""
    print("\n--- LISTA DE PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado!")
        return

    print(f"{'Nome':<25} {'Idade':<8} {'Telefone':<16}")
    print("-" * 50)
    for p in sorted(pacientes, key=lambda p: p["nome"].lower()):
        print(f"{p['nome']:<25} {p['idade']:<8} {formatar_telefone(p['telefone']):<16}")


def menu_principal():
    """Função para exibir o menu principal"""
    carregar_pacientes()
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA CLÍNICA VIDA")
        print("=" * 50)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("\nEncerrando sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
