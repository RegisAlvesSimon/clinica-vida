# Clínica Vida+ — Sistema de Cadastro de Pacientes

Sistema em Python, executado no terminal, para cadastrar e consultar os pacientes de uma clínica. Projeto desenvolvido para o Projeto Integrado Inovação do curso de Análise e Desenvolvimento de Sistemas da Anhanguera.

## Funcionalidades

- **Cadastrar paciente** com nome, idade e telefone
- **Buscar paciente** pelo nome completo ou por parte do nome
- **Listar pacientes** em tabela, em ordem alfabética
- **Ver estatísticas**: total de pacientes, idade média, paciente mais novo e mais velho
- **Dados salvos em arquivo** (`pacientes.json`), mantidos entre uma execução e outra

### Validações

- Nome obrigatório e sem duplicidade (não diferencia maiúsculas e minúsculas)
- Idade numérica entre 1 e 150 anos
- Telefone com DDD (10 ou 11 dígitos), aceito com ou sem parênteses, espaço e hífen, e exibido no formato `(18) 99999-9999`

## Como executar

Requisito: Python 3.8 ou superior (não usa bibliotecas externas).

```bash
python clinica_vida.py
```

## Exemplo de uso

```
==================================================
SISTEMA CLÍNICA VIDA
==================================================
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Sair
==================================================
Escolha uma opção (1-5): 4

--- LISTA DE PACIENTES ---
Nome                      Idade    Telefone
--------------------------------------------------
Ana Paula                 30       (18) 99999-1234
João Silva                45       (18) 3222-1111
```

## Conceitos aplicados

- Organização do código em funções com responsabilidade única
- Listas e dicionários para estruturar os dados
- Tratamento de erros com `try/except`
- List comprehension, `lambda`, `min`, `max` e `sorted`
- Leitura e escrita de arquivos JSON
- Formatação de saída com f-strings

## Autor

**Reginaldo Alves Simon** — estudante de Análise e Desenvolvimento de Sistemas
[LinkedIn](https://www.linkedin.com/in/reginaldo-alves-simon)
