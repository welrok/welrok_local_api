Telemetry
~~~~~~~~~

Telemetry is used to obtain the current state of device.

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get telemetry, send command ``{"cmd": 4}``, for example, the answer for az thermostat will be:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "f.0":"1","f.3":"0","f.4":"0","f.7":"0",
      "f.9":"0","f.10":"0","f.11":"0","f.12":"0",
      "f.13":"0","f.16":"0","f.20":"0","m.0":"0",
      "m.1":"0","m.2":"65","m.3":"2","m.5":"0",
      "o.0":"-57","o.1":"1","par.26":"45","par.27":"5",
      "t.0":"470","t.1":"392","t.5":"400","t.7":"640","time":"812112348"
   }

``sn`` - device serial number

``x.n`` is the parameter key, where ``x`` is a group of parameters, ``n`` is the number in the group

``time`` - request time

Parameter groups:
   * ``t`` - temperature is 1/16 °C
      * ``0`` - internal overheating sensor
      * ``1`` - floor
      * ``5`` - current setting
      * ``7`` - microcontroller temperature      
   * ``m`` - modes
      * ``0`` - control type: floor = 0, air (not used in this model) = 1, extended (not used in this model) = 2
      * ``1`` - control type: schedule = 0, manual = 3, away = 4, temporary = 5
      * ``2`` - the number of the current schedule period (the schedule uses all 7 days of the week, each containing up to 16 periods. Accordingly, if the schedule uses all 16 periods every day, the value can range from 0 (representing the first period on Monday) to 111 (representing the last period on Sunday). The example given shows the maximum possible value. There can be fewer periods; for example, if using 2 periods per day, the value range will be from 0 (the first period on Monday) to 13 (the last period on Sunday)
      * ``3`` - blocking type: no blocking = 0, blocking changes from the cloud = 1, blocking changes from the local network = 2, both = 3
      * ``5`` - heating mode (0 - heating, 1 - cooling)
   * ``o`` - other parameters
      * ``0`` - Wi-Fi signal strength in dBm
      * ``1`` - the reason for the last reboot. Depending on the hardware version of the platform, two types of values may be output. The first is a hexadecimal mask, which is read as follows: power-off = 0x04, software reset = 0x08, watchdog timer = 0x10, low voltage = 0x40. The second is a direct value: software reboot due to low MCU supply voltage = 9; software reboot = 3; power reset = 1.
   * ``par`` - duplication of some device `parameters <parameters.html>`_
      * ``n`` - parameter number
   * ``f`` - bit parameters
      * ``0`` - load status: 0 - off, 1 - on
      * ``3`` - no floor sensor: 0 - ok, 1 - no sensor
      * ``4`` - short circuit floor sensor: 0 - no short circuit, 1 - short circuit
      * ``7`` - preheat algorithm is active: 0 - off, 1 - on 
      * ``9`` - internal overheating: 0 - no overheat, 1 - overheat
      * ``10`` - time synchronization issue: 0 - the thermostat's time matches the cloud time; 1 - the thermostat's time does not match the cloud time.
      * ``11`` - time drift issue: 0 - the thermostat's clock is accurate (not lagging); 1 - the thermostat's clock is inaccurate (lagging)
      * ``12`` - overheat protection (internal device temperature sensor circuit): 0 - no error (operating correctly), 1 - error (overheat protection not functioning)
      * ``13`` - load proportional mode (emergency operation mode without floor temperature sensor): 0 - disabled, 1 - enabled
      * ``14`` - digital floor sensor is used: 0 - not used, 1 - used
      * ``16`` - power off state: 0 - on, 1 - off
      * ``20`` - zero-crossing detection circuit error: 0 - no error, 1 - error


