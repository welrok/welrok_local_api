Schedule
~~~~~~~~

To get all schedule of the device send command ``{"cmd":2}``. Answer:

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

``tt`` - schedule exchange key 

``0``, ``1``, ``2``, ``3``, ``4``, ``5``, ``6`` - day number key, 0-monday. 

A two-dimensional array with a minimum of one period is used as the argument. The maximum number of periods is set by the parameter maxSchedulePeriod, which is always 16.

Each period consists of pair of values:
  * Number of minutes from the start of the day
  * Temperature in degrees (*10)

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
   It is not allowed to send schedules for multiple days in a single request.

.. note::
   The temperature cannot be greater than parameter 26 (upperLimit) or less than parameter 27 (lowerLimit)


