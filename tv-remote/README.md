# Control remoto Samsung UN55MU6100

Servidor Python + página web para el celular. Corre en un equipo de tu red (PC, Raspberry Pi, etc.).

## Instalación
1. `pip install -r requirements.txt`
2. Edita `config.json`: `tv_ip`, `tv_mac` (TV > Configuración > Soporte > Acerca de) y tus apps/macros.
3. En la TV: Configuración > General > Administrador de dispositivos externos > **Administrador de conexión de dispositivo** > Configuración de acceso: *Aceptar*.
4. `python3 server.py` (o `--mock` para probar sin TV).
5. En el celular (mismo Wi-Fi) abre `http://IP_DEL_EQUIPO:8080`. La primera vez la TV pedirá **Permitir**; el token queda en `token.txt`.
6. Menú del navegador > "Añadir a pantalla de inicio".

## Encender la TV
Usa Wake-on-LAN: en la TV activa Configuración > General > Red > Configuración de experto > **Encendido con Wi-Fi/LAN**. Funciona mejor con cable Ethernet.

## Macros
En `config.json`, cada paso puede ser `{"key":"KEY_..."}` (con `"repeat"`), `{"wait": segundos}` o `{"app":"id"}`.
