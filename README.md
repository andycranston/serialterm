# serialterm

A (very) simple serial terminal written in Python to be run
from the Windows command prompt

## Before downloading ...

If you are looking for a nice and easy to use serial terminal to use on
your Windows 10 laptop then this one is NOT for you. Instead try Simon Tatham's excellent
`putty`.

However, if you want a simple serial terminal program that you can run
in a Windows command prompt window and control from an automation
program then this might be for you.

## Why did I write this?

I wanted to automate a serial terminal session on Windows 10 to configure a range of devices
I might connect to the serial port.  Here is a good example on YouTube of me doing exactly that:

[Raritan intelligent PDU being automatically configured via serial port](http://bit.ly/2H85TKf)

## Pre-requisites

As well as the `serialterm.py` code here is what you also need:

* Windows 10
* Python 3.7
* Python module `pyserial` 3.4

Note: earlier versions of all of the above may well work as the `serialterm.py` code
does not do anything that unusual.

## Running

First of all run as:

```
python serialterm.py list
```

This will list any available COM style ports available.

If port `COM7` was available you could connect to it as follows:

```
python serialterm.py com7
```

If you need to specify a speed then use the `--speed` command line option.  For example
to connect at 9600:

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

Easy - just type `~` twice to get one `~`.  Give it a try.

## What else can it do?

Not much.  Run:

```
python serialterm.py -h
```

to see all the command line options.

Better still visit:

[xxx](http://yyy)

For a demo video on YouTube.

## Built with automation in mind

The program is intended by another program - NOT a human typing away. This keeps
code simple.  It also makes it easy to add features to help your automation
activities.

-------------------------------

End of file
