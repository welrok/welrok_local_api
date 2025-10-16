**Получение ключа TOTP**
========================

Для безопасного управления устройством с аутентификацией по TOTP протоколу необходимо знать ключ, 
который представляет из себя последовательность из 16 байт. Он генерируется облаком в момент первого 
подключения и при каждой привязке к аккаунту.

Получить его можно только через API сервера в 2 этапа:
   * получить токен авторизации для нужной учетной записи
   * получить список устройств с параметрами, привязанных к данной учетной записи

.. rubric:: **ПОЛУЧЕНИЕ ТОКЕНА АВТОРИЗАЦИИ** 

**POST** https://app.welrok.com/api/login/

.. code-block:: json

   {
      "email":"user@email.com",
      "password":"myPassword"
   }

**Параметры:**
   - **email** - почта зарегистрированного аккаунта
   - **password** - пароль от аккаунта

**Ответ:**

.. code-block:: json

   {
      "access_token":"9573e6a8e24b025fafbaf81dc2eccbc09b94d187",
      "user_name":"welrok",
      "is_timezone_chosen":true
   }

``access_token`` - искомый токен авторизации

**Пример:**

..  code-block:: html

   {
      POST /api/login/ HTTP/1.1
      Host: app.welrok.com
      Accept-Language: en
      Content-Type: application/json
      
      {"email":"demo@welrok.com","password":"demoaccount"}   
   }

.. rubric:: **ПОЛУЧЕНИЕ СПИСКА УСТРОЙСТВ**

**GET** https://app.welrok.com/api/device/ --header «Authorization: Token ``access_token``»

**Параметры**
   - ``access_token`` - токен авторизации в заголовке                 

Ответ:

.. code-block:: json

   {
      "count": 4,
      "next": null,
      "previous": null,
      "results": [
                  {
                     "id": 1,
                     "sn": "404CCAAAD4E8A89860609800000149",
                     "name": "az",
                     "":""
                     "totp_key": "AAD4EXAJX4E8A8XT"
                  }
                 ]
   }

Поле ``totp_key`` в параметрах каждого устройства содержит искомый ключ для генерации TOTP токена.

* Пример:

..  code-block:: HTML

   {
      GET /api/device/ HTTP/1.1
      Host: app.welrok.com
      Accept-Language: en
      Content-Type: application/json
      Authorization: Token 9573e6a8e24b025fafbaf81dc2eccbc09b94d187   
   }