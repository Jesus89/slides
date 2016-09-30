# Bonus

![](resources/6.bonus/python-logo-mini.png)

- click
- SCons
- pySerial
- Requests
- pytest
- tox

---

## click

http://click.pocoo.org

* Command Line Interface Creation Kit
* Unix command line conventions
* Fully nestable and composable
* Environment variables, prompting, file handling
* Useful common helpers
* Python 2 and 3

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of Hello! messages.')
def hello(count):
    for x in range(count):
        click.echo('Hello!')

if __name__ == '__main__':
    hello()
```

```bash
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --count INTEGER  Number of Hello! messages.
  --help           Show this message and exit.

```

```bash
$ python hello.py --count 2
Hello!
Hello!

```

---

## SCons

http://scons.org/

* A software construction tool
* Cross-platform substitute for the classic Make utility
* Automatic dependency analysis
* Support multiple languages
* Python 2 (+3 support in >2.5.0)

```python
# SConstruct
Program(['example.c', 'math.c'])
```

```bash
$ scons
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
gcc -o example.o -c example.c
gcc -o math.o -c math.c
gcc -o example example.o math.o
scons: done building targets.
```

```bash
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

* Encapsulates the access for the serial port
* Access to the port settings through Python properties
* Support byte sizes, stop bits, parity, RTS/CTS and Xon/Xoff
* Tools: list_ports, miniterm
* Python 2 and 3

```python
import serial

port = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
port.write('on')
print(port.readline())
port.close()
```

```python
$ python -m serial.tools.list_ports
/dev/ttyUSB0        
/dev/ttyUSB1        
2 ports found
```

```python
$ python -m serial.tools.miniterm /dev/ttyUSB1
--- Miniterm on /dev/ttyUSB1  9600,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
```

---

## pytest

http://doc.pytest.org

* Testing framework
* Assert statements
* Auto-discovery of tests
* Compatible with unittest and nose
* +150 external plugins


```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

```
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

test_sample.py:6: AssertionError
============ 1 failed in 0.01 seconds ============
```

---

## tox

https://tox.readthedocs.io

* Generic virtualenv management and test command line tool
* checking your package installs correctly with different Python versions and interpreters
* running your tests in each of the environments, configuring your test tool of choice
* acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

```
example
setup.py
tests
tox.ini
```

```
# content of: tox.ini
[tox]
envlist = py27, py35

[testenv]
deps=pytest
commands=py.test
```

```
$ tox
[...]
_____________________ summary ______________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)
```
