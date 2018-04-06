# esp8266-micropython-blink
Minimalistic template containing main script and module for blink internal led from nodeMCU board. 

Requires esp8266 micropython firmware and nodeMCU board. 
Expected familiarity with mpfshell and esptool too.  

Inside bin folders, you will find some scripts to make erase, flash and upload easier, 
but you are free to use prefered (and best) methods. 

To upload blink to a brand new nodeMCU:

0 - Download esp-micropython-firmware
1 - Install mpfshell and esptool in your system
2 - Run bin/erase_flash
3 - Run bin/flash path-to-esp-micropython-firmware   
4 - Reset your board
5 - Run bin/upload_project

