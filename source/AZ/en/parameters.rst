Parameters list
~~~~~~~~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get all available parameters of the device send command ``{"cmd":1}``, for example answer for *az* thermostat:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[0,6,"536112000"],[1,6,"536112000"],
            [2,2,"1"],[3,2,"0"],[5,1,"30"],
            [7,1,"5"],[17,4,"175"],[18,2,"2"],
            [19,2,"10"],[21,1,"0"],[23,2,"6"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],
            [28,2,"16"],[29,1,"0"],[31,1,"8"],
            [52,4,"0"],[53,4,"480"],[55,2,"24"],
            [109,7,"0"],[114,7,"1"],[115,7,"0"],
            [117,7,"0"],[118,7,"0"],[120,7,"0"],
            [121,7,"0"],[124,7,"0"],[125,7,"0"]]
   }

``sn`` - device serial number

``par`` - parameter exchange key

Transfer format is an array of arrays. The first value is number of the parameter, the second its type, the third is string with the parameter value.

For example, turn on the device and set floor temperature in manual mode to 27 °C (device menu item ``bLc`` = 0FF, blocking is disabled):

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[125,7,"0"],[5,1,"27"]]
   }

Answer:

In response, we receive an updated list of parameters:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[0,6,"536112000"],[1,6,"536112000"],
            [2,2,"1"],[3,2,"0"],[5,1,"27"],
            [7,1,"5"],[17,4,"175"],[18,2,"2"],
            [19,2,"10"],[21,1,"0"],[23,2,"6"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],
            [28,2,"16"],[29,1,"0"],[31,1,"8"],
            [52,4,"0"],[53,4,"480"],[55,2,"24"],
            [109,7,"0"],[114,7,"1"],[115,7,"0"],
            [117,7,"0"],[118,7,"0"],[120,7,"0"],
            [121,7,"0"],[124,7,"0"],[125,7,"0"]]
   }

.. note::
   The floor sensor temperature in the user menu and via API can be changed in 1 °C increments over the entire operating range.

.. important::
   When changing device parameters, the command must contain the key ``sn``

.. table:: **Data types**
   :widths: auto   

   === =====
   Num Type
   === =====
   0   CStringType
   1   int8
   2   uint8
   3   int16
   4   uint16
   5   int32
   6   uint32
   7   bool
   === =====


.. table:: **Parameters list**
   :widths: auto

   ======   ==============  =======================    =========================================================================================================================
   Num      Type            Name                       Description
   ======   ==============  =======================    =========================================================================================================================
   0        6(uint32)       startAwayTime              in seconds from 01.01.2000, away start time
   1        6(uint32)       endAwayTime                in seconds from 01.01.2000, away end time
   2        2(uint8)        mode                       mode: schedule=0, manual=3
   3        2(uint8)        controlType                control tupe: by floor=0
   5        1(int8)         manualFloorTemperature     in °C, manual mode temperature by floor
   6        1(int8)         awayAirTemperature         in °C, temperature mode away by air
   7        1(int8)         awayFloorTemperature       in °C, temperature mode away by floor
   17       4(uint16)       power                      in a.e., If the «Р» is less than or equal to 150, then P = power * 10. If the «Р» is greater than 150, then P = power * 20 - 1500. As a result, we get the specified connected power in Watts.
   18       2(uint8)        sensorType                 type of connected temperature sensor: 4,7kOhm=0, 6,8kOhm=1, 10kOhm=2, 12kOhm=3, 15kOhm=4, 33kOhm=5, 47kOhm=6
   19       2(uint8)        histeresis                 in °C*10, hysteresis
   21       1(int8)         floorCorrection            in °C*10, floor temperature sensor correction
   23       2(uint8)        brightness                 in a.e. (from 0 to 9) brightness 
   25       2(uint8)        propKoef                   in minutes when load on within 30-minutes cycle of the proportional mode
   26       1(int8)         upperLimit                 in °C, max setting value of the floor temperature
   27       1(int8)         lowerLimit                 in °C, min setting value of the floor temperature
   28       2(uint8)        maxSchedulePeriod          max number of perioods per day. Read Only 
   29       1(int8)         tempTemperature            in °C, temporary mode temperature
   31       1(int8)         setTemperature             in °C, setting temperature of current mode (awayFloorTemperature | manualFloorTemperature | tempTemperature)
   52       4(uint16)       nightBrightStart           in minutes from 00:00, night low bright start time
   53       4(uint16)       nightBrightEnd             in minutes from 00:00, night low bright end time
   55       2(uint8)        relayOnTimeLimit           in hours, continuous heating time for emergency alert (Read-only)
   109      7(bool)         offButtonLock              disable automatic lock of touch buttons (Read-only)   
   114      7(bool)         lanBlock                   local newort control block: 0 - disabled, 1 - enabled
   115      7(bool)         cloudBlock                 cloud control block: 0 - disabled, 1 - enabled
   117      7(bool)         NCContactControl           inverted relay: 0 - disabled, 1 - enabled
   118      7(bool)         coolingControlWay          mode: 0 - heating, 1 - cooling
   120      7(bool)         useNightBright             activate using night bright: 0 - disabled, 1 - enabled
   121      7(bool)         preControl                 preheat: 0 - disabled, 1 - enabled
   124      7(bool)         childrenLock               children protect: 0 - disabled, 1 - enabled
   125      7(bool)         powerOff                   power off: 0 - enabled, 1 - disabled
   ======   ==============  =======================    =========================================================================================================================

.. note::
   Setpoints for all modes must fit within limits for parameters 26 and 27