D2W: List of parameters
~~~~~~~~~~~~~~~~~

.. Important::
   The ability to control via the local network without a security token is `blocked by default <safety_ru.html>`_ for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the parameter ``bLc`` to the value **oFF**. Otherwise, change requests without this token will not be executed.

To obtain a set of all available parameters for a specific device, send the request ``{"cmd":1}``. For example, the response for the D2W device:

.. code-block:: json

   {
      "deviceId":0,"par":{"1":245,"5":144,"9":3,
      "14":-8,"20":3,"19":3,"13":1,"73":5,
      "124":false,"125":true,"126":false,"119":false,
      "118":true,"117":true,"116":false,"114":false,
      "115":false,"ts":1781076688}
   }

``par`` — parameter exchange key
``deviceId`` - is always 0

The transmission format is an array of arrays. The first number is the parameter number, the second is its type, the third is a string with the parameter value.

For example, to turn on the device relay:

.. code-block:: json

   {
      "deviceId":0,
      "par":[["119":true]]
   }

Response:
We receive an updated list of all parameters in response:

.. code-block:: json

   {
      "deviceId":0,"par":{"1":245,"5":144,"9":3,
      "14":-8,"20":3,"19":3,"13":1,"73":5,
      "124":false,"125":true,"126":false,"119":true,
      "118":true,"117":true,"116":false,"114":false,
      "115":false,"ts":1781076688}
   }

.. important::
   When changing device parameters, the command must contain the key ``"deviceId":0"``

.. table:: **List of parameters**
   :widths: auto
   
   ======   =============  =======================    =========================================================================================================================
   Num      Type           Name                       Description
   ======   =============  =======================    =========================================================================================================================
   1        (uint16)       upperU                     in volts, upper voltage limit (from 230 to 280)
   5        (uint8)        lowerU                     in volts, lower voltage limit (from 100 to 210)
   9        (uint16)       tonDelay                   in seconds, relay activation delay (from 3 to 999)
   13       (uint32)       lowVoltageTime             in seconds, voltage drop duration (from 0.1 to 10)
   14       (int8)         correctionU                in volts, voltage correction (from -20 to 20)
   19       (uint8)        repTimes                   protection against frequent activations (from 1 to 5)
   20       (uint8)        voltageHysteresis          in volts, voltage hysteresis (from 0 to 5)
   73       (uint8)        brightness                 in arbitrary units, indicator brightness in standby mode (from 0 to 10)
   114      (bool)         lanBlock                   blocking any setting changes via API: false — disabled, true — enabled
   115      (bool)         cloudBlock                 blocking any setting changes and firmware updates via the cloud: false — disabled, true — enabled
   116      (bool)         modeGen                    generator compatibility mode: false — disabled, true — enabled
   117      (bool)         repON                      use of protection against repeated activations (REP): false — disabled, true — enabled
   118      (bool)         easyPowerOff               ability to manually turn off via the widget: false — disabled, true — enabled
   119      (bool)         powerOff                   device is off: false — on, true — off
   124      (bool)         modePro                    "Pro" mode: false — disabled, true — enabled
   125      (bool)         DelayOnType                "Odt" — delay‑on activation model: false — tAo, true — tAr
   126      (bool)         childrenLock               button lock to prevent parameter changes: false — disabled, true — enabled
   ======   =============  =======================    =========================================================================================================================