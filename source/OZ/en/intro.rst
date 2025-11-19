Introduction
~~~~~~~~~~~~

For Wi-Fi devices direct control via a local network is available. Information is exchanged through POST requests at http://``dev_ip``/api.cgi, where ``dev_ip`` is the ip address of the device on the local network. To detect new devices on the local network `broadcast <broadcast.html>`_ packets is used. Data is presented in JSON format.

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

JSON keys are available:

``sn`` - the serial number of the device, required when transferring new data into device.

``cmd`` - `send command <comands.html>`_ to receive data from the device (`parameters <parameters.html>`_, `schedule <schedule.html>`_, `telemetry <telemetry.html>`_)

``par`` - `change device parameters <parameters.html>`_

``tt`` - `transfer new schedule <schedule.html>`_

``ttAir`` - `transfer new schedule <schedule.html>`_ for air control (air with floor restriction), for devices with an air sensor

``time``, ``auth`` - `authentication  <safety.html>`_

.. Important::
   It is impossible to transfer the schedule and parameters in one request, as well as several days of the schedule.

.. note::
   The device has a page at http://``dev_ip``/index.html, where the function for connecting the device to the cloud ``API`` ``CLOUD`` is available. If the ``CLOUD`` item is enabled, the device's connection to the cloud is active. If the ``CLOUD`` item is disabled, the device has no connection to the cloud. When the connection to the cloud is disabled, no data is guaranteed to be transmitted to the cloud. However, this also means the device's time is not synchronized with the cloud. The page is also accessible when the device operates in access point mode. To do this, switch the device to "AP" mode, connect to it, and go to: http://192.168.0.1/index.html