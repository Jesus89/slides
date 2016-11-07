<!-- .slide: data-background="resources/0.cover/background.png" -->

<h1 style="color: #EEEEEE;">
  Bonus
</h1>

![](resources/6.bonus/python-logo-mini.png)

<br>

<h3 style="color: #EEEEEE;">
  click - SCons - pySerial - pytest - tox
</h3>

[examples/Python-resources](https://github.com/Jesus89/slides/tree/master/2016-10-Python-uControllers-and-FPGAs/examples/Python-resources)

<!-- .slide: data-transition="slide-in fade-out" -->

---

## click

http://click.pocoo.org

Command Line Interface Creation Kit

```python
# content of hello.py

import click

@click.command()
@click.option('-c', '--count', default=1, help='Number of Hello! messages.')
def hello(count):
    for x in range(count):
        click.echo('Hello!')

if __name__ == '__main__':
    hello()
```

```AsciiDoc
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  -c, --count INTEGER  Number of Hello! messages.
  --help               Show this message and exit.
```

```AsciiDoc
$ python hello.py --count 2
Hello!
Hello!
```

---

## SCons

http://scons.org/

A software construction tool. Cross-platform substitute for the classic Make utility

Python 2 (+3 support in >2.5.0)

```python
# content of SConstruct
Program(['example.c', 'math.c'])
```

```AsciiDoc
$ scons
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
gcc -o example.o -c example.c
gcc -o math.o -c math.c
gcc -o example example.o math.o
scons: done building targets.
```

```AsciiDoc
$ scons -c
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Cleaning targets ...
Removed example.o
Removed math.o
Removed example
scons: done cleaning targets.
```

---

## pySerial

http://pyserial.readthedocs.io

Encapsulates the access for the serial port

```python
import serial

port = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
port.write('on')
print(port.readline())
port.close()
```

#### list_ports

```AsciiDoc
$ python -m serial.tools.list_ports
/dev/ttyUSB0        
/dev/ttyUSB1        
2 ports found
```

#### miniterm

```AsciiDoc
$ python -m serial.tools.miniterm /dev/ttyUSB1
--- Miniterm on /dev/ttyUSB1  9600,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
```

---

## pytest

http://doc.pytest.org

The testing framework

```python
# content of test_sample.py

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

```AsciiDoc
$ pytest
============== test session starts ===============
collected 1 items

test_sample.py F

==================== FAILURES ====================
__________________ test_answer ___________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:7: AssertionError
============ 1 failed in 0.01 seconds ============
```

---

## tox

https://tox.readthedocs.io

Generic virtualenv management and test command line tool

```
├── example
│   ├── __init__.py
│   └── math.py
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_example.py
└── tox.ini
```

```ini
# content of: tox.ini

[tox]
envlist = py27, py35

[testenv]
deps=pytest
commands=py.test
```

```AsciiDoc
$ tox
[...]
_____________________ summary ______________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)
```
