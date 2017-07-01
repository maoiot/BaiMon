# BaiMon

ESP8266 - based monitoring device for Vaillant boilers.

Periodically monitors boiler internal state, temperature and pressure.

Measured values can be viewed using Web interface.
Automatic data publishing to 'narodmon.ru' is also available.

This version supports Vaillant TurboTec Pro, but can be easily adapted to other models having EBus interface.

Requires Arduino IDE with ESP8266 support to compile and upload to ESP8266-based controller (I run it on Wemos D1 Mini). 

Controller comminicates to the boiler using UART. Adapter is needed to adjust signal levels (EBus uses 9-20 volts).

EBus-adapter.pdf contains schematics of a simple EBus adapter with optical decoupling. It can be connected directly to ESP8266 outputs. 

