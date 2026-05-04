MS: Telemetry
~~~~~~~~~

Telemetry is used to obtain the current state of device.

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get telemetry, send command ``{"cmd": 4}``, for example, the answer for az thermostat will be:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "m.1":"1","t.0":"850","o.0":"-65","o.1":"1",
      "o.5":"0","t.7":"675","m.3":"0","f.10":"0",
      "f.13":"0","f.0":"0","f.1":"0","f.2":"0",
      "f.20":"0","f.21":"0","time":"825266488"
   }

``sn`` - device serial number

``x.n`` is the parameter key, where ``x`` is a group of parameters, ``n`` is the number in the group

``time`` - device current time

Parameter groups:
   * ``t`` - temperature in 1/16 °C
      * ``0`` - internal overheat sensor
      * ``7`` - MCU temperature
   * ``m`` - modes
      * ``1`` - always sends constant = 1
      * ``3`` - lock type: no locks = 0, cloud changes lock = 1, local network changes lock = 2, both = 3
   * ``o`` - other parameters
      * ``0`` - Wi-Fi signal level in dBm (-127..128)
      * ``1`` - reason for the last reboot. Depending on the hardware platform version, two types of values may be returned. The first is a hexadecimal mask, interpreted as: power off = 0x04, software reset = 0x08, watchdog timer = 0x10, low voltage = 0x40. The second is a direct value: software reboot due to low MCU supply voltage = 9; software reboot = 3; power reset = 1.
      * ``5`` - WCH reboot reason: 0 reboot via NRST pin, 1 via power, 2 software reboot, 3 independent watchdog, 4 window watchdog, 5 brownout
   * ``par`` - duplication of some `parameters <parameters_ru.html>`_ of the device
      * ``n`` - parameter number
   * ``f`` - bit parameters
      * ``0`` - internal overheat: 0 - no overheat: 1 - overheat
      * ``1`` - clock issues: 0 - no error, 1 - error
      * ``2`` - overheat control (internal temperature monitoring circuit of the device): 0 - no error (operates correctly), 1 - error (overheat control not working)
      * ``10`` - load: 0 - relay open, 1 - relay closed
      * ``13`` - time synchronization issue: 0 - device time is synchronized with cloud time 1 - device time is not synchronized with cloud time
      * ``20`` - zero-cross detection circuit error: 0 - no error, 1 - error
      * ``21`` - time from the local network was received less than 24 hours ago: 0 - does not ignore cloud time, 1 - ignores cloud time