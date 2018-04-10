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