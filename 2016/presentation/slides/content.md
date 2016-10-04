
<!-- .slide: data-background="resources/0.cover/background.png" -->

<h2 style="color: #EEEEEE;">
  <ol>
    <li>Introduction</li>
    </br>
    <li>Open Source Toolchains</li>
    </br>
    <li>Open Source Boards</li>
    </br>
    <li>Open Source IDEs</li>
    </br>
    <li>Python</li>
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

# What is a microcontroller?

"A small computer on a single integrated circuit". Created by Intel in the 1970's

![](resources/1.introduction/uC-intro.png)

---

# Microcontroller internals

![](resources/1.introduction/uC-internals.png)

---

# Microcontroller workflow

It executes specific machine language instructions one by one

</br>
</br>

![](resources/1.introduction/uC-workflow.png)

</br>
</br>
</br>

---

# Microcontroller vs Processor

</br>
</br>

|              |   Microcontroller   |  Processor        |
|:------------:|:-------------------:|:-----------------:|
| Applications | Specialized devices | General computing |
| Speed        | Relative slow (MHz) | Very fast (GHz)   |
| Cost         | Low (~$1)           | High (~$100)      |
| Consumption  | Low (1-100mW)       | High (1-100W)     |
| Vendors      | *Atmel, Microchip, TI, ST* | *Intel, AMD, ARM* |
| | |

</br>
</br>
</br>
</br>

---

# What is an FPGA?

"A reconfigurable digital integrated circuit". Created by Xilinx in the 1980's

</br>

![](resources/1.introduction/FPGA-intro.png)

</br>

---

# FPGA internals

Interconnected Logic Blocks, Memory Blocks and I/O ports

<img style="float: right;" src="resources/1.introduction/FPGA-config.gif">

![](resources/1.introduction/FPGA-internals.png)

---

# FPGA workflow

The bitstream defines a new real circuit in the FPGA

</br>
</br>

![](resources/1.introduction/FPGA-workflow.png)

</br>
</br>

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  2. Open Source Toolchains
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

## GNU C Compiler
(1987)

</br>

* *Language*: **C**
* *Architecture*: Motorola 68000
* *Website*: https://gcc.gnu.org/

![](resources/2.toolchains/mc68000.png)

---

## GNU Compiler Collection
[1987, 2016)

</br>

* *Languages*: **C, C++, Java, Ada, Objective-C, Fortran, Go ...**
* *Architectures*: ARM, AVR, AMD64, IA-32, PIC, Xtensa, **RISC-V**, ...

![](resources/2.toolchains/gcc-internals.jpg)

New compilers: clang/LLVM [2007, 2016)/[2003, 2016)

---

## GCC flow

![](resources/2.toolchains/gcc-flow.png)

---

## GCC flow - example

[examples/microcontroller/gcc]()

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

```
0000020a: 00000000 00000000 00000000 00000000 00000000 00000000
00000210: 00000000 01100101 01111000 01100001 01101101 01110000
00000216: 01101100 01100101 00101110 01100011 00000000 01101101
```

---

## IceStorm
[2015, 2016)

</br>

* *Language*: **Verilog**
* *FPGA*: Lattice iCE40
* *Website*: http://www.clifford.at/icestorm/

</br>

![](resources/2.toolchains/lattice-iCE40.png)

---

## IceStorm flow

![](resources/2.toolchains/icestorm-flow.png)

---

## IceStorm flow - example

[examples/FPGA/icestorm]()

</br>

```verilog
module led(output wire LED);
  assign LED = 1'b1;
endmodule
```

```bash
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

```bash
00000000: 11111111 00000000 00000000 11111111 01111110 10101010
00000006: 10011001 01111110 01010001 00000000 00000001 00000101
0000000c: 10010010 00000000 00100000 01100010 00000001 01001011
```

---

## Simulation

</br>

* Icarus Verilog: http://iverilog.icarus.com
* GTKWave: http://gtkwave.sourceforge.net

![](resources/2.toolchains/gtkwave-simulation.png)

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  3. Open Source Boards
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

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

## Lattice Development Kits

</br>

![](resources/3.boards/lattice.png)

* *FPGA*: iCE40
* **No sources available**

---

## icoBOARD

(2016)

![](resources/3.boards/icoboard-min.png)

* *FPGA*: iCE40-HK8K-CT256
* *Sources*: http://icoboard.org

---

## icoBOARD - demo

(2016)

</br>

<iframe width="620" height="350" src="https://www.youtube.com/embed/urjyWhCpMk4?rel=0&showinfo=0">
</iframe>

</br>


* *Processor*: https://github.com/cliffordwolf/picorv32
* *Examples*: https://github.com/Jesus89/picorv32-c-examples

---

## IceZUM

(2016)

![](resources/3.boards/icezum-min.png)

* *FPGA*: iCE40-HK1K-TQ144
* *Sources*: https://github.com/FPGAwars/icezum

---

## IceZUM - demo

(2016)

</br>

<iframe width="620" height="350" src="https://www.youtube.com/embed/6I5Z70eewrg?rel=0&showinfo=0">
</iframe>

</br>

* *Examples*: https://github.com/FPGAwars/FPGA-peripherals

---

### More Open FPGA Boards

</br>

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

## Emacs

[1976, 2016)

![](resources/4.ides/emacs-min.png)

* *Written in*: **Lisp**, **C**
* *Sources*: https://github.com/emacs-mirror/emacs

---

## Vim

[1991, 2016)

![](resources/4.ides/vim-min.png)

* *Written in*: **C**
* *Sources*: https://github.com/vim/vim

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

## Icestudio

(2016)

![](resources/4.ides/icestudio-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/icestudio

---

## Icestudio - demo

(2016)

</br>

<iframe width="700" height="395" src="https://www.youtube.com/embed/OWnVCjo7N9Y?start=52?rel=0&showinfo=0">
</iframe>

---

## Apio IDE

(2016)

![](resources/4.ides/apio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/apio-ide

---

<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  5. Python
</h1>

<!-- .slide: data-transition="slide-in fade-out" -->

---

## PlatformIO

[2014, 2016)

![](resources/5.python/platformio-logo.png)

|                           |
|---------------------------|
| 19 Development Platforms  |
| 148 Microcontroller Units |
| 321 Embedded Boards       |
| 1.159 Libraries           |
| 5.837 Library Examples    |
|                           |

</br>

* *Written in*: **Python**
* *Sources*: https://github.com/platformio/platformio

---

## PlatformIO - demo

[2014, 2016)

![](resources/5.python/platformio.gif)

---

![](resources/5.python/apio-logo-min.png)

(2016)

</br>

|               |                                                             |
|---------------|-------------------------------------------------------------|
| Packages      | icestorm, iverilog, scons, system, examples                 |
| Architectures | linux (x86_64, i386, armv7l, aarch64), windows, darwin      |
| Boards        | Icezum, Go board, icoBOARD, iCEstick, iCE40-HX8K            |
| Commands      | build, verify, clean, upload, time, sim                     |
|               |                                                             |

</br>

* *Based on PlatformIO*
* *Focused on open FPGA development*
* *Written in*: **Python**
* *Sources*: https://github.com/FPGAwars/apio

---

## Apio - demo

(2016)

</br>

<iframe width="700" height="395" src="https://www.youtube.com/embed/UJ6-_42P5BE?rel=0&showinfo=0">
</iframe>
