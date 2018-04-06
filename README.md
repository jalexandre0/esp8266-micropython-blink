# esp8266-micropython-blink
Minimalistic template containing main program and blink module.

Instead put all the code in main.py (as a lot of tutorials do), I'd prefer
split the code into files and use this repository as template for my next projects.

Of course, you can do the same.  
 
To run blink, you will need a esp8266, a micropython firmware and led. This code will 
run without modifications in any nodeMCU with internal led wired to GPIO 2. If you have other scenario, adjust blink/blink.py file to reflect your hardware. 

Also, some familiarity with mpfshell and esptool is expected, but you can (and should) use your prefered framework. I like mpfshell and recomend.   

Inside "bin" folder, you will find scripts to erase, flash and upload firmware. 
The flash firmware script is adjusted to nodeMCU boards. Again, fell free to use 
any methods that works well to you. 

To upload esp8266-micropython-blink nodeMCU board, you will need:

    0 - Download stable esp-micropython-firmware 
    1 - Install mpfshell and esptool in your system
    2 - Copy esptool to 'bin' folder
    3 - Run bin/erase_flash
    4 - Run bin/flash path-to-esp-micropython-firmware   
    5 - Reset your board
    6 - Run bin/upload_project
    7 - Reset your board

If everything run smoothly, after reset you should see the internal led blinking. 

Now its time to play. 

Use bin/repl script to invoke micropyhton interactive shell. This must interrupt any code
running on board and present you with interactive prompt. 

To resume operation of your board using interactive prompt, run:


    >>> from main import *
    >>> main()


If you read the blink/blink.py file, you will notice that function responsible for toggle the led on or off is the 'toggle(pin)' function, so, if you want to test it, you should run:


    >>>  from blink.blink import *
    >>>> toggle(pin)

Lets develop a simple function who should write 'hello, I'm a new function' on screen. Lets do this using REPL

    >>>> def hello():
    >>>>     print("Hello, I'm a new function")
    >>>>
    >>>>
    >>>>

Then, run it:

    >>>> hello()
    Hello, I'm a new function

Now, lets modify some already existing function. Using your prefered text editor, open the blink/blink.py and modify the toggle function:

    def toggle(p):
        p.value(not p.value())
        print("Toggle function " + str(p.value()))

Use the bin/upload_project to upload the changes (close the repl first). 

After upload reset your board and you should see the new changes. Now, you are ready to start develop your own projects. 


