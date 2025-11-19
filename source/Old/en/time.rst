Time
~~~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To retrieve the current time parameters from the device, use the request ``{"cmd": 3}`` `Command <comands.html>`_.

To change the time on the device, send the following request:

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "time": "634929122"
   }

``sn`` - device serial number

``time`` - time in seconds since 01.01.2000 00:00

.. note::
   If changes via local network are locked (``lanBlock`` = **1**; ``bLc`` = **Lan**), you must include a TOTP token «auth» (see `Safety <safety.html>`_):

.. code-block:: json

   {
      "sn": "404CCAAAD4E8A89860609800000149",
      "time": "634929122",
      "auth": "672201707"
   }

When setting the time via command, the time synchronization between the device and the cloud is disabled. To restore time synchronization, reset the device to factory defaults (refer to the device manual).

.. note::

   Setting the device time to a value earlier than the current device time may cause a configuration conflict.

   The conflict occurs because if any commands were sent to the device via cloud with timestamps later than the manually set time, new commands will not execute until the device time exceeds the timestamp of the last cloud-processed command.

   Example scenario:
   
      * A command was sent to the cloud-synchronized device at 13:00 real time.
      * At 13:01, the device time is set to 10:01.
      * For 3 hours, no new commands will be processed.
      * At 16:01 real time, when the device reaches 13:01 (which is later than 13:00 when the server recorded the last command), new commands will begin to be accepted and executed.
   
   To prevent this conflict, disable cloud synchronization in advance (see `safety <safety.html>`_).