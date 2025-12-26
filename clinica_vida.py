# Sistema de Gestão da Clínica Vida

pacientes = []

def cadastrar_paciente():
    """Função para cadastrar um novo paciente"""
    print("\n--- CADASTRAR PACIENTE ---")
    try:
        nome = input("Nome do paciente: ").strip()
        if not nome:
            print("Erro: Nome não pode ser vazio!")
            return
        
        idade = int(input("Idade: "))
        if idade <= 0 or idade > 150:
            print("Erro: Idade deve estar entre 1 e 150 anos!")
            return
        
        telefone = input("Telefone: ").strip()
        if not telefone:
            print("Erro: Telefone não pode ser vazio!")
            return
        
        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }
        
        pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")
    
    except ValueError:
        print("Erro: Entrada inválida! Verifique os dados.")

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
    """Função para buscar um paciente pelo nome"""
    print("\n--- BUSCAR PACIENTE ---")
    nome = input("Nome do paciente: ").strip()
    
    encontrados = [p for p in pacientes if p["nome"].lower() == nome.lower()]
    
    if encontrados:
        print(f"Paciente encontrado:")
        for p in encontrados:
            print(f"  Nome: {p['nome']}")
            print(f"  Idade: {p['idade']}")
            print(f"  Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado!")

def listar_pacientes():
    """Função para listar todos os pacientes"""
    print("\n--- LISTA DE PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado!")
        return
    
    print(f"{'Nome':<20} {'Idade':<8} {'Telefone':<15}")
    print("-" * 45)
    for p in pacientes:
        print(f"{p['nome']:<20} {p['idade']:<8} {p['telefone']:<15}")

def menu_principal():
    """Função para exibir o menu principal"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA CLÍNICA VIDA")
        print("="*50)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("="*50)
        
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
