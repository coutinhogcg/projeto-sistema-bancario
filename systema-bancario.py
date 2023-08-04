#declaração de variaveis
saldo = 1000
y = 3
x = 0
saqueextrato = 0
depositoextrato = 0

#loop para o codigo para somente quano usuario quiser
while True:
    
    #menu para mostrar as opções ao usuario
    menu = ''' --------------------------
                    menu

            [d] depositar
            [s] sacar
            [e] extrato
            [q] sair
          --------------------------- 
          '''
    print (menu)

    #pegando a opção escolida pelo usuario
    opção = input ("")
    
   
    #condição caso usuario escolha depositar        
    if opção == "d":
       valordeposito = float (input("digite o valor que deseja depositar: ")) 
       #condição paar evitar a tentativa de um deposito negativo       
       if valordeposito < 1:
           print ("você não pode depositar um valor negativo ou igual a 0")    
        
       #condição de deposito bem sucedido
       else:
           print ("deposito efetuado")
           saldo = saldo + valordeposito
           print ("saldo atual: R$",saldo)
           depositoextrato += 1
    
    
  
    
             
    #laço de repetição para bloquear o usuario a fazer somente 3 saques por "dia"
    while opção == "s":
            
            #contador para o if que fecha o while
            x += 1
            
            #if que trava o while quando exede o limite diario de saques
            if x >= 4:
                print("você excedeu seu limite de saques diarios")
                break
            
            
            if opção == "s":
                valorsacar = float (input ("digite o valor que deseja sacar: "))
                #if para evitar do usuario sacar mais dinheiro do que possui na sua conta
                if valorsacar > saldo :
                    print ("você não pode sacar um valor maior que seu saldo tente denovo")
                   
               #if para evitar que o usuario faça saques de mais que R$500 de uma vez
                elif valorsacar >=500.1:
                    print ("você não pode sacar mais de R$500 so em um saque")
                #caso não tenha problema com o valor inserido esse if continua a operação
                elif valorsacar<saldo:
                    print ("saque realisado")
                    saldo= saldo - valorsacar
                    print ("saldo atual: R$",saldo)
                    y=y-1
                    print ("você so pode fazer mais ",y," saques hoje")
                    opção = "a"
                    saqueextrato +=1
                    
    #if que condicio o extrato
    if opção == "e":
          extrato = "extrato"
          print (extrato.center(46, "=")) 
          print ("quantidade de depositos efetuados: ",depositoextrato)
          print ("quantidade de saques efetuados   : ",saqueextrato)
          print ("saldo atual                      :R$",saldo)
    #if que condiciona o encerramento do programa
    if opção == "q":
        break