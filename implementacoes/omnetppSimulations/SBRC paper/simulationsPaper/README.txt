Execução das simualções:
   - Setar o repeat = 2 do omnetpp.ini para 10;
   - Colocar o sim-time-limit = 20s do omnetpp.ini para 300s;
   - Na mesma pasta deste arquivo existe um script shell chamado cmdenv_run.sh, nesse arquivo é necessário alterar os
   caminhos de execução para os da máquina do Gold;
   - Após configurar o script é só dar "sh cmdenv_run.sh" no bash estando neste diretório no terminal;
   - Esse script provavelmente vai demorar um BOOOOOM tempo rodando, ainda mais com esse tempo de simulação;
   - Depois de rodar esse script é só verificar se a pasta sca_source deste diretório possui os .sca para análise;
   - Se estiver tudo certo é só rodar o results_analysis.py neste diretório;
   - Ele vai avisando na linha de comando em que passo ele está, oq demora mais é o de desenho;
   - Eu tirei o desenho dos dois parâmetros que eu achei irrelevantes (packetErro e bitError), mas se quiser voltar é só descomentar 
   onde eles são criados;
   - Na linha de comando no fim da execução ele imprime as médias de endToEndDelay e a porcentagem de pacotes perdidos que eu fiz;
   - As imagens ficam salvas no analysis_plot;

   Acho que é só isso, qqr dúvida me manda msg.

   GLHF!