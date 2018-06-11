Abstract

	In this paper we are interested in the context of live video streaming in
	mobile networks. Our goal is to realize an quantitative and qualitative analysis
	with the intent to better understand some aspects of data transmission. For
	such we analyzed some methods of package transmission of live video stream
	in this networks. We performed simulations to achieve a comparison between
	this methods to classify them about their qualities and scalability. We performed
	comparisons between the protocols TCP, UDP and the transmission technique
	DASH, those simulations were made on OMNeT++ and INET Framework.

Introdução

	Esse trabalho está dentro do projeto de iniciação científica orientado pelo profes-
	sor Alfredo Goldman e que compõem o projeto INCT da Internet do Futuro para
	Cidades Inteligentes : Improving fog computing techniques to allow a better quality
	of experience in vehicular networks, coordenado pelo professor Edmundo Roberto
	Mauro Madeira (UNICAMP), com participação do profeessor Luiz Fernando Bit-
	tencourt (UNICAMP) e o aluno Diogo Machado Gonçalves (M.Sc., UNICAMP).
	Nesse mesmo projeto trabalha comigo o aluno de graduação Patrick Abrahão (IME
	-USP).
	Desejamos estudar a transmissão de dados em tempo real em redes veiculares e a
	nossa motivação foi o cenário de veículos autônomos e o crescimento da populari-
	zação da transmissão de vídeo ao vivo em redes sociais, serviços de entretenimento
	e outros. Redes veiculares tem apresentado atualmente vantagens como controle
	eficiente de tráfego, maior segurança e possibilidade de desenvolvimento de novos
	recursos. Esse é um ambiente composto por uma estrutura capaz de fornecer dados
	para veículos que trafegam em uma determinada área, e outra estrutura que confi-
	gura o conjunto de veículos que utilizarão o serviço.
	Dada a complexidade de trabalhar com esse ambiente, em um primeiro momento,
	reduzimos nosso cenário de estudo para transmissão de vídeo ao vivo em uma rede
	AD-HOC, que é composta por dispositivos móveis que não necessitam de uma infra-
	estrutura de rede por trás e possuem movimentação, tendo assim cenários dinâmi-
	cos.
	Vamos fazer comparações entre dois protocolos de transmissão, TCP e UDP, e o
	DASH, uma técnica aplicada no primeiro deles que permite a mudança da quali-
	dade da transmissão de vídeo de acordo com a qualidade da rede. Utilizaremos o
	simulador de redes OMNeT++ com a extensão INET Framework que nos possibilita
	trabalhar também com cenários móveis e redes wireless. A partir dessas simulações
	faremos análises comparativas entre os protocolos e a técnica apresentada.

Objetivos

	O objetivo do trabalho é estudar pontos de qualidade de serviço e de experiência do
	usuário para a transmissão de vídeo em tempo real em redes AD-HOC. Vamos fazer
	comparações entre os protocolos de transmissão, TCP e UDP, e a técnica DASH.
	Para tal estudaremos conceitos de redes como infra-estrutura, o que é uma rede
	móvel e veicular, seus protocolos e técnicas de transmissão de dados.
	Estudaremos os tipos de cenários nesse contexto e as metodologias de análises utili-
	zadas. Vamos desenvolver nossos próprios cenários e os implementaremos utilizando
	o simulador de redes OMNeT++ com a extensão INET Framework e tentaremos
	integrar essas simulações com o SUMO, um simulador de mobilidade urbana. A
	partir dessas simulações vamos analisar deformação e perda de pacotes, o delay na
	entrega deles e seu comportamento multi-hop para então quiçá apontar quais dessas
	técnicas ou protocolos podem ser melhores em determinados cenários.

Etapas já desenvolvidas

	Iniciamos esse trabalho em Julho de 2017 e muito da proposta que foi apresentada
	na seção objetivos tem sido lapidada desde então. Já passamos, parcialmente, pelas
	três etapas descritas, estudando e moldando o problema, escolhendo ferramentas
	para trabalharmos e nos adequando a elas. Além de ler vários trabalhos relaciona-
	dos, temos desde então nos adequado com o simulador escolhido, desenvolvendo aos
	poucos nossas aplicações. Atualmente já desenvolvemos e implementamos um dos
	primeiros cenários cotados pelo grupo e estamos trabalhando na parte de coleta de
	dados para fazermos as primeiras análises.


Acompanhamento do desenvolvimento :

