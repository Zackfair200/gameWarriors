Crear un entorno local para realizar todo tipo de pruebas tanto de codigo como la instalacion de nuevas dependencias.
.-Las dependencias instaladas no salen del entorno manteniendo tu maquina limpia
.-Al crear el nuevo entorno ya dispone del instalador de dependencias de su lenguaje, por ejemplo, en un entorno python ya dispone de pip

////***COMANDOS DE USO BÁSICO***////
Crear nuevos entorno para pruebas: virtualenv -p nombreLenguaje nombreEntorno ----- (ejemplo: virtualenv -p python test-env)
Acceder al entorno de pruebas: .\nombreEntorno\Scripts\activate ----- (ejemplo: .\test-env\Scripts\activate)
Salir del entorno de pruebas: deactivate