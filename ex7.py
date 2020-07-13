hora_ini = int(input("Informe a Hora atual: "))
min_ini = int(input("Informe o minuto atual: "))
print("\nLeia o texto a seguir:")
print("""\nMr. Bennet foi uma das primeiras pessoas que visitaram Mr. Bingley. 
Sempre fora esta a sua intenção, embora continuasse a assegurar até o fim à sua
 esposa que não iria de forma alguma; nada lhe disse até à noite do dia em que
  fez a visita. Só aí ele o revelou, da seguinte maneira: vendo a sua segunda 
  filha ocupada em reformar um chapéu, dirigiu-lhe de súbito estas palavras:
— Espero que Mr. Bingley goste do chapéu, Lizzy.
— Não temos nenhum modo de saber as preferências de Mr. Bingley já que não
 podemos visitá-lo — interveio a mãe, ressentida.
— Mas você se esquece, mamãe — disse Elizabeth —, de que nós o encontraremos em
 reuniões e que Mrs. Long nos prometeu apresentá-lo.
— Não creio que Mrs. Long faça tal coisa. Ela tem duas sobrinhas e é uma mulher
 egoísta e hipócrita. A minha opinião sobre ela não é boa.
— Nem a minha tampouco — disse Mr. Bennet.
— Alegra-me saber que você não depende dos serviços dela.
Mrs. Bennet não se dignou responder. Incapaz de dominar-se por mais tempo, 
entretanto, pôs-se a ralhar com uma das filhas:
— Não tussa desse modo, pelo amor de Deus, Kitty . Tenha um pouco de piedade dos
 meus nervos... Você está dilacerando-os!
— Kitty não sabe tossir discretamente — disse o pai.
— Não tem noção do momento oportuno.
— Não tusso para distrair-me — respondeu Kitty, irritada. — Quando será o nosso
 próximo baile, Lizzy?
— De amanhã a 15 dias.
— É verdade — gritou a mãe. — E Mrs. Long só estará de volta na véspera desse
 dia. Logo, ser-lhe-á impossível fazer a apresentação do estranho, pois ela
  tampouco o terá conhecido.
— Portanto, minha cara, você poderá adiantar-se à sua amiga e apresentar 
Mr. Bingley a ela.
— Impossível, Mr. Bennet, impossível! Se eu não tenho relações com ele! Como
 pode você ser tão provocante?
— Respeito a sua discrição. Quinze dias de conhecimento decerto não são
 suficientes. Não se pode conhecer realmente um homem em tão curto espaço de
  tempo. Mas se não arriscarmos, outra pessoa o fará. E afinal de contas,
   Mrs. Long e as suas sobrinhas devem ter também a sua oportunidade. E como lhe
    será fácil pensar que é um ato de caridade da sua parte recusar tal
     incumbência, eu assumirei a responsabilidade.
As meninas olharam fixamente para o pai. Mrs. Bennet disse apenas:
— Tolice, tolice.
""")
hora_fim = int(input("Informe a Hora atual, após a leitura: "))
min_fim = int(input("Informe o minuto atual, após a leitura: "))
min_total = (hora_fim*60+min_fim) - (hora_ini*60+min_ini)
seg_total = min_total * 60
seg_palavra = seg_total/382
seg_nec_total = seg_palavra * 90000
seg_nec_diario = seg_nec_total / 30
hora_nec_diario = seg_nec_diario // 3600
min_nec_diario = (seg_nec_diario % 3600) // 60
print("Seu tempo de leitura é de, aproximadamente, %.1f" %seg_palavra,"seg(s) por palavra.")
print("Para a leitura de um livro adulto em 1 mês seria necessária uma dedicação diária de",int(hora_nec_diario),"horas e",int(min_nec_diario),"minutos")