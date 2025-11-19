Расписание
~~~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get all schedule of the device send command ``{"cmd":2}`` - for floor control, or ``{"cmd":10}`` - for air and advanced mode control (for devices with an air sensor). For example answer for *oz* thermostat:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "tt":{
            "0":[[360,300],[480,250],[1020,300],[1320,250]],
            "1":[[360,300],[480,250],[1020,300],[1320,250]],
            "2":[[360,300],[480,250],[1020,300],[1320,250]],
            "3":[[360,300],[480,250],[1020,300],[1320,250]],
            "4":[[360,300],[480,250],[1020,300],[1320,250]],
            "5":[[480,300],[1380,250]],
            "6":[[480,300],[1380,250]]
           }
   }

``sn`` - device serial number

``tt`` - schedule exchange key for control type "By floor", ``ttAir`` - schedule exchange key for control type "By air" or "By air with floor limit".

``0``, ``1``, ``2``, ``3``, ``4``, ``5``, ``6`` - ключ номера дня недели, 0-понедельник. 

A two-dimensional array with at least one period is used as an argument. The maximum number of periods for one day is set by the ``maxSchedulePeriod`` parameter always=16.

Each period consists of pairs of values:
  * number of minutes since the beginning of the day
  * temperature in degrees (*10)

The schedule logic is as follows:
  * A single day can have no more than 16 time periods.
  * The start of the next period is the end time of the previous one.

For example, set two periods on Wednesday: 8:00 -> 28 °C, 18:00 -> 18 °C:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "tt":{
            "2":[[480,280],[1080,180]]
           }
   }

In this case, if we did not manually set the schedule for Tuesday, then:
  * From the start of the last period on Tuesday (in the factory settings, the last period on Tuesday starts at 1320 minutes and maintains a temperature of 25°C) until minute 480 on Wednesday, a temperature of +25°C will be maintained.
  * From minute 480 to minute 1080 on Wednesday, the temperature will be maintained at 28°C.
  * From minute 1080 until the start of the next period on Thursday, a temperature of +18°C will be maintained.

.. important::
   It is impossible to transfer several days of the schedule in one request.

.. note::
   The temperature cannot be greater than parameter 26 (upperLimit), less than parameter 27 (lowerLimit) for the floor and greater than parameter 33 (upperAirLimit), less than parameter 34 (lowerAirLimit) for the air (for devices with an air sensor).

.. note::
   Parameters 29 and 31, in scheduled and timed operation modes, can take the values 127 and -127, which correspond to the setting values **on** (the load is always on) and **off** (the load is always off) in the graphical interface and on the device display.