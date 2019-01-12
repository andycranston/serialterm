# serialterm

A basic serial terminal program written in Python to be run
from the Windows 10 command prompt.

## Demonstration video

This link:

[How to use the simple serialterm serial terminal program](https://youtu.be/tjnj2DLnkDw)

is a ten minute YouTube video showing what the program can do.

Note that this is designed to be
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

Trying to automate a serial terminal program like `putty` was, while
possible, quite a bit of work. I quickly realised that if I wrote my
own program I would have complete control over the appearance and
expected inputs and this would make the process of automating it
easier.

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

Just type `~` twice to get one `~`

## Capturing output

Run:

```
python serialterm.py --capture term.txt com7
```

to have all seesion output copied to file `term.txt`.

The related `--defer` option sets up session output capture but does
not start capturing:

```
python serialterm.py --capture term.txt com7
```

With `--defer` in order to actually start capure type the two character
sequence:

```
~c
```

(note that is a lowecase 'c')

To suspend capture type:

```
~C
```

(note that is an UPPERCASE 'C')

You can toggle (switch on and switch off) capture as many times as
you need during a session.

## Use a different escape character

By default the escape character is the tiled '~' character.  To use another
character:

```
python serialterm.py --escape + com7
```

In this exampel the plus sign '+' character is now the escape character
so to exit the program you now type:

```
+.
```

## The --ptimeout and -ktimeout arguments

These options are port timeout and keyboard timeout respectively.

The port timeout is the time in seconds the program will wait for any input from
the serial port.  By default it is 0.01 of a second.

The keyboard timeout is the time in seconds the program will wait after a key
is pressed to allow for the user to type another key.  By default it is 0.01 of a second.

To make `serialterm` respond a bit faster try:

```
python serialterm.py --ptimeout 0.001 -ktimeout 0.001 com7
```

but bear in mind this might cause more CPU cycles to be used even when there is
no data to be read from the port or no key strokes to be read from
the keyboard.

## Final notes

The timing logic for the main loop of the program probably needs
improving.  In particular how data is read from the port.

-------------------------------

End of file
