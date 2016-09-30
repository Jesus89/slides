![](resources/index/6.svg)

---

# What is an FPGA?

---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/7.svg)

---

# Open Source Toolchain

---

## IceStorm
[2015, 2016)

</br>

* *Language*: **Verilog**
* *FPGA*: Lattice iCE40
* *Website*: http://www.clifford.at/icestorm/

</br>

![](resources/lattice-iCE40.png)

---

## IceStorm flow

![](resources/icestorm-flow.png)

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

![](resources/gtkwave-simulation.png)

---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/8.svg)

---

# Open Source Boards

---

## Lattice Development Kits

</br>

![](resources/lattice.png)

* *FPGA*: iCE40
* **No sources available**

---

## icoBOARD

(2016)

![](resources/icoboard-min.png)

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

![](resources/icezum-min.png)

* *FPGA*: iCE40-HK1K-TQ144
* *Sources*: https://github.com/FPGAwars/icezum

---

## Icezum - demo

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

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/9.svg)

---

# Open Source Multiplatform IDEs

---

## Icestudio

(2016)

![](resources/icestudio-min.png)

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

![](resources/apio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/FPGAwars/apio-ide

---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/10.svg)

---

# Python and FPGAs

---

![](resources/apio-logo-min.png)

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
