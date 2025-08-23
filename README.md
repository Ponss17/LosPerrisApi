# ♥️ API de Nayecute

Esta es una API en Flask que muestra el rango actual de Valorant de **[Naye](https://www.twitch.tv/nayecutee)** usando la API de [HenrikDev](https://docs.henrikdev.xyz/).  
Está hosteada en Render y puede mantenerse despierta con UptimeRobot.

Endpoints:
- `/` → Mensaje de prueba: funcionando jiji, cualquier duda con ponsscito :)
- `/rango` → Devuelve el rango actual, puntos y cambio de MMR en la última partida: Mi rango actual es Diamante 2 con 53 puntos 🤗✨, Mi última partida: [+18]

Variables necesarias:
- API_KEY → tu API key de HenrikDev
- PORT → Render lo maneja automáticamente

Personalizar para otro jugador:
Si quieres mostrar el rango de otro jugador de Valorant, cambia estas variables en el código:
NOMBRE = "NombreDelJugador"
TAG = "1234"  # El número de su tag
REGION = "na"  # ej: na, eu, kr, etc.
Luego la API seguirá funcionando igual, solo que mostrará los datos del jugador que hayas configurado.

Mantener la API despierta:
- Render Free apaga servicios si no reciben visitas.
- Usa UptimeRobot para hacer ping cada 5 minutos y mantenerla activa.

Nota final:
Hecho con cariño para **[Naye en Twitch](https://www.twitch.tv/nayecutee)** ❤️  
Usando la API de HenrikDev para traer datos oficiales de Valorant.  
Puedes usarla libremente y adaptarla para otros jugadores cambiando los datos arriba. 
