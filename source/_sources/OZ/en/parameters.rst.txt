Parameters list
~~~~~~~~~~~~~~~

To get all available parameters of the device send command ``{"cmd":1}``, for example answer for *oz* thermostat:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[64,6,"0"],[65,3,"300"],[23,2,"10"],
            [114,7,"0"],[115,7,"0"],[29,3,"0"],
            [66,6,"0"],[67,6,"0"],[0,6,"0"],[1,6,"0"],
            [2,2,"1"],[31,3,"230"],[3,2,"2"],[19,2,"10"],
            [18,2,"2"],[21,1,"0"],[5,3,"300"],[7,3,"50"],
            [109,7,"1"],[80,1,"0"],[81,1,"0"],[82,1,"0"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],[33,1,"35"],
            [34,1,"5"],[28,2,"16"],[17,4,"0"],[52,4,"0"],
            [53,4,"480"],[62,1,"35"],[63,1,"5"],[55,2,"24"],
            [20,1,"0"],[4,3,"230"],[6,3,"180"],[14,1,"0"],
            [15,1,"45"],[122,7,"0"],[35,2,"1"],[36,7,"1"],
            [117,7,"0"],[118,7,"0"],[121,7,"0"],[124,7,"0"],
            [125,7,"0"],[120,7,"0"]]
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
      "par":[[64,6,"0"],[65,3,"300"],[23,2,"10"],
            [114,7,"0"],[115,7,"0"],[29,3,"0"],
            [66,6,"0"],[67,6,"0"],[0,6,"0"],[1,6,"0"],
            [2,2,"1"],[31,3,"230"],[3,2,"2"],[19,2,"10"],
            [18,2,"2"],[21,1,"0"],[5,3,"300"],[7,3,"50"],
            [109,7,"1"],[80,1,"0"],[81,1,"0"],[82,1,"0"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],[33,1,"35"],
            [34,1,"5"],[28,2,"16"],[17,4,"0"],[52,4,"0"],
            [53,4,"480"],[62,1,"35"],[63,1,"5"],[55,2,"24"],
            [20,1,"0"],[4,3,"230"],[6,3,"180"],[14,1,"0"],
            [15,1,"45"],[122,7,"0"],[35,2,"1"],[36,7,"1"],
            [117,7,"0"],[118,7,"0"],[121,7,"0"],[124,7,"0"],
            [125,7,"0"],[120,7,"0"]]
   }

