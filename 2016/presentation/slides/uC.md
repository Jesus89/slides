<!-- .slide: data-transition="fade" -->

![](resources/index/1.svg)

---

## What is a microcontroller?



---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/2.svg)

---

# Open Source Toolchain

---

## GNU C Compiler
(1987)

</br>

* *Language*: **C**
* *Architecture*: Motorola 68000

![](resources/mc68000.jpg)

---

## GNU Compiler Collection
[1987, 2016)

</br>

* *Languages*: **C, C++, Java, Ada, Objective-C, Fortran, Go ...**
* *Architectures*: ARM, AVR, AMD64, IA-32, PIC, Xtensa, **RISC-V**, ...

![](resources/gcc-internals.jpg)

Other compilers: clang/LLVM [2007, 2016)/[2003, 2016)

---

## GCC flowchart

</br>

![](resources/gcc-flowchart.png)

---

## GCC flowchart - example

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

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/3.svg)

---

# Open Source Boards

---

## Arduino

[2005, 2016)

![](resources/arduino.png)

* *Languages*: **C, C++, ...**
* *Architecture*: Atmel AVR
* *Sources*: https://github.com/arduino

---

## NodeMCU

[2014, 2016)

![](resources/nodemcu.png)

* *Languages*: **C, C++, Lua, MicroPython, ...**
* *Architecture*: Xtensa (**ESP8266**)
* *Sources*: https://github.com/nodemcu

---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/4.svg)

---

# Open Source Multiplatform IDEs

---

## Vim

[1991, 2016)

![](resources/vim-min.png)

* *Written in*: **C**
* *Sources*: https://github.com/vim/vim


---

## Arduino IDE

[2005, 2016)

![](resources/arduino-ide-min.png)

* *Written in*: **Java, C, C++**
* *Sources*: https://www.arduino.cc

---

## Eclipse

[2001, 2016)

![](resources/eclipse-min.png)

* *Written in*: **Java**
* *Sources*: https://www.eclipse.org

---

## Atom

[2014, 2016)

![](resources/atom-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/atom/atom

---

<!-- .slide: data-transition="slide-in fade-out" -->

![](resources/index/5.svg)

---

## &micro;Controllers and Python

---

## PlatformIO

[2014, 2016)

![](resources/platformio-logo.png)

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

## PlatformIO CLI

[2014, 2016)

![](resources/platformio.gif)

---

## PlatformIO IDE

[2016)

![](resources/platformio-ide-min.png)

* *Written in*: **Javascript, HTML**
* *Sources*: https://github.com/platformio/platformio-atom-ide
