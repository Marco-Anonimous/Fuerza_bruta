
![image](https://github.com/user-attachments/assets/165f4f1e-a993-4f4b-9c71-b52484f47654)

hydra -l jose -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong password. Please try again." -f -q
1. hydra
Descripción: Ejecuta la herramienta Hydra, que se utiliza para realizar ataques de fuerza bruta contra diferentes protocolos y servicios.
2. -l jose
Descripción: Especifica un único nombre de usuario (jose) que se utilizará durante el ataque.
Alternativa: Si quisieras probar múltiples nombres de usuario, usarías -L seguido del archivo que contiene una lista de nombres, por ejemplo:
bash
Copiar código
-L userlist.txt
3. -P /usr/share/wordlists/rockyou.txt
Descripción: Especifica el archivo de contraseñas (rockyou.txt) que Hydra usará para probar posibles contraseñas.
Ruta: Asegúrate de que la ruta al archivo es correcta. Si no tienes rockyou.txt, puedes instalarlo o descargarlo:
bash
Copiar código
sudo apt install wordlists
4. lookup.thm
Descripción: Es el dominio o la dirección IP del servidor objetivo.
Nota: Si estás usando un dominio personalizado como lookup.thm, asegúrate de que esté configurado en tu archivo /etc/hosts para apuntar a la dirección IP correcta:
Copiar código
10.10.10.10 lookup.thm
5. http-post-form
Descripción: Especifica que Hydra atacará un formulario web con un método HTTP POST.
Uso común: Hydra también admite otros módulos como ftp, ssh, etc., pero aquí estás apuntando a un formulario web.
6. "/login.php:username=^USER^&password=^PASS^:Wrong password. Please try again."
Descripción: Define el comportamiento del formulario web y cómo Hydra interactúa con él.
/login.php:
La ruta del archivo que contiene el formulario de inicio de sesión. En este caso, está ubicado en /login.php.
username=^USER^&password=^PASS^:
Estos son los parámetros que el formulario espera recibir:
^USER^: Es el marcador de posición que Hydra reemplazará con el nombre de usuario actual.
^PASS^: Es el marcador de posición que Hydra reemplazará con la contraseña actual.
Wrong password. Please try again.:
Es el texto que Hydra busca en la respuesta del servidor para identificar un intento fallido. Asegúrate de que esta cadena coincida exactamente con lo que el servidor devuelve.
7. -f
Descripción: Indica a Hydra que se detenga tan pronto como encuentre una combinación válida de nombre de usuario y contraseña.
8. -q
Descripción: Activa el modo silencioso, lo que reduce la cantidad de salida en pantalla. Solo muestra los resultados importantes, como intentos exitosos.

![image](https://github.com/user-attachments/assets/a57f7c6a-9c1d-406a-838e-e69c56ed3114)
