from words import lista_palavras, cenas_forca
numero = int(input("Escolha um numero entre 0 e 49: "))
palavra = (lista_palavras[numero])
palavra_lista = ["_" for i in range(len(palavra))]
lista_indices = []
def find(palavra, letra):
    			indice = 0
    			while indice < len(palavra):
        			if palavra[indice] == letra:
            				lista_indices.append(indice)
        			indice = indice + 1


if numero>=0 and numero<=49:
	n_tentativas_incorretas = 0
	tentativas_incorretas = []
	letras_digitadas = []
	
	while n_tentativas_incorretas<6 and len(lista_indices)!=len(palavra):
		print("\n",cenas_forca[n_tentativas_incorretas])		
		print("Palavra: ", end="") #imprime a palavra
		for k in range(len(palavra)):
			if k < len(palavra)-1:
				if k in lista_indices:
					print(palavra[k]," ",end="")
				else:
					print("_"," ",end="")
			else:			
				if k in lista_indices:
					print(palavra[k])
				else:
					print("_")
		print(end="\n")		
		
		
		
		if n_tentativas_incorretas > 0: #copia as letras incorretas digitadas
			print("Tentativa(s) incorreta(s):", end="")
			for i in tentativas_incorretas:
				print ("", i,end="")
			print(end="\n")	

		letra =  input("Proxima letra: ")

							
		if letra in letras_digitadas:  #caso repita a letra
			print("Voce jah escolheu esta letra.")
			letras_digitadas.append(letra)
			
		elif letra not in palavra: #caso erre a letra
			n_tentativas_incorretas+=1
			letras_digitadas.append(letra)
			tentativas_incorretas.append(letra)
				
		else: #caso acerte a letra
			letras_digitadas.append(letra)
			find(palavra, letra)
			
	
	print("\n",cenas_forca[n_tentativas_incorretas],)
	print("Palavra: ", end="") #imprime a palavra
	for k in range(len(palavra)):
		if k < len(palavra)-1:
			if k in lista_indices:
				print(palavra[k]," ",end="")
			else:
				print("_"," ",end="")
		else:			
			if k in lista_indices:
				print(palavra[k])
			else:
				print("_")
		
	print(end="\n")	
	print("Tentativa(s) incorreta(s):",end="")
	for i in tentativas_incorretas:
		print (" "+ i, end='')
	print(end="\n")
	
	if len(lista_indices)==len(palavra):
		print("Palavra encontrada!")
	else:
		print("Palavra oculta:",palavra)			
		
		
else:
	print("Numero invalido.")
