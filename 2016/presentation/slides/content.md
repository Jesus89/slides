# 1. Introduction

---

# What is a microcontroller?

TODO:

---

# What is an FPGA?

TODO:

---

# 2. Open Source Toolchains

---

## GNU C Compiler
(1987)

</br>

* *Language*: **C**
* *Architecture*: Motorola 68000
* *Website*: https://gcc.gnu.org/

![](resources/2.toolchains/mc68000.jpg)

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

</br>

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

```as
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
0000021c: 01100001 01101001 01101110 00000000 01110011 01110101
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

```v
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

```v
set_io LED 99
```

```
.logic_tile 12 12
000000000000000000000000000000000000000010000000000000
000000000000000000000000000000000000000000000000000000
```

```
00000000: 11111111 00000000 00000000 11111111 01111110 10101010
00000006: 10011001 01111110 01010001 00000000 00000001 00000101
0000000c: 10010010 00000000 00100000 01100010 00000001 01001011
00000012: 01110010 00000000 10010000 10000010 00000000 00000000
00000018: 00010001 00000000 00000001 00000001 00000000 00000000
```

---

## Simulation

* Icarus Verilog: http://iverilog.icarus.com
* GTKWave: http://gtkwave.sourceforge.net

</br>

![](resources/2.toolchains/gtkwave-simulation.png)

---

# 3. Open Source Boards

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

<iframe width="620" height="350" src="https://www.youtube.com/embed/urjyWhCpMk4">
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

<iframe width="620" height="350" src="https://www.youtube.com/embed/6I5Z70eewrg">
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

# 4. Open Source IDEs

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

<iframe width="700" height="395" src="https://www.youtube.com/embed/OWnVCjo7N9Y?start=52">
</iframe>

---

## Apio IDE

(2016)

![](resources/4.ides/apio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/apio-ide

---

# 5. Python

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

<iframe width="700" height="395" src="https://www.youtube.com/embed/UJ6-_42P5BE">
</iframe>