.. note::
   The floor sensor temperature in the device's user menu and via API changes in 1 °C increments over the entire operating range. The air sensor temperature in the device's user menu changes in 1 °C increments in the range from -15 °C to -10 °C, in 0.5 °C increments in the range from -10 °C to 75 °C (for devices with an air sensor). The air sensor temperature when controlled via API changes in 0.1 °C increments over the entire operating range.

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
   
   ======   ===========  =======================    =========================================================================================================================
   Num      Type         Name                       Description
   ======   ===========  =======================    =========================================================================================================================
   0        6(uint32)    startAwayTime              in seconds from 01.01.2000, away start time
   1        6(uint32)    endAwayTime                in seconds from 01.01.2000, away end time
   2        2(uint8)     mode                       mode: schedule=0, manual=1
   3        2(uint8)     controlType                control tupe: by floor=0, by air=1, air mode with floor limitation=2 
   4        3(int16)     manualAir                  in °C*10, manual mode setpoint for air (for devices with an air sensor)
   5        3(int16)     manualFloorTemperature     in °C*10, manual mode temperature by floor
   6        3(int16)     awayAirTemperature         in °C*10, temperature mode away by air
   7        3(int16)     awayFloorTemperature       in °C*10, temperature mode away by floor
   14       2(uint8)     minTempAdvancedMode        in °C, minimum floor temperature limitation in air mode with floor limitation
   15       2(uint8)     maxTempAdvancedMode        in °C, maximum floor temperature limitation in air mode with floor limitation
   17       4(uint16)    power                      in a.e., If the «Р» is less than or equal to 150, then P = power * 10. If the «Р» is greater than 150, then P = power * 20 - 1500. As a result, we get the specified connected power in Watts.
   18       2(uint8)     sensorType                 type of connected temperature sensor: 4,7kOhm=0, 6,8kOhm=1, 10kOhm=2, 12kOhm=3, 15kOhm=4, 33kOhm=5, 47kOhm=6
   19       2(uint8)     histeresis                 in °C*10, hysteresis
   20       1(int8)      airCorrection              in °C*10, air temperature sensor correction
   21       1(int8)      floorCorrection            in °C*10, floor temperature sensor correction
   23       2(uint8)     brightness                 in a.e. from 0 to 10 brightness 
   25       2(uint8)     propKoef                   in minutes when load on within 30-minutes cycle of the proportional mode
   26       1(int8)      upperLimit                 in °C, max setting value of the floor temperature
   27       1(int8)      lowerLimit                 in °C, min setting value of the floor temperature
   28       2(uint8)     maxSchedulePeriod          max number of perioods per day. (Read Only) 
   29       3(int16)     tempTemperature            in °C*10, temporary mode temperature
   31       3(int16)     setTemperature             in °C*10, setting temperature of current mode (awayFloorTemperature | manualFloorTemperature | tempTemperature)
   33       1(int8)      upperAirLimit              in °C, max setting value of the air temperature
   34       1(int8)      lowerAirLimit              in °C, min setting value of the air temperature
   35       2(uint8)     bleSensorInterval          in minutes, air sensor polling frequency (1-60)
   36       7(bool)      bleSensorsBind             wireless air sensor connected (Read-only): 0 - not connected, 1 - connected
   52       4(uint16)    nightBrightStart           in minutes from 00:00, night low bright start time
   53       4(uint16)    nightBrightEnd             in minutes from 00:00, night low bright end time
   55       2(uint8)     relayOnTimeLimit           in hours, continuous heating time for emergency alert (Read-only)
   62       1(int8)      upperWarningTemp           in °C, upper temperature threshold for alarm
   63       1(int8)      lowerWarningTemp           in °C, lower temperature threshold for alarm
   64       6(uint32)    timerPeriod                n seconds from 01.01.2000 00:00, time of end of timer (in UTC)
   65       3(int16)     timerTemperature           in °C*10, timer mode temperature setting
   66       6(uint32)    startAwayTimeUTC           in seconds from 01.01.2000 00:00, departure start time (in UTC)
   67       6(uint32)    endAwayTimeUTC             in seconds from 01.01.2000 00:00, departure end time (in UTC)
   109      7(bool)      offButtonLock              disable automatic lock of touch buttons (Read-only): 0 - locking active, 1 - locking disabled   
   114      7(bool)      lanBlock                   local newort control block: 0 - disabled, 1 - enabled
   115      7(bool)      cloudBlock                 cloud control block: 0 - disabled, 1 - enabled
   117      7(bool)      NCContactControl           inverted relay: 0 - disabled, 1 - enabled
   118      7(bool)      coolingControlWay          heat/cool mode: 0 - heating, 1 - cooling
   120      7(bool)      useNightBright             activate using night bright: 0 - disabled, 1 - enabled
   121      7(bool)      preControl                 preheat: 0 - disabled, 1 - enabled
   122      7(bool)      windowOpenControl          open window control: 0 - disabled, 1 - enabled
   124      7(bool)      childrenLock               children protect: 0 - disabled, 1 - enabled
   125      7(bool)      powerOff                   power off: 0 - enabled, 1 - disabled
   ======   ===========  =======================    =========================================================================================================================

.. note::
   Parameters 29 and 31, in scheduled and timed operation modes, can take the values 127 and -127, which correspond to the setting values **on** (the load is always on) and **off** (the load is always off) in the graphical interface and on the device display.

.. note::
   Setpoints for all modes must fit within limits for parameters 26 and 27 during floor operation, and within limits for parameters 33 and 34 during air operation.