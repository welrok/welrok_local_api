**MQTT**
========

There's a possibility to collect telemetry and manage some parameters via MQTT protocol.
MQTT server connection settings are available only via the device web-interface, which is available at its local IP address:

``Host``/``Port`` - IP address and port of the MQTT server

``User``/``Password`` - username and password to connect

``Keep alive`` - the maximum allowed period of time without data exchange

``QoS`` - quality of service level

``Publish prefix`` - publication prefix for sending telemetry

``Subscribe path`` - name of the way to subscribe to commands

``Client ID`` - device name

.. note::
   If no authorization is configured on the MQTT server, the ``User``/ ``Password`` fields are ignored.

.. important::
   The maximum length of the ``User`` name and ``Password`` is 30 characters

.. rubric:: **PUBLISHED TOPICS**

Published every minute with an interval of +/- 5 seconds in the following topics:

``Publish prefix``/``Client ID``/``get``/``floorTemp`` - floor temperature sensor readings, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.1"**. Returns in °C as "xx.x" string

``Publish prefix``/``Client ID``/``get``/``protTemp`` - internal overheating sensor readings, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.0"**. Returns in °C as "xx.x" string.

``Publish prefix``/``Client ID``/``get``/``setTemp`` - setpoint temperature, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.5"**. Returns in °C as "xx.x" string.

``Publish prefix``/``Client ID``/``get``/``powerOff`` - device power off status, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"f.16"**. Returns as string where "0" - enabled, "1" - disabled.

``Publish prefix``/``Client ID``/``get``/``load`` - load status, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"f.0"**. Returns as string where "0" - disabled, "1" - enabled.

``Publish prefix``/``Client ID``/``get``/``bright`` - current thermostat display brightness, read similarly to `parameters <parameters.html>`_ requested via API with ``{"cmd":1}`` command.

.. rubric:: **CONTROL TOPICS**

The following topics are available for control:

.. note:: 
   After sending a control command, an out-of-turn data publication occurs after 3-5 seconds.

``Subscribe path``/``Client ID``/``set``/``setTemp`` - setpoint temperature setting. Passed as string in "xx" format.

``Subscribe path``/``Client ID``/``set``/``bright`` - display brightness. Passed as string in "x" format. Values from 0 to 9.

``Subscribe path``/``Client ID``/``set``/``powerOff`` - device power off. Passed as string in "x" format. Values 0 or 1, where 0 - enabled, 1 - disabled.

``Subscribe path``/``Client ID``/``set``/``mode`` - operation mode selection. Passed as string in "x" format. Values 0 or 1, where 0 - schedule, 3 - manual.

.. note::
   The floor temperature sensor in the device user menu and via API/MQTT changes with 1 °C step throughout the entire operating range