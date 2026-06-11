D2W: commands
~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

The ``cmd`` key is used to get or reset device parameters, schedules, time, and telemetry.
Possible values:

   * 1 - `parameters <parameters.html>`_ request
   * 3 -  time getting request
   * 4 - `telemetry <telemetry.html>`_ request

 
Example ``{"cmd":1}``

`Parameters <parameters.html>`_ request

Answer:

.. code-block:: json

   {
      "deviceId":0,"par":{"1":245,"5":144,"9":3,
      "14":-8,"20":3,"19":3,"13":1,"73":5,
      "124":false,"125":true,"126":false,"119":true,
      "118":true,"117":true,"116":false,"114":false,
      "115":false,"ts":1781076688}
   }

Example ``{"cmd":3}``

Time getting request

Answer: 

.. code-block:: json

   {"deviceId":0,"time":834401814}

Where ``time`` - time in seconds from 01.01.2000 00:00 in UTC

Example ``{"cmd":4}``

`Telemetry <telemetry.html>`_ request

Answer:

.. code-block:: json

   {
     "deviceId":0,"telemetry":{"u":{"13":245,"14":144,"15":218},
     "t":{"0":576,"7":946},"m":{"1":0,"3":0,"10":0},
     "f":{"0":false,"1":false,"2":false,"3":false,"4":true,"5":true,
     "6":false,"10":true,"12":false,"13":false,"14":false,"15":false},
     "o":{"0":-58},"ts":834392219}
   }

.. toctree::
   :maxdepth: 1
   :caption: Подразделы команд:
   
   Parameters <parameters>
   Schedule <schedule>
   Telemetry <telemetry>
   Working with time <time>
