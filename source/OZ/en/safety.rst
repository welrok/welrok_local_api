Safety
~~~~~~

Possibility of device control with enabled ``LAn`` locking (`Parameter <parameters.html>`_ 114 ``lanBlock`` = **1**; in the thermostat menu, the ``bLc`` = **Lan**).

.. note::
   If both locks are tuned on (`Parameter <parameters.html>`_ 114 ``lanBlock`` = **1**, 115 ``cloudBlock`` = **1**; in the thermostat menu, the ``bLc`` = **on**) device is locked for any control by network. Only buttons can change device parameters.

TOTP protocol is used for source authentication when sending commands to the device (**rfc4226**, **rfc6238**, Interval = 30 second, Digit = 9). 
For this purpose it is necessary to add two fields in front of the data fields:

``time`` - time in seconds from 01.01.2000 00:00

``auth`` - calculated token.

For example, the command to turn on the device, set the brightness to 1, and enable API lock would be:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "time":"634929122",
      "auth":"672201707",
      "par":[[125,7,"0"], [23,2,"1"], [114,7,"1"]]
   }

The key for token generation can be obtained through `Server API <keyGet.html>`_.

If you don't need to use authentication, or if you are using software version 2.3, you must disable ``LAn`` locking (``lanBlock`` = **0**).

You can view the lock status as ``m.3`` key in the telemetry or ``lanBlock`` parameter in the parameters or in the menu item ``bLc``.

The blocking is disabled through the device menu - the ``bLc`` parameter must be changed to **oFF**.

.. note::
   Use short presses of the middle button to navigate to the ``bLc`` menu section, then use the ``+`` and ``-`` selection buttons to change the value to **oFF** (see the device manual).

.. note::
   The device has a web interface at http://``dev_ip``/index.html where the ``CLOUD`` connection setting is available. When ``CLOUD`` is enabled, the device maintains active connection to the cloud API. When ``CLOUD`` is disabled, the device has no cloud connectivity. Disabling cloud connection ensures no data is transmitted to the cloud. However, this also disables time synchronization between the device and cloud servers.
   
   This page is also accessible when the device operates in access point mode. To access it, switch the device to "AP" mode, connect to its network, and navigate to: http://192.168.0.1/index.html