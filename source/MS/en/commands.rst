MS: commands
~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

The ``cmd`` key is used to get or reset device parameters, schedules, time, and telemetry.
Possible values:

   * 1 - `parameters <parameters.html>`_ request
   * 2 -  time getting request
   * 3 - `telemetry <telemetry.html>`_ request

 
Example ``{"cmd":1}``

`Parameters <parameters.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "par":[[68,2,"0"],[125,7,"0"],[70,2,"2"],
      [71,2,"0"],[3,2,"0"],[23,2,"10"],[55,2,"24"],
      [114,7,"0"],[115,7,"0"],[124,7,"0"]]
   }

Example ``{"cmd":3}``

Time getting request

Answer: 

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "time":"825266448", "tzone":"3"}
   }

Where ``time`` - time in seconds from 01.01.2000 00:00

Example ``{"cmd":4}``

`Telemetry <telemetry.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "m.1":"1","t.0":"850","o.0":"-65","o.1":"1",
      "o.5":"0","t.7":"675","m.3":"0","f.10":"0",
      "f.13":"0","f.0":"0","f.1":"0","f.2":"0",
      "f.20":"0","f.21":"0","time":"825266488"
   }

.. toctree::
   :maxdepth: 1
   :caption: Подразделы команд:
   
   Parameters <parameters>
   Schedule <schedule>
   Telemetry <telemetry>
   Working with time <time>
