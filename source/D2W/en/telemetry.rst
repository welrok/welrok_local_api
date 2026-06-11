D2W: Telemetry
==========

Telemetry is used to obtain the current state of the device.

.. Important::
   The ability to control via the local network without a security token is `blocked by default <safety.html>`_ for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the parameter ``bLc`` to the value **oFF**. Otherwise, change requests without this token will not be executed.

To obtain telemetry, send the request ``{"cmd":4}``. Response:

.. code-block:: json

   {
     "deviceId":0,"telemetry":{"u":{"13":245,"14":144,"15":218},
     "t":{"0":576,"7":946},"m":{"1":0,"3":0,"10":0},
     "f":{"0":false,"1":false,"2":false,"3":false,"4":true,"5":true,
     "6":false,"10":true,"12":false,"13":false,"14":false,"15":false},
     "o":{"0":-58},"ts":834392219}
   }

``x.n`` — parameter key, where ``x`` is the parameter group, ``n`` is the number in the group

``ts`` — current device time

Parameter groups:
   * ``u`` — voltage in volts
      * ``13`` — upper voltage threshold
      * ``14`` — lower voltage threshold
      * ``15`` — voltage averaged over the last 0.5 seconds
   * ``t`` — temperature in 1/16°C
      * ``0`` — internal overheating sensor
      * ``7`` — microcontroller temperature
   * ``m`` — modes
      * ``1`` — device status: 0 — on, 1 — off via button
      * ``3`` — lock type: no locks = 0, cloud change lock = 1, local network change lock = 2, both = 3
      * ``10`` — remaining time until load activation in seconds
   * ``f`` — bit parameters
      * ``0`` — internal overheating: false — no overheating, true — overheating
      * ``1`` — clock issues: false — no error, true — error
      * ``2`` — overheating monitoring (circuit of the internal temperature sensor of the device): false — no error (working correctly), true — error (overheating monitoring is not working)
      * ``3`` — period of the last time request: true — if less than 24 hours have passed since receiving the time via API, otherwise — 0
      * ``4`` — the ability to remotely force load shutdown via the Welrok app for iOS / Android: true — possible, false — not possible
      * ``5`` — reserved
      * ``6`` — fifth overheating lock: true — locked, false — not locked
      * ``10`` — relay status: false — relay open, true — relay closed
      * ``12`` — REP lock: false — no lock, true — lock
      * ``13`` — flag indicating an incident during the telemetry period: false — no incident, true — incident
      * ``14`` — incident — high voltage: false — no incident, true — incident
      * ``15`` — incident — low voltage: false — no incident, true — incident
   * ``o`` — other parameters
      * ``0`` — Wi‑Fi signal level in dBm (−127..128)