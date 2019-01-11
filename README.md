# serialterm

A basic serial terminal program written in Python to be run
from the Windows 10 command prompt.

## Before downloading ...

This serial terminal program is designed to be
run and controlled by another program. If you want a serial terminal
program for interactive (i.e. human) use then I recommend
using `putty` by Simon Tatham - visit:

[PuTTY: a free SSH and Telnet client](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

for more details.

## Why did I write the `serialterm.py` program?

I wanted to automate a serial terminal session on Windows 10 to
configure a range of devices that I might connect to the serial port.
Here is a good example on YouTube of me doing exactly that:

[Raritan intelligent PDU being automatically configured via serial port](http://bit.ly/2H85TKf)

Trying to automate a serial terminal program like putty was, while possible, quite
a bit of work. If quickly realised that I wrote my own program I would have complete
control
over its appearance and expected inputs and this would make automating it
predictable and simpler.

## Pre-requisites

As well as the `serialterm.py` code here is what you also need:

* Windows 10
* Python 3.7
* Python module `pyserial` 3.4

Note: earlier versions of all of the above may well work as
the `serialterm.py` code does not do anything that unusual.

## Running `serialterm.py`

First of all run as:

```
python serialterm.py list
```

This will list any available COM ports.

For example if port `COM7` was available you could connect to it as follows:

```
python serialterm.py com7
```

If you need to specify a connection speed then use the `--speed` command
line option.  For example to connect at 9600:

```
python serialterm.py --speed 9600 com7
```

## Exiting the program

You can type `Control^C` which will interrupt the program in the expected way.

To exit more cleanly type:

```
~.
```

More precisely type the `~` character and then the fullstop/period character `.`
and the program will exit with a nice message.

## I want to type the `~` character

Just type `~` twice to get one `~`.  Give it a try.

## What else can it do?

Run:

```
python serialterm.py -h
```

to see all the command line options.

## Still to document

This README document is incomplete.  I still need to add detail on:

* The --capture and --defer arguments
* Using the ~ (tilde) character escapes
* The --ptimeout and -ktimeout arguments



-------------------------------

End of file
