medicos = [
    {
        "nome": "pedo",
        "cpf": "000000000-00",
        "rg": "1234567890",
        "crm": "CRM0000",
        "telefone": "(88) 9999-9999",
        "endereco": "Rua tal, 00, Bairro tal",
        "sexo": "Masculino",
        "senha": "1234"
    },
    {
        "nome": "palo",
        "cpf": "00000000001",
        "rg": "20210987654",
        "crm": "CRM1111",
        "telefone": "(88) 9999-9999",
        "endereco": "Rua tal, 10, Bairro tal",
        "sexo": "Masculino",
        "senha": "0909"
    }
]
pacis = [
    {
        "nome": "Mikael",
        "cpf": "1122334455",
        "rg": "436492955353",
        "telefone": "(21) 9999-0000",
        "endereco": "Rua tal, 20, Bairro h",
        "sexo": "Masculino",
        "convenio": "ConvenioX"
    },
    {
        "nome": "Maria",
        "cpf": "5475935384",
        "rg": "5347875453",
        "telefone": "(00) 8181-1212",
        "endereco": "Rua c, 30, Bairro j",
        "sexo": "Feminino",
        "convenio": "ConvenioY"
    }
]
convenios = [
    {
        "nome": "ConvenioX",
        "telefone": "(31) 77777-3333",
        "endereco": "Rua frederico, 40, Bairro y",
        "cnpj": "487547583487",
        "planos": "Plano x, Plano y"
    },
    {
        "nome": "ConvenioY",
        "telefone": "(12) 6666-6666",
        "endereco": "Rua n, 50, São Vicente",
        "cnpj": "45734865686",
        "planos": "Plano v, Plano t"
    }
]

agenda = [
    {   
        "medico": "Dr. Pedim",
        "paciente":"mikael sousa",
        "data" : "09/04/2007",
        "hora inicial" : "8:00",
        "hora final" : "10:00",
        "descrição" : "exame de vista"
    },
        {
            
        "medico": "Dr. Roberto",
        "paciente":"hiago",
        "data" : "01/10/2000",
        "hora inicial" : "6:00",
        "hora final" : "8:00",
        "descrição" : "consulta da clavicula"
    },
        {

        "medico": "Dr. Manel",
        "paciente":"Lucas",
        "data" : "11/04/2007",
        "hora inicial" : "13:00",
        "hora final" : "15:00",
        "descrição" : "exame de sangue"
    }
]

