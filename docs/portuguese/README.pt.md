<div align="center">

# PROJECT Time IS Money

Uma iniciativa para criar o primeiro ativo do mundo cujo valor é determinado por si próprio.

---

[English](https://github.com/mickietoken/Time-IS-Money/blob/main/README.md) | [Español](https://github.com/mickietoken/Time-IS-Money/blob/main/docs/spanish/README.es.md) | [Português](https://github.com/mickietoken/Time-IS-Money/blob/main/docs/portuguese/README.pt.md) | [Français](https://github.com/mickietoken/Time-IS-Money/blob/main/docs/french/README.fr.md) | [Hindi](https://github.com/mickietoken/Time-IS-Money/blob/main/docs/indian/README.hi.md)

</div>

## A IDEIA

A ideia é criar um ativo que mostre exatamente quando atingirá o seu pico, quando irá cair abruptamente e quantas vezes alcançará máximos históricos, para que os investidores saibam quando investir, durante quanto tempo manter o ativo e quando vender, com risco mínimo. Um algoritmo irá valorizar automaticamente esse ativo através de aumentos incrementais baseados no tempo, usando Bitcoin como moeda de referência.

Atualmente, todos os ativos do mundo são valorizados com base no sentimento ou nas condições do mercado, enquanto são manipulados por bilionários, políticos e day traders que passam o dia a observar gráficos.

Com o AVC, o ativo (Tokenmobiles) será **AUTOVALORIZADO**, sem depender de valorização ou validação externas.

Para concretizar isto, são necessários programadores que construam a sua própria versão do programa. (São necessárias pelo menos 100 versões para um lançamento seguro e sustentável.)

A partir do DIA DE INÍCIO, o programa deverá funcionar sem interrupções durante mais de 200 anos e **NUNCA PODERÁ SER PARADO**.

O programa deverá ser como o próprio tempo mundial: várias versões a funcionar em diferentes servidores e dispositivos, todas a seguir o mesmo padrão/algoritmo.

Antes de começarem a desenvolver a sua versão com as ferramentas que escolherem, os programadores precisarão das características fundamentais do ativo e dos detalhes do algoritmo AVC.

-
-
-
-

## O ATIVO

Foram implementados na blockchain Stacks 100 contratos inteligentes padrão de tokens fungíveis.

Cada contrato inteligente contém um Tokenmobile único, com uma oferta entre 200 e 50 000.

Existem 999 999 Tokenmobiles no total.

Cada Tokenmobile possui atributos/metadados essenciais para o algoritmo AVC.

Os metadados estão protegidos na Arweave e têm cópias de segurança na IPFS.

![](/media/asset.png)

**TYPE** — A etiqueta/o nome do Tokenmobile em código Morse.

**SUPPLY** — O token individual dentro da oferta fixa do contrato inteligente.

**CYCLES** — O número de vezes que o valor do Tokenmobile irá cair/reiniciar e recuperar novamente.

**BOOST** — A percentagem de aumento da duração do ciclo do Tokenmobile sempre que este reinicia. Isto aumenta o seu valor máximo.

**START** — A duração do primeiro ciclo.

**MAX** — A duração do último ciclo.

**AVC** — O algoritmo/motor que determina o valor de cada Tokenmobile.

-
-
-
-

## O ALGORITMO

• **A de Automation (Automação).** A automação é o TEMPO, medido em intervalos de 60 segundos.

• **V de Valuation (Valorização).** A valorização ocorre em incrementos de 0.00001 ou 0.00003.

• **C de Currency (Moeda).** A moeda é o ₿itcoin, utilizado como referência para valorizar os Tokenmobiles.

Assim, um Tokenmobile aumentará ₿0.00001 ou ₿0.00003 a cada 60 segundos.

-
-
-
-

## O PROGRAMA

![](/media/program.jpg)

Aqui está uma demonstração AO VIVO. [VER DEMONSTRAÇÃO](https://tokenmobiles.live/)

Está a ver 2 RACKS com 2 Tokenmobiles a serem valorizados pelo AVC. (O programa oficial terá 100 RACKS.)

1. É o endereço/localização do contrato inteligente do ativo que está a ser valorizado.

2. É o contador crescente em tempo real, formatado como YY/DDD/HH/MM/SS (os DIAS são contados em períodos de 365 dias). Sem anos bissextos, semanas, meses ou milissegundos.

3. É a marca temporal em que o ciclo atual termina e o contador para antes de reiniciar. (As marcas temporais dos ciclos de cada Tokenmobile estão no ficheiro FUNDAMENTALS.)

4. É o total de CICLOS, que diminui sempre que o contador reinicia e a marca temporal é atualizada. (O primeiro ciclo deve diminuir imediatamente quando o AVC de um Tokenmobile começa, e não quando termina.)

5. É o BOOST.

6. É o SUPPLY.

(BOOST e SUPPLY são apenas apresentados na interface. Não executam ações no código.)

7. É o valor AVC do Tokenmobile, que aumenta em incrementos de ₿0.00001 ou ₿0.00003 sempre que o contador completa 60 segundos. O valor regressa a ₿0.00000 quando começa um novo ciclo. (No final do último ciclo, o valor deve parar e permanecer na sua valorização máxima.)

O programa oficial, pronto para o DIA DE INÍCIO, deverá ter 100 RACKS de cada um dos 100 contratos inteligentes Tokenmobile, todos iniciados em simultâneo e a funcionar com AVC até cada um terminar o seu percurso de valorização. Tokenmobiles-100 será o primeiro a terminar, após apenas 60 dias, com uma valorização máxima de ₿0.86400; Tokenmobiles-43 será o último, após mais de 200 anos, com uma valorização máxima de ₿338.93753.

O programa exige uma infraestrutura de servidor backend, uma interface frontend que apresente atualizações em tempo real, segundo a segundo e sem atrasos, e uma solução de alojamento capaz de garantir 99.99% de disponibilidade durante mais de 200 anos.

-
-
-
-

## O CÓDIGO

Espera-se que cada programador desenvolva a sua versão do programa inteiramente do zero, utilizando as ferramentas que preferir, o seu próprio servidor, a sua solução de alojamento e os fundamentos fornecidos. A demonstração pode ser usada como modelo, mas não copie linha a linha o código da demonstração nem o de outras versões.

O objetivo é evitar versões duplicadas que possam conter os mesmos erros de código. Devem existir implementações diferentes do mesmo programa, contribuindo assim para a sua longevidade e segurança.

-
-
-
-

## O AMBIENTE

A iniciativa Time IS Money estará ativa no GitHub e no Discord, onde os programadores poderão reunir-se para discutir e partilhar atualizações sobre o seu progresso na criação do programa.

Quando os programadores estiverem a desenvolver ativamente e a partilhar testes do programa, receberão a data do DIA DE INÍCIO para o lançar oficialmente em funcionamento, juntamente com um pacote do ativo que o programa valoriza. (Tokenmobiles equivalentes aos ciclos dos primeiros 10 anos.)

-
-
-
-

## A CONQUISTA

Se mais de 100 versões do programa entrarem em funcionamento no DIA DE INÍCIO, sejam públicas ou privadas, o ativo e o programa adquirirão imediatamente relevância e importância consolidadas. Em comparação com ações, metais, criptomoedas, ETFs, etc., seria o único ativo do mundo cujo valor é determinado por si próprio.
