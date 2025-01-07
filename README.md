
![image](https://github.com/user-attachments/assets/165f4f1e-a993-4f4b-9c71-b52484f47654)

Hydra Brute Force Script
Este script utiliza Hydra para realizar un ataque de fuerza bruta a un formulario web mediante el protocolo HTTP POST. La herramienta probará combinaciones de nombres de usuario y contraseñas hasta encontrar una coincidencia válida.

Comando
bash
Copiar código
hydra -l jose -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong password. Please try again." -f -q
Explicación de cada componente
1. hydra
Descripción: Ejecuta la herramienta Hydra, utilizada para realizar ataques de fuerza bruta contra diferentes protocolos y servicios.
2. -l jose
Descripción: Especifica un único nombre de usuario, en este caso jose, que se utilizará durante el ataque.
Alternativa: Si deseas probar múltiples nombres de usuario, puedes usar -L con un archivo de lista:
bash
Copiar código
-L userlist.txt
3. -P /usr/share/wordlists/rockyou.txt
Descripción: Especifica el archivo de contraseñas, rockyou.txt, que Hydra usará para probar las posibles contraseñas.
Nota: Si no tienes rockyou.txt, puedes instalarlo o descargarlo:
bash
Copiar código
sudo apt install wordlists
4. lookup.thm
Descripción: Es el dominio o la dirección IP del servidor objetivo al que se enviarán las solicitudes de inicio de sesión.
5. http-post-form
Descripción: Indica que Hydra atacará un formulario web utilizando el método HTTP POST.
Uso común: También puedes usar otros módulos de Hydra, como FTP o SSH, pero en este caso estamos atacando un formulario web.
6. "/login.php:username=^USER^&password=^PASS^:Wrong password. Please try again."
Descripción: Esta cadena define cómo Hydra interactúa con el formulario web:
/login.php: La ruta del archivo que contiene el formulario de inicio de sesión.
username=^USER^&password=^PASS^: Los parámetros que el formulario espera. ^USER^ y ^PASS^ son marcadores de posición que Hydra reemplazará con los valores actuales durante el ataque.
Wrong password. Please try again.: El mensaje que Hydra busca en la respuesta del servidor para identificar que el intento fue fallido.
7. -f
Descripción: Detiene la ejecución de Hydra tan pronto como encuentra una combinación válida de nombre de usuario y contraseña.
8. -q
Descripción: Activa el modo silencioso, mostrando solo los resultados más importantes (intentos exitosos). Esto reduce la salida en pantalla.
Resultado esperado
Si Hydra encuentra una contraseña válida, la salida será algo como:

bash
Copiar código
[80][http-post-form] host: lookup.thm   login: jose   password: password123
¡Listo para probar!
Este script es muy útil para realizar pruebas de seguridad en tus propios sitios web o en entornos de pruebas como TryHackMe. ¡No olvides usarlo solo de forma ética!
![image](https://github.com/user-attachments/assets/a57f7c6a-9c1d-406a-838e-e69c56ed3114)
