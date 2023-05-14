## Sobre o Projeto

O objetivo deste projeto é criar um sistema para controle e monitoramento de vagas de estacionamento, utilizando placas Raspberry PI acompanhandas de um servidor central e uma interface de usuário. 

O sistema deve monitorar a entrada e saída dos veículos, o andar no qual eles se encontram e o preço cobrado por sua estadia.

## Visão Geral

O sistema consiste em um estacionamento de dois andares, cada um controlado por uma placa e, portanto, processo separado. 

Os servidores distribuídos se comunicarão com o servidor central através do protocolo TCP/IP usando o formato JSON (Brilakis et al., 2013)

## <a href="https://gitlab.com/fse_fga/trabalhos-2023_1/trabalho-1-2023-1#3-funcionamento-e-requisitos">Funcionamento e Requisitos</a>


## Componentes

<ul>
  <li>2 placas Raspberry Pi</li>
  <li>2 botões para entrada/cancelamento</li>
  <li>2 sensores de emergência</li>
  <li>2 sensores de cancelamento</li>
  <li>16 sensores de vacância</li>
  <li>2 botões de saída/cancelamento</li>
  <li>2 LEDs</li>
  <li>Python 3</li>
  <li>Flask (Servidor Central)</li>
  <li>RPi.GPIO (Controle dos pinos GPIO da Raspberry Pi)</li>
  <li>SQLite (armazenar dados do estacionamento)</li>
</ul>


## Referências
Brilakis, I.; Lee, S. H.; Becerik-Gerber Burçin. Computing in Civil Engineering: June 23-25, 2013, Los Angeles, California; ASCE, American Society of Civil Engineers: Reston, VA, 2013. 

Global Street Design Guide; Island Press: Washington D.C., 2015. 

Teodorovic, D.; Janic, M. Transportation Engineering: Theory, Practice, and Modeling; Elsevier Science & Technology: San Diego, 2022. 