As tarefas descritas a seguir darão continuidade as etapas desenvolvidas descritas.
Seguem ,por semana, as atividades efetuadas a partir do dia 19/03 (data da inclusão oficial da disciplina) :

	- Semana do 19/03 : 
		Revisão e conclusão das análises dos dados obtidos. Finalização do primeiro artigo
		do projeto e submissão na trilha WTG da 
		SBRC2018 ( http://www.sbrc2018.ufscar.br/ ).

	- Semana do 26/03 : 
		Revisão geral do trabalho feito até então e levantamento das próximas tarefas. 
		Junto com a disciplina MAC0470 foi criado um subprojeto, para submeter o cenário
		concluído até a etapa	anterior no repositório oficial da extensão do simulador, 
		INET Framework ( https://inet.omnetpp.org/ ), colaborando com a comunidade 
		que o utiliza.

	- Semana do 02/04 : 
		Por motivo de problemas pessoais, não trabalhei no projeto nessa semana.

	- Semana do 09/04 :
		Revisão e correções seguindo os apontamento do feedback da submissão para a trilha
		WTG da SBRC2018. O artigo foi aceito :D !! Resultado divulgado 10/04.

	- Semana do 16/04 :
		Foi marcada uma pré-apresentação do nosso trabalho para o grupo de sistemas 
		para o dia 23/04 para que possamos melhor nos preparar para o Congresso.
		Nessa semana foquei em rever toda a fundamentação do trabalho, os conceitos 
		e bibliografias principais para estar preparado para possíveis questionamentos 
		e para melhor preparar a apresentação.

	- Semana do 23/04:
		Nessa semana eu apresentei, junto ao meu grupo, nosso projeto do WTG do SBRC2018.
		A apresentação foi feita para o grupo de sistemas do IME e tivemos ótimos
		feedbacks. Assim sendo agora estamos trabalhando nas possíveis correções 
		para a apresentação oficial que será no dia 6 de Maio no SBRC.

	- Semana do 30/04:
		Fizemos as correções apontadas na nossa apresentação para o grupo de sistemas do IME.
		No dia 06/05 fomos para a SBRC2018 em Campos do Jordão para então apresentar nosso
		artigo. A apresentação foi ótima, tivemos muitas perguntas e comentários construtivos
		e acreditamos que nos saímos bem.
		A partir de agora, vamos nos reunir com nosso orientador para programar as próximas
		etapas.
		Também fiz um pull request para o repositório do INET Framework com a nossa 
		implementação da transmissão de vídeo ao vivo via TCP e via DASH, e com nosso cenário 
		experimental. Para que os dois primeiros fossem acrescentados aos módulos de 
		TCP->Wireless e o cenário experimntal para os exemplos disponíveis.

	- De 6 a 7 de Maio : Participação no SBRC2018 em Campos do Jordão. 
		![SBRC2018 Campos do Jordão](https://github.com/andersonandrei/VehicularNetworksIC/blob/master/SBRC2018/1.jpg)

	- Semana do 07/05 :
		Durante nossa apresentação no SBRC2018 tivemos muitas perguntas construtivas e algumas 	
		recomendações muito interessantes. Assim, nessa semana, agrupamos toda a informação 
		obtida no Simpósio e fizemos nossa devolutiva para nosso orientador.

	- Semana do 14/05 :
		Durante essa semana, remontamos nosso plano de trabalho, partindo agora para o estudo
		 da parte específica de redes veiculares, assim como as ferramentas que usaremos a 
		 partir de então. São elas o Veins e o Sumo Simulator que são módulos do OMNeT++ 
		 e que interagem com o INET Framework, que temos utilizado.

	- Semana do 21/05 :
		Verifiquei que está para ser lançada uma nova versão do INET Framework e decidimos
		versar nosso projeto para tal atualização.
		Também apontaram no meu pull request que seria mais fácil de acrescentar o projeto 
		ao repositório em si, se eu o atualiza-se o para essa nova versão.
		A partir da branch "integration" do repositório deles do GitHub obtive tal versão 
		em desenvolvimento para então adequar nossa implementação de transmissão de 
		vídeo ao vivo via TCP e via DASH, assim como nosso cenário experimental.

	- Semana do 28/05 :
		Ainda estou trabalhando na atualização do nosso cenário para a nova versão do 
		INET Framework. Alguns módulos de transmissão de pacotes foram refatorados, e 
		uma nova camada de validação da integridade dos pacotes foi acrescentada, assim, 
		estou com dificuldades para efetuar a atualização.
		Mesmo assim, atualizei minhas modificações no meu pull request para o repositório 
		e pedi orientações para o tratamento dos erros.

	- Semana do 04/06 : 
		Recebi uma resposta com uma breve explicação do erro e possíveis próximos passos. 
		Recebi também outra resposta de um outro desenvolvedor da comunidade informando 
		que criou uma branch com minhas modificações e que está trabalhando em correções.

	- Semana do 11/06 :
		Consegui arrumar mais um erro da implementação e atualizei no pull request, mas 
		ainda existem erros na minha simulação. O código compila e executa, mas está 
		apontando erro durante a simulação.
		Nesta semana trabalharei no banner que será exposto com os principais resultados 
		da pesquisa. Nele apontarei dados do paper que publicamos.

	

