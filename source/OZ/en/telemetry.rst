Telemetry
~~~~~~~~~

Telemetry is used to obtain the current state of device.

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get telemetry, send command ``{"cmd": 4}``, the answer for thermostat will be:

.. code-block:: json 

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "t.0":"482","t.1":"399","t.2":"371","t.5":"368",
      "m.0":"2","m.1":"3","m.2":"1","m.5":"0","m.6":"255",
      "o.0":"-64","o.1":"1","o.5":"0","o.2":"0","o.4":"61",
      "t.7":"692","m.3":"0","f.3":"0","f.4":"0","f.5":"0",
      "f.6":"0","f.8":"0","f.7":"0","f.13":"0","f.0":"0",
      "f.17":"0","f.16":"0","f.9":"0","f.11":"0","f.12":"0",
      "f.20":"0","f.21":"0","f.22":"1","f.23":"0",
      "par.26":"45","par.27":"5","par.33":"35","par.34":"5",
      "time":"799767684","setPointStep":"0.5","setPointType":"3"
   }

``sn`` - device serial number

``x.n`` is the parameter key, where ``x`` is a group of parameters, ``n`` is the number in the group

``time`` - device current time

``setPointStep`` - setpoint step

``setPointType`` - reserved

Parameter groups:
   * ``t`` - temperature is 1/16 °C
      * ``0`` - internal overheating sensor
      * ``1`` - floor
      * ``2`` - air (for devices with an air sensor)
      * ``3`` - reserved
      * ``4`` - reserved
      * ``5`` - current setting
      * ``6`` - reserved
      * ``7`` - microcontroller temperature      
   * ``m`` - modes
      * ``0`` - control type: floor = 0, air = 1, air mode with floor limitation = 2
      * ``1`` - Operation mode: schedule = 0, expectation = 1, manual = 3, away = 4, temporary = 5, timer = 6
      * ``2`` - the number of the current schedule period (the schedule uses all 7 days of the week, each containing up to 16 periods. Accordingly, if the schedule uses all 16 periods every day, the value can range from 0 (representing the first period on Monday) to 111 (representing the last period on Sunday). The example given shows the maximum possible value. There can be fewer periods; for example, if using 2 periods per day, the value range will be from 0 (the first period on Monday) to 13 (the last period on Sunday)
      * ``3`` - blocking type: no blocking = 0, blocking changes from the cloud = 1, blocking changes from the local network = 2, both = 3
      * ``4`` - reserved
      * ``5`` - heating mode (0 - heating, 1 - cooling)
      * ``6`` - next mode — the mode the device will switch to upon exiting the current timer, away, or waiting mode: = scheduled = 0, expectation = 1, manual = 3, away = 4, temporary = 5, timer = 6. For all other modes = 255 (undefined)
   * ``o`` - other parameters
      * ``0`` - Wi-Fi signal strength in dBm (-127..128)
      * ``1`` - the reason for the last reboot: 9 - software reboot due to low MK supply voltage; 3 - software reboot; 1 - power reset.
      * ``2`` - timer remaining (to get the time in seconds, the value must be multiplied by 5)
      * ``4`` - humidity in % (air sensor data)
      * ``5`` - reason for reboot WCH: WCH reset cause: Other reasons = 0, Reset = 3, Software failure = 4
   * ``par`` - duplication of some device parameters
      * ``n`` - parameter number
   * ``te`` - extra temperatures
   * ``f`` - bit parameters
      * ``0`` - load status: 0 - disabled, 1 - enabled
      * ``1`` - reserved
      * ``2`` - floor limit action (for devices with air sensor)
      * ``3`` - floor sensor break: 0 - no break, 1 - break
      * ``4`` - floor sensor short circuit: 0 - no short circuit, 1 - short circuit
      * ``5`` - air sensor loss: 0 - no loss, 1 - loss (for devices with air sensor)
      * ``6`` - reserved
      * ``7`` - preheat function action: 0 - disabled, 1 - enabled
      * ``8`` - open window function action: 0 - disabled, 1 - enabled
      * ``9`` - internal overheating: 0 - no overheating, 1 - overheating
      * ``10`` - time synchronization issue: 0 - thermostat time matches cloud time, 1 - thermostat time doesn't match cloud time
      * ``11`` - time flow issue: 0 - thermostat time counts correctly (not lagging), 1 - thermostat time counts incorrectly (lagging)
      * ``12`` - overheating protection (internal device temperature monitoring circuit): 0 - no error (working correctly), 1 - error (overheating protection not working)
      * ``13`` - proportional load operation mode (emergency operation without floor temperature sensor): 0 - disabled, 1 - enabled
      * ``14`` - digital floor sensor used: 0 - not used, 1 - used
      * ``15`` - reserved
      * ``16`` - device power off: 0 - enabled, 1 - disabled
      * ``17`` - long load operation time: 0 - no notification, 1 - notification present
      * ``18`` - reserved
      * ``19`` - reserved
      * ``20`` - zero-crossing detection circuit error: 0 - no error, 1 - error
      * ``21`` - cloud time ignoring: 0 - not ignoring, 1 - ignoring
      * ``22`` - air sensor connection: 0 - not connected, 1 - connected
      * ``23`` - air sensor battery status: 0 - battery OK, 1 - low battery