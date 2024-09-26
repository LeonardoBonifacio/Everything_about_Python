import os


class No:

    def __init__(self, chave, titulo, nota):
        self.chave = chave
        self.titulo = titulo
        self.nota = nota
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_no_final(self, chave, titulo, nota):
        novo_no = No(chave, titulo, nota)
        if not self.inicio:
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no

    def adicionar_no_inicio(self, chave, titulo, nota):
        novo_no = No(chave, titulo, nota)
        if not self.inicio:
            self.inicio = self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

    def inserir_apos(self, chave_existente, chave, titulo, nota):
        atual = self.inicio
        while atual:
            if atual.chave == chave_existente:
                novo_no = No(chave, titulo, nota)
                novo_no.anterior = atual
                novo_no.proximo = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = novo_no
                atual.proximo = novo_no
                if atual == self.fim:
                    self.fim = novo_no
                return True
            atual = atual.proximo
        return False

    def deletar(self, chave):
        atual = self.inicio
        while atual:
            if atual.chave == chave:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                if atual == self.inicio:
                    self.inicio = atual.proximo
                if atual == self.fim:
                    self.fim = atual.anterior
                return True
            atual = atual.proximo
        return False

    def exibir_para_frente(self):
        atual = self.inicio
        while atual:
            print(f"Chave: {atual.chave}, Título: {atual.titulo}, Nota: {atual.nota}")
            atual = atual.proximo
        input('[ENTER] para continuar...')

    def exibir_para_tras(self):
        atual = self.fim
        while atual:
            print(f"Chave: {atual.chave}, Título: {atual.titulo}, Nota: {atual.nota}")
            atual = atual.anterior
        input('[ENTER] para continuar...')

    def trocar_elementos(self, chave1, chave2):
        if chave1 == chave2:
            return False  # Não há necessidade de trocar se as chaves forem iguais
        
        no1 = no2 = None
        atual = self.inicio
        
        while atual:
            if atual.chave == chave1:
                no1 = atual
            if atual.chave == chave2:
                no2 = atual
            atual = atual.proximo
        
        if not no1 or not no2:
            return False  # Pelo menos uma das chaves não foi encontrada

        # Troca de nós
        if no1.anterior:
            no1.anterior.proximo = no2
        if no1.proximo:
            no1.proximo.anterior = no2

        if no2.anterior:
            no2.anterior.proximo = no1
        if no2.proximo:
            no2.proximo.anterior = no1

        no1.anterior, no2.anterior = no2.anterior, no1.anterior
        no1.proximo, no2.proximo = no2.proximo, no1.proximo

        # Ajusta o inicio e fim da lista se necessário
        if no1 == self.inicio:
            self.inicio = no2
        elif no2 == self.inicio:
            self.inicio = no1

        if no1 == self.fim:
            self.fim = no2
        elif no2 == self.fim:
            self.fim = no1

        return True
    
    def ordenar_por_chave(self):
        # Bubble sort
        if not self.inicio or not self.inicio.proximo:
            return
        trocado = True
        while trocado:
            trocado = False
            atual = self.inicio
            while atual.proximo:
                if atual.chave > atual.proximo.chave:
                    # Troca os valores
                    atual.chave, atual.proximo.chave = atual.proximo.chave, atual.chave
                    atual.titulo, atual.proximo.titulo = atual.proximo.titulo, atual.titulo
                    atual.nota, atual.proximo.nota = atual.proximo.nota, atual.nota
                    trocado = True
                atual = atual.proximo
            
        input('Ordenação concluída! [ENTER]')


def menu():
    lista = ListaDuplamenteEncadeada()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenu:")
        print("1. Adicionar no final")
        print("2. Adicionar no início")
        print("3. Inserir após chave existente")
        print("4. Deletar por chave")
        print("5. Exibir lista para frente")
        print("6. Exibir lista para trás")
        print("7. Trocar dois elementos")
        print("8. Ordenar elementos")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            chave = int(input("Digite a chave: "))
            titulo = input("Digite o título: ")
            nota = input("Digite a nota: ")
            lista.adicionar_no_final(chave, titulo, nota)     
        
        elif escolha == '2':
            chave = int(input("Digite a chave: "))
            titulo = input("Digite o título: ")
            nota = input("Digite a nota: ")
            lista.adicionar_no_inicio(chave, titulo, nota)      
        
        elif escolha == '3':
            chave_existente = int(input("Digite a chave existente após a qual deseja inserir: "))
            chave = int(input("Digite a nova chave: "))
            titulo = input("Digite o novo título: ")
            nota = input("Digite a nova nota: ")
            if lista.inserir_apos(chave_existente, chave, titulo, nota):
                print("Nó inserido com sucesso.")
            
            else:
                print("Chave existente não encontrada.")      
        
        elif escolha == '4':
            chave = int(input("Digite a chave para deletar: "))
            
            if lista.deletar(chave):
                print("Nó deletado com sucesso.")
            
            else:
                print("Chave não encontrada.")
        
        elif escolha == '5':
            print("Exibindo a lista para frente:")
            lista.exibir_para_frente()   
        
        elif escolha == '6':
            print("Exibindo a lista para trás:")
            lista.exibir_para_tras()       
        
        elif escolha == '7':
            chave1 = int(input("Digite a chave do primeiro nó: "))
            chave2 = int(input("Digite a chave do segundo nó: "))
            if lista.trocar_elementos(chave1, chave2):
                print("Nós trocados com sucesso.")
            else:
                print("Erro na troca. Verifique se as chaves existem.")    
        
        elif escolha == '8':
            lista.ordenar_por_chave()    
        
        elif escolha == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
