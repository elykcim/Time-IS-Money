<div align="center">

# PROJECT Time IS Money

Una iniciativa para crear el primer activo del mundo cuyo valor se determina a sí mismo.

---

[English](https://github.com/elykcim/Time-IS-Money/blob/main/README.md) | [Español](https://github.com/elykcim/Time-IS-Money/blob/main/docs/spanish/README.es.md) | [عربي](https://github.com/elykcim/Time-IS-Money/blob/main/docs/arabic/README.ar.md) | [Français](https://github.com/elykcim/Time-IS-Money/blob/main/docs/french/README.fr.md) | [Hindi](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.hi.md) | [Português](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.to.md) | [Русский](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.ru.md)

</div>

## LA IDEA

La idea es crear un activo que muestre exactamente cuándo alcanzará su pico, cuándo se desplomará y cuántas veces llegará a un máximo histórico, para que los inversores sepan cuándo invertir, cuánto tiempo mantenerlo y cuándo vender con un riesgo mínimo. Para ello, se utilizará un algoritmo que valore automáticamente dicho activo mediante incrementos de valor basados en el tiempo, tomando Bitcoin como moneda de referencia.

Actualmente, todos los activos del mundo se valoran según el sentimiento del mercado o las condiciones del mercado, mientras son manipulados por multimillonarios, políticos y operadores diarios que pasan el día mirando gráficos.

Con el AVC, el activo (Tokenmobiles) tendrá un valor **AUTODETERMINADO**, sin depender de la apreciación ni de la validación externas.

Para llevarlo a cabo, se necesitan programadores que construyan su propia versión del programa. (Se necesitan al menos 100 versiones para un lanzamiento seguro y sostenible).

A partir del DÍA DE INICIO, el programa deberá ejecutarse y avanzar sin interrupciones durante más de 200 años y **NUNCA PODRÁ DETENERSE**.

El programa debe ser como el propio tiempo mundial: múltiples versiones funcionando en distintos servidores y dispositivos, todas siguiendo el mismo patrón/algoritmo.

Antes de empezar a crear sus versiones con las herramientas que elijan, los programadores necesitarán las características fundamentales del activo y los detalles del algoritmo AVC.

-
-
-
-

## EL ACTIVO

Se desplegaron 100 contratos inteligentes estándar de tokens fungibles en la blockchain de Stacks.

Cada contrato inteligente contiene un Tokenmobile único, con una oferta que oscila entre 200 y 50 000.

Hay 999 999 Tokenmobiles en total.

Cada Tokenmobile único tiene atributos/metadatos esenciales para el algoritmo AVC.

Los metadatos están protegidos en Arweave y respaldados en IPFS.

![](/media/asset.png)

**TYPE** — La etiqueta/nombre del Tokenmobile en código Morse.

**SUPPLY** — El token individual dentro de la oferta fija del contrato inteligente.

**CYCLES** — El número de veces que el valor del Tokenmobile caerá/se reiniciará y volverá a recuperarse.

**BOOST** — El porcentaje de aumento de la duración del ciclo del Tokenmobile cada vez que se reinicia. Esto aumenta su valor máximo.

**START** — La duración del primer ciclo.

**MAX** — La duración del último ciclo.

**AVC** — El algoritmo/motor que determina el valor de cada Tokenmobile.

-
-
-
-

## EL ALGORITMO

• **A — Automation (Automatización).** La automatización es el TIEMPO, y el tiempo se mide en intervalos de 60 segundos.

• **V — Valuation (Valoración).** La valoración se realiza en incrementos de 0.00001 o 0.00003.

• **C — Currency (Moneda).** La moneda es ₿itcoin, utilizada como referencia para valorar los Tokenmobiles.

Por tanto, un Tokenmobile aumentará en ₿0.00001 o ₿0.00003 cada 60 segundos.

-
-
-
-

## EL PROGRAMA

![](/media/program.jpg)

Aquí hay una demostración EN VIVO. [VER DEMOSTRACIÓN](https://tokenmobiles.live/)

Estás viendo 2 RACKS con 2 Tokenmobiles valorados mediante AVC. (El programa oficial tendrá 100 RACKS).

1. Es la dirección/ubicación del contrato inteligente del activo que se está valorando.

2. Es el contador ascendente en vivo, con formato YY/DDD/HH/MM/SS (los DÍAS se cuentan en períodos de 365 días). Sin años bisiestos, semanas, meses ni milisegundos.

3. Es la marca de tiempo en la que terminará el ciclo actual y el contador se detendrá para reiniciarse. (Las marcas de tiempo de los ciclos de cada Tokenmobile se proporcionan en el archivo FUNDAMENTALS).

4. Es el total de CICLOS, que disminuye cada vez que el contador se reinicia y se actualiza la marca de tiempo. (El primer ciclo debe disminuir inmediatamente cuando se inicia el AVC de un Tokenmobile, no cuando termina).

5. Es el BOOST.

6. Es el SUPPLY.

(BOOST y SUPPLY solo se muestran en la interfaz de usuario. No ejecutan ninguna acción en el código).

7. Es el AVC/valor del Tokenmobile, que aumentará en incrementos de ₿0.00001 o ₿0.00003 cada vez que el contador complete 60 segundos. El valor vuelve a ₿0.00000 al comenzar un nuevo ciclo. (Al finalizar el último ciclo, el valor debe detenerse y permanecer en su valoración máxima).

El programa oficial, listo para el DÍA DE INICIO, deberá tener 100 RACKS de cada uno de los 100 contratos inteligentes Tokenmobile, todos iniciados a la vez y funcionando simultáneamente mediante AVC hasta que cada uno complete su recorrido de valoración. Tokenmobiles-100 será el primero en terminar, tras solo 60 días, con una valoración máxima de ₿0.86400; Tokenmobiles-43 será el último, tras más de 200 años, con una valoración máxima de ₿338.93753.

El programa requiere una infraestructura de servidor backend, una interfaz frontend que muestre actualizaciones en tiempo real segundo a segundo sin retrasos y una solución de alojamiento capaz de garantizar un tiempo de actividad del 99.99 % durante más de 200 años.

-
-
-
-

## EL CÓDIGO

Se espera que cada programador codifique su versión del programa completamente desde cero, utilizando las herramientas que elija, su propio servidor, su solución de alojamiento y los fundamentos que se le proporcionen. La demostración puede utilizarse como plantilla, pero, por favor, no copies línea por línea el código de la demostración ni el de otras versiones.

El motivo es evitar versiones duplicadas que posiblemente compartan los mismos errores de código. Debe haber distintas implementaciones del mismo programa. Esto ayuda a mantener la longevidad y la seguridad del programa.

-
-
-
-

## EL ENTORNO

La iniciativa Time IS Money estará activa en GitHub y Discord, donde los programadores podrán reunirse para debatir y compartir actualizaciones sobre su progreso en la creación del programa.

Cuando los programadores estén desarrollando activamente y compartiendo ejecuciones de prueba del programa, recibirán la fecha del DÍA DE INICIO para ponerlo oficialmente en funcionamiento, así como un paquete del activo que el programa valorará. (Tokenmobiles equivalentes a los primeros 10 años de ciclos).

-
-
-
-

## EL LOGRO

Si más de 100 versiones del programa se ponen en marcha el DÍA DE INICIO, ya sean públicas o privadas, el activo y el programa adquirirán inmediatamente relevancia e importancia consolidadas. En comparación con acciones, metales, criptomonedas, ETF, etc., sería el único activo del mundo cuyo valor se determina a sí mismo.
