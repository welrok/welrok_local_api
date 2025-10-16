Introduction
~~~~~~~~~~~~

For Wi-Fi devices direct control via a local network is available. Information is exchanged through POST requests at http://``dev_ip``/api.cgi, where ``dev_ip`` is the ip address of the device on the local network. To detect new devices on the local network `broadcast <broadcast.html>`_ packets is used. Data is presented in JSON format.

.. Important::
   The ability to control device via local network without authentification by default `blocked <safety.html>`_ for security reasons.

JSON keys are available:

``sn`` - the serial number of the device, required when transferring new data into device.

``cmd`` - `send command <comands.html>`_ to receive data from the device (`parameters <parameters.html>`_, `schedule <schedule.html>`_, `telemetry <telemetry.html>`_)

``par`` - `change device parameters <parameters.html>`_

``tt`` - `transfer new schedule <schedule.html>`_

``time``, ``auth`` - `authentication  <safety.html>`_

.. Important::
   It is impossible to transfer the schedule and parameters in one request, as well as several days of the schedule.

.. note::
   The device has a page at http:// dev_ip /api.html, where dev_ip is the device's IP address on the local network. This page allows you to verify the correctness of requests and test the communication protocol. 
   The API control function is also available when the device is operating in the "Access Point" thermostat mode. To do this, switch the device to "AP" mode, as described in the device's manual, connect to it, and go to: http://192.168.0.1/api.html
