Time
~~~~~~~~~~

To retrieve the current time parameters from the device, use the request ``{"cmd": 3}`` `Command <comands.html>`_.

To change the time and time zone on the device, send the following request:

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "time": "634929122",
      "tzone": "3"
   }

``sn`` - device serial number

``time`` - time in seconds since 01.01.2000 00:00

``tzone`` - time zone

To change the time zone without changing the time:

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "tzone": "3"
   }

To change the time without changing the time zone:

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "time": "634929122"
   }

.. note::
   If changes via local network are locked (``lanBlock`` = **1**; ``bLc`` = **Lan**), you must include a TOTP token «auth» (see `Safety <safety.html>`_):

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "time": "634929122",
      "tzone": "time zone",
      "auth": "672201707"
   }

.. important::
   If the time is set with a difference exceeding 24 hours, the telemetry parameter ``f21`` will be reset, and time synchronization with the cloud will be re-established.

When setting the time using a command, synchronization between the device time and the cloud time is stopped. To restore time synchronization, you need to reset the device settings to their default values (see device user manual).

.. note::

   Setting the device time to a value earlier than the current device time may cause a configuration conflict.

   The conflict occurs because if any commands were sent to the device via cloud with timestamps later than the manually set time, new commands will not execute until the device time exceeds the timestamp of the last cloud-processed command.

   Example scenario:
   
      * A command was sent to the cloud-synchronized device at 13:00 real time.
      * At 13:01, the device time is set to 10:01.
      * For 3 hours, no new commands will be processed.
      * At 16:01 real time, when the device reaches 13:01 (which is later than 13:00 when the server recorded the last command), new commands will begin to be accepted and executed.
   
   To prevent this conflict, disable cloud synchronization in advance (see `safety <safety.html>`_).