a = True
while a:
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")
   
   def cadastrarMedicos():
        
       print("Você quer se cadastar? (s/n)")
       rm=input("")
       if rm=="s":
        print("Informe seu nome: ")
        nomem=input("")
        print("Informe seu CPF: ")
        cpf= input("")
        print("Qual o RG do medico?")
        rg= input("")
        print("Informe seu CRM: ")
        crm= input("")
        print("Informe seu telefone: ")
        telef= input("")
        print("Informe seu endereço: ")
        ender= input("")
        print("Qual sua senha? ")
        senha= input("")
        print("Qual seu sexo? ")
        sexo=input("")
        print("Deseja salvar as informaçoes? (s/n)")
        input()
        print("Sucesso")
        medicos.append({"nome": nomem,
                "cpf": cpf,
                "rg": rg,
                "crm": crm,
                "telefone": telef,
                "endereco": ender,
                "sexo": sexo,
                "senha": senha})
        print(medicos)
       else:
          print("Programa cancelado!")
          breakpoint
        
   def cadastrarPacientes():
    
       print("Você quer cadastar um paciente? (s/n)")
       rp=input("")
       if rp=="s":
        print("Informe seu nome: ")
        nomep= input("")
        print("Informe seu endereço: ")
        endep= input("")
        print("Informe seu telefone(88 9999-9999): ")
        telep= input("")
        print("Informe seu CPF: ")
        cpfp= input("")
        print("Informe seu RG: ")
        rgp= input("")
        print("Qual seu sexo?(m/f)")
        sexop= input("")
        print("Qual seu convênio?")
        convep = input("")
        print("Deseja salvar as informaçoes?(s/n)")
        input()
        print("Sucesso!")
        pacis.append({
    
            "nome": nomep,
            "endereco": endep,
            "telefone": telep,
            "cpf": cpfp,
            "rg": rgp,
            "sexo": sexop,
            "convenio": convep
        })
 
        print(pacis)
       else:
          print("Programa cancelado!")
          breakpoint
       
   def cadastrarConvenios():
     
       print("Você quer cadastar um convênio? (s/n)")
       rc=input("")
       if rc=="s":
        print("Informe o nome do seu convênio: ")
        nomec= input("")
        print("Informe seu telefone para contato: ")
        telec= input("")
        print("Informe seu endereço: ")
        endec= input("")
        print("Informe O CNPJ do convênio")
        cpfc= input("")
        planos = input("")
        print("Deseja salvar as informações?")
        input()
        print("Sucesso")
        convenios.append({
    
            "nome": nomec,
            "endereco": endec,
            "telefone": telec,
            "planos": planos
        })
 
        print(convenios)
       else:
          print("Programa cancelado")
          breakpoint
   
   def buscarMedicos():
   
       print("Informe o nome ou o CRM do médico: ")
       busm = input("")
       resultados = [medico for medico in medicos if busm in medico['nome'] or busm in medico['crm']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
       else:
           print("Nenhum médico foi encontrado!")
   
   def buscarPacientes():
   
       print("Informe o nome ou o CPF do paciente: ")
       busp = input("")
       resuls = [paciente for paciente in pacis if busp in paciente['nome'] or busp in paciente['cpf']]
       if resuls:
           for resultado in resuls:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
       else:
           print("Nenhum paciente foi encontrado ")
   
   def buscarConvenios():
     
       print("Informe o nome ou o CNPJ do convênio: ")
       busc = input("")
       resultados = [convenio for convenio in convenios if busc in convenio['nome'] or busc in convenio['cnpj']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
       else:
           print("Nenhum convênio foi encontrado ")
   
   def alterarMedicos():
     
     print("Informe o CRM do médico que você deseja alterar: ")
     crm = input("")
     medico = next((medico for medico in medicos if medico['crm'] == crm), None)
     if medico:
           print(f"Dados atuais: {medico}")
           print("Informe os novos dados(deixe em branco para manter o valor atual): ")
           nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
           cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
           rg = input(f"RG ({medico['rg']}): ") or medico['rg']
           telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
           endereço = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
           sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
           senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
           medico.update({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereço,
            "sexo": sexo,
            "senha": senha
           })
           print("Os dados do médico foram atualizados!")
           print(medicos)
     else:
           print("Médico não foi encontrado!")
   
   def alterarPacientes():
   
       print("Informe o CPF do paciente que você deseja alterar: ")
       cpf = input("")
       paciente = next((paciente for paciente in pacis if paciente['cpf'] == cpf), None)
       if paciente:
           print(f"Dados atuais: {paciente}")
           print("Forneça os novos dados (deixe em branco para manter o valor atual):")
           nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
           rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
           telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
           endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
           sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
           convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
           paciente.update({
            "nome": nome,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
           })
           print("Dados do paciente foram atualizados!")
       else:
           print("Paciente não foi encontrado!")
   
   def marcarCompromisso():
     
     print("Você deseja marcar um compromisso?(s/n)")
     com=input("")
     if com=="s":
         print("Informe a data que você deseja(DD/MM/AAAA):")
         data=input("")
         print("Informe a hora que você deseja sua consulta(HH:MM - HH:MM): ")
         hi=input("")
         print("Informe a hora que você deseja finalizar sua consulta(HH:MM - HH:MM): ")
         hf=input("")
         print("Descreva o seu compromisso: ")
         desc=input("")
         print("Você deseja salvar essas informações?")
         rc=input("")
         print(f"Seu compromisso foi agendado, confira os dados: {agenda}")
     else:
         print("Programa Encerrado!")
         breakpoint
     
   def marcarConsulta():
       print("Você quer marcar uma consulta?(s/n)")
       mc = input("")
       if mc == "s":
           print("Informe o nome do médico: ")
           nm = input("")
           mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
           if mencontrado:
               print("Informe o nome do paciente: ")
               pnome = input("")
               pencontrado = next((paciente for paciente in pacis if paciente['nome'] == pnome), None)
               if pencontrado:
                   print("Informe a data da consulta(DD/MM/AAAA): ")
                   data = input("")
                   print("Informe a hora da consulta(HH:MM - HH:MM): ")
                   horario = input("")
                   print("A consulta foi marcada com sucesso! ")
                   agenda.append({
                       "data": data,
                       "horario": horario,
                       "medico": nm,
                       "paciente": pnome
                   })
               else:
                   print("O paciente não foi encontrado! ")
           else:
               print("Médico não foi encontrado!")
       else:
           print("Programa Cancelado! ")
   

   def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Médicos cadastrados: ")
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados: ")
        for paciente in pacis:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios: ")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['cnpj']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        print("Informe a data de início(DD/MM/AAAA): ")
        data_inicio = input("")
        data_fim = input("Informe a data de termino(DD/MM/AAAA): ")
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in agenda:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta.get('horario', consulta.get('hora inicial', ''))}-{consulta.get('hora final', '')}, Médico: {consulta.get('medico', '')}, Paciente: {consulta.get('paciente', '')}, Descrição: {consulta.get('descrição', '')}")
    else:
        print("Opção inválida!")

   match lang:
       case "1":
           cadastrarMedicos()
           
       case "2":
           cadastrarPacientes()

       case "3": 
           cadastrarConvenios()
           
       case "4":
           buscarMedicos()
           
       case "5":
           buscarPacientes()
           
       case "6":
           buscarConvenios()
         
       case "7":
           alterarMedicos()
           
       case "8":
           alterarPacientes()
           
       case "9":
           marcarCompromisso()
           
       case "10":
           marcarConsulta()
           
       case "11":
           emitirRelatorio()
                
       case "12":
           a = False
          
       case _:
           print("Escolha uma opção válida")
           lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")