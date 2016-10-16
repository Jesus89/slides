
<!-- .slide: data-background="resources/0.cover/background.png" -->

<h2 style="color: #EEEEEE;">
  <ol>
    <li>Introduction</li>
    <br>
    <li>Open Source Toolchains</li>
    <br>
    <li>Open Source Boards</li>
    <br>
    <li>Open Source IDEs</li>
    <br>
    <li>Python: the universal glue</li>
  </ol>
</h2>

<!-- .slide: data-transition="slide-in fade-out" -->

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  1. Introduction
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

## What is a microcontroller?

"A small computer on a single integrated circuit". Created by Intel in the 1970's

![](resources/1.introduction/uC-intro.png)

---

## Microcontroller internals

![](resources/1.introduction/uC-internals.png)

---

## Microcontroller workflow

It executes specific machine language instructions one by one

<br>
<br>

![](resources/1.introduction/uC-workflow.png)

<br>
<br>

---

## Microcontroller vs Processor

<br>
<br>

|              |   Microcontroller   |  Processor        |
|:------------:|:-------------------:|:-----------------:|
| Applications | Specialized devices | General computing |
| Speed        | Relative slow (MHz) | Very fast (GHz)   |
| Cost         | Low (~$1)           | High (~$100)      |
| Consumption  | Low (1-100mW)       | High (1-100W)     |
| Vendors      | *Atmel, Microchip, TI, ST* | *Intel, AMD, ARM* |
| | |

<br>
<br>
<br>
<br>

---

# FPGA time!

---

## What is an FPGA?

"A reconfigurable digital integrated circuit". Created by Xilinx in the 1980's

<br>

![](resources/1.introduction/FPGA-intro.png)

<br>

---

## FPGA internals

Interconnected Logic Blocks, Memory Blocks and I/O ports

<figure style="float: right;">
  <img  src="resources/1.introduction/FPGA-config.gif">
  <figcaption>(GIF created by *Juan González*)</figcaption>
</figure>

![](resources/1.introduction/FPGA-internals.png)

---

## FPGA workflow

The bit stream defines a new real circuit in the FPGA

<br>
<br>

![](resources/1.introduction/FPGA-workflow.png)

<br>
<br>

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  2. Open Source Toolchains
</h1>

<!--<h3 style="color: #EEEEEE;">
  <br>
  <ul>
    <li>GCC</li>
    <br>
    <li>IceStorm</li>
  </ul>
</h3>-->

<!-- .slide: data-transition="slide-in fade-out" -->

---

## GNU C Compiler
(1987)

<br>

* *Language*: **C**
* *Architecture*: Motorola 68000
* *Website*: https://gcc.gnu.org/

![](resources/2.toolchains/mc68000.png)

Created by *RMS* and the *GNU team*

---

## GNU Compiler Collection
[1987, 2016)

<br>

* *Languages*: **C, C++, Java, Ada, Objective-C, Fortran, Go ...**
* *Architectures*: ARM, AVR, AMD64, IA-32, PIC, Xtensa, **RISC-V**, ...

![](resources/2.toolchains/gcc-internals.jpg)

New compilers: **Clang/LLVM** [2007, 2016)/[2003, 2016)

---

## GCC flow

![](resources/2.toolchains/gcc-flow.png)

---

## GCC flow - example

[examples/microcontroller/gcc]()

<br>

```c
#define A 1
#define B 2

void main() {
    printf("%d + %d = %d\n", A, B, sum(A, B));
}
```

```c
void main() {
    printf("%d + %d = %d\n", 1, 2, sum(1, 2));
}
```

```x86asm
main:
      movl    $2, %esi
      movl    $1, %edi
      call    sum
      movl    %eax, %ecx
      movl    $2, %edx
      movl    $1, %esi
      movl    $.LC0, %edi
      movl    $0, %eax
      call    printf
```

```AsciiDoc
0000020a: 00000000 00000000 00000000 00000000 00000000 00000000
00000210: 00000000 01100101 01111000 01100001 01101101 01110000
00000216: 01101100 01100101 00101110 01100011 00000000 01101101
```

---

## All FPGA toolchains are privative :( <!-- .element: class="fragment" data-fragment-index="1" -->

## ...until now! :)  <!-- .element: class="fragment" data-fragment-index="2" -->

---

## IceStorm
[2015, 2016)

<br>

* *Language*: **Verilog**
* *FPGA*: Lattice iCE40
* *Website*: http://www.clifford.at/icestorm/

<br>

![](resources/2.toolchains/lattice-iCE40.png)

<br>

Created by *Clifford Wolf* through reverse engineering

---

## IceStorm flow

![](resources/2.toolchains/icestorm-flow.png)

---

## IceStorm flow - example

[examples/FPGA/icestorm]()

<br>

```verilog
module led(output wire LED);
  assign LED = 1'b1;
endmodule
```

```
.model led
.inputs
.outputs LED
.names $false
.names $true
1
.names $undef
.names $true LED
1 1
.end

```

```verilog
set_io LED 99
```

```bash
.logic_tile 12 12
000000000000000000000000000000000000000010000000000000
000000000000000000000000000000000000000000000000000000
```

```AsciiDoc
00000000: 11111111 00000000 00000000 11111111 01111110 10101010
00000006: 10011001 01111110 01010001 00000000 00000001 00000101
0000000c: 10010010 00000000 00100000 01100010 00000001 01001011
```

---

## Simulation

<br>

* Icarus Verilog: http://iverilog.icarus.com
* GTKWave: http://gtkwave.sourceforge.net

![](resources/2.toolchains/gtkwave-simulation.png)

---

## More storms coming

<br>

<img style="float: left;" src="resources/2.toolchains/clifford-project-x-ray.png">

<br>

* New Yosys front-ends:
  * VHDL
  * ...

<br>

* New FPGAs support:
  * Silego GreenPack4
  * Xilinx 7-Series
  * iCE40 Ultralite
  * ...

<br>
<br>
<br>

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  3. Open Source Boards
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

# Open Hardware

## Board's schematics are Open Source  <!-- .element: class="fragment" data-fragment-index="1" -->
## &micro;Controller's schematics are still privative  <!-- .element: class="fragment" data-fragment-index="2" -->

---

## Arduino

[2005, 2016)

![](resources/3.boards/arduino.png)

* *Languages*: **C, C++, ...**
* *Architecture*: Atmel AVR
* *Sources*: https://github.com/arduino

---

## NodeMCU

[2014, 2016)

![](resources/3.boards/nodemcu.png)

* *Languages*: **C, C++, Lua, MicroPython, ...**
* *Architecture*: Xtensa (**ESP8266**)
* *Sources*: https://github.com/nodemcu

---

# Open FPGAs

## Usable with Open Source Tools  <!-- .element: class="fragment" data-fragment-index="1" -->
## FPGA's schematics are still privative  <!-- .element: class="fragment" data-fragment-index="2" -->

---


## Lattice Development Kits

<br>

![](resources/3.boards/lattice.png)

* *FPGA*: iCE40 family
* **No sources available**

---

## icoBOARD

(2016)

![](resources/3.boards/icoboard-min.png)

* Raspberry Pi HAT
* Created by *icoTC team*
* *Sources*: http://icoboard.org

---

## icoBOARD - demo

(2016)

<br>

<iframe width="620" height="350" src="https://www.youtube.com/embed/urjyWhCpMk4?rel=0&showinfo=0">
</iframe>

<br>


* *Processor*: https://github.com/cliffordwolf/picorv32
* *Examples*: https://github.com/Jesus89/picorv32-c-examples

---

## IceZUM

(2016)

![](resources/3.boards/icezum-min.png)

* FPGA board for makers
* Created by *Eladio Delgado* and *Juan González*
* *Sources*: https://github.com/FPGAwars/icezum

---

## IceZUM - demo

(2016)

<br>

<iframe width="620" height="350" src="https://www.youtube.com/embed/6I5Z70eewrg?rel=0&showinfo=0">
</iframe>

<br>

* *Examples*: https://github.com/FPGAwars/FPGA-peripherals

---

### More Open FPGA Boards

<br>

|           |                                         |
|-----------|-----------------------------------------|
| Olimex    | https://github.com/OLIMEX/iCE40HX1K-EVB |
| eCowLogic | https://github.com/Agilack/eCow-logic   |
| CAT board | https://github.com/xesscorp/CAT-Board   |
| myStorm   | https://folknologylabs.wordpress.com    |
| Go board  | https://www.nandland.com/goboard        |
| ...       |                                         |

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  4. Open Source IDEs
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

## Arduino IDE

[2005, 2016)

![](resources/4.ides/arduino-ide-min.png)

* *Written in*: **Java, C, C++**
* *Sources*: https://www.arduino.cc

---

## Eclipse

[2001, 2016)

![](resources/4.ides/eclipse-min.png)

* *Written in*: **Java**
* *Sources*: https://www.eclipse.org

---

## Atom

[2014, 2016)

![](resources/4.ides/atom-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/atom/atom

---

## PlatformIO IDE

(2016)

![](resources/4.ides/platformio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/platformio/platformio-atom-ide

---

# Open FPGA IDEs

---

## Apio IDE

(2016)

![](resources/4.ides/apio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/apio-ide

---

## Icestudio

(2016)

![](resources/4.ides/icestudio-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/icestudio

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  5. Python: the universal glue
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

## PlatformIO

[2014, 2016)

![](resources/5.python/platformio-logo.png)

|       |                       |
|------:|-----------------------|
| 19    | Development Platforms |
| 348   | Embedded Boards       |
| 1.193 | Libraries             |
| 6.022 | Library Examples      |
|       |                       |

<br>

* Created by *Ivan Kravets*
* *Front-end*: PlatformIO IDE, Eclipse, ...
* *Written in*: **Python**
* *Sources*: https://github.com/platformio/platformio

---

## PlatformIO - demo

[2014, 2016)

![](resources/5.python/platformio.gif)

---

## Apio

(2016)

![](resources/5.python/apio-logo-min.png)

|                |                                                             |
|---------------:|-------------------------------------------------------------|
| Packages       | icestorm, iverilog, scons, system, examples                 |
| Architectures  | linux (x86_64, i686, armv7l, aarch64), windows, darwin      |
| Boards         | Icezum, Go board, icoBOARD, iCEstick, iCE40-HX8K, Cat board |
| Commands       | build, verify, clean, upload, time, sim                     |
|                |                                                             |

<br>

* **Focused on open FPGA development**
* *Based on PlatformIO*
* *Front-ends*: Icestudio, Apio IDE
* *Written in*: **Python**
* *Sources*: https://github.com/FPGAwars/apio

---

## PIO Lattice iCE40 support

<br>

![](resources/5.python/apio-pio.png)

1. Initial FPGA support (\#480)
2. Apio created. Based on PlatformIO
3. First release with FPGA support (2.9.0)
4. Fully decentralized architecture (3.0.0)
5. Contributions to platform-lattice_ice40

---

# Demo

![](resources/5.python/demo-stack.png)
