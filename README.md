# Micro-X

Juego de navegador al estilo Rally-X, con sabor chileno: conduces una **micro amarilla**
por un laberinto de calles de Santiago, esquivando **obras, lomos de toro y quiltros** y huyendo de las
**radiopatrullas de Carabineros** (verde y blanco, con balizas).

## Cómo jugar
Abre `index.html` en el navegador (no requiere instalación).

- **Flechas / WASD**: mover (en móvil: botones o deslizar sobre la pantalla)
- **Espacio / Z**: soltar **humo negro** (gasta bencina); las radiopatrullas que lo toquen se detienen 3 s
- **P**: pausa

Junta las 10 banderas chilenas para pasar de nivel. Cada bandera seguida vale más (100, 200… 1000).
Los bidones **D** rellenan bencina. Si chocas con unas obras o te pilla Carabineros, pierdes una vida.
El radar de la derecha muestra el mapa completo.

## Mapa
El laberinto es fijo y reproduce el mapa de Rally-X (32×56 casillas, transcrito de una imagen del mapa original).

## Niveles y menú
- 20 niveles con dificultad gradual (más obras, lomos, quiltros y patrullas, patrullas más rápidas, menos bencina). Al completar el 20 ganas.
- Menú principal: JUGAR, **RÉCORD HISTÓRICO** (editable: Enter, escribes el número, Enter), NIVEL INICIAL y ZOOM. En juego, `+`/`-` cambian el zoom.

## Controles táctiles
Inspirados en Pac-Man (móvil) y Pac-Man 256: la micro avanza sola y tú solo eliges hacia dónde.
- **Deslizar el dedo** en cualquier parte de la pantalla: gira. El gesto se reconoce al instante y se recuerda hasta que la micro pueda girar (máx. 3 s). El giro en U es inmediato.
- **Toque corto** en cualquier parte de la pantalla: suelta humo (ya no hay botón de humo).
- **Cruceta (opcional)**: en el menú, `CONTROL < CRUCETA >` muestra 4 botones translúcidos en la esquina.
- Pantalla completa: el HUD es una barra delgada arriba y el radar una ventana pequeña en la esquina.
- Para probar los controles táctiles en un computador, abre `index.html?touch`.
- El radar es minimalista, como el de Rally-X: fondo negro con puntos (amarillo = banderas, rojo = patrullas, verde = bidones, blanco = tu micro).

## Aviso de bencina y resúmenes
- Bajo el 30 % de bencina: pitido de alarma, globo «¡POCA BENCINA!» sobre la micro, escape más negro y barra parpadeando. Bajo el 12 %: pitido más rápido, marco rojo en pantalla.
- Cada 3 niveles aparece una pantalla de **resumen del tramo** (puntos, tiempo y bencina de cada nivel, humo usado, patrullas frenadas, choques y hasta 3 estrellas).
- La micro lleva la patente **JCBO04** grande sobre el techo.

## Pausa y menú
- **Botón de pausa** (círculo amarillo arriba a la izquierda) o teclas `P` / `Esc`. La pausa congela todo, incluido el reloj y la bencina, y ofrece REANUDAR o MENÚ PRINCIPAL. El juego se pausa solo si cambias de pestaña o apps.
- En el menú principal, las filas NIVEL INICIAL, ZOOM y CONTROL tienen flechas `<` y `>`: toca el lado izquierdo para retroceder y el derecho para avanzar (con teclado, ← y →).

## Instalar como app (PWA)
El juego incluye `manifest.webmanifest`, `sw.js` e íconos, así que, servido por **https**, se puede instalar:
- **iPhone (Safari):** botón Compartir → *Añadir a pantalla de inicio*.
- **Android (Chrome):** menú ⋮ → *Instalar aplicación* (o *Añadir a pantalla de inicio*).
Se abre a pantalla completa y funciona sin conexión. Al publicar una versión nueva, cambia `CACHE` en `sw.js` (p. ej. `microx-v2`) para que los celulares la descarguen.

### Publicar con GitHub Pages
Repositorio → *Settings* → *Pages* → *Build and deployment* → Source: **Deploy from a branch** → Branch: `ccr-958f09af-vrjph8`, carpeta `/ (root)` → *Save*.
La dirección queda en `https://jbeghelli.github.io/micro-x/`. Cada `git push` a esa rama la actualiza.

## Novedades
- **Bencina más exigente:** el tanque dura ~50 s en el nivel 1 y ~32 s en el 20 (cada bidón da +30 %). Con el tanque vacío la micro avanza muy lenta y, tras **8 s**, pierdes una vida.
- **La micro se ve de perfil**, como en el logo: de lado al ir a izquierda/derecha, de frente al bajar y de atrás al subir (con la patente JCBO04).
- **Música** chiptune con ritmo de cumbia, generada en el dispositivo (sin archivos). Se acelera cuando queda poca bencina. Botón de silencio junto a la pausa y opción MÚSICA en el menú.
- **Ajuste de pantalla móvil:** el área de juego usa el tamaño real visible (con barra de Chrome, muescas y barra de gestos).

## Música
Se genera en el dispositivo con WebAudio, sin archivos. El menú tiene **TEMA MENÚ** y **TEMA JUEGO** (se pueden elegir distintos); al elegir «TEMA JUEGO» en el menú suena como vista previa. El botón de parlante silencia todo.
- **Cumbia**: composición propia.
- **Obras de dominio público**, escritas aquí como notas (sin grabaciones de terceros): Para Elisa y Quinta sinfonía (Beethoven), Himno a la Alegría (Beethoven) en cinco estilos (normal, marcha, galope, cumbia y solemne, para probar qué ritmo va mejor), En la gruta del rey de la montaña (Grieg, acelera en cada vuelta), Canon (Pachelbel) y Tocata en re menor (Bach).
- La música se acelera cuando queda poca bencina.
- Aviso: las melodías clásicas son de dominio público, pero **un arreglo o una grabación moderna sí pueden tener derechos**. Aquí todo se sintetiza desde cero. Del Himno Nacional de Chile hay normas de respeto a los símbolos patrios; está pendiente (ver `ROADMAP.md`).

## Patrullas de perfil
Las radiopatrullas de Carabineros (sedán verde con techo blanco, panel blanco en la puerta delantera con el escudo y «CARABINEROS DE CHILE», baliza amarilla en el techo y llantas de aleación, según foto de referencia) ahora se ven como la micro: de lado al ir a izquierda/derecha, de frente al bajar y de atrás al subir.

## Diseño tipo letrero de micro
HUD, menú de inicio, pausa, avisos y resumen usan lettering de letrero de micro amarilla: fondo negro, cabecera naranja, cajas rojas y letras condensadas pintadas a mano (cada letra con un leve desnivel). La tipografía es **Anton** (SIL Open Font License 1.1, `fonts/ANTON-OFL.txt`).
La cámara va siempre centrada en la micro, así que nunca queda tapada por la barra superior. El menú muestra la versión (abajo a la derecha) para saber qué compilación estás jugando; el juego instalado se actualiza solo al abrirlo con conexión.

## Terremoto y vida extra
- El ícono de bencina es un **terremoto** (vino pipeño de color ámbar rojizo con una bola de helado de piña blanco y bombilla a rayas): los bidones del mapa, el aviso de poca bencina y la barra de arriba. Es solo estético: sigue dando +30 de bencina.
- Cada **3 niveles completados** ganas **1 vida extra** (máximo 5). Se anuncia en la pantalla de resumen.

## Obstáculos
Los baches se reemplazaron por tres obstáculos, que crecen de a poco entre el nivel 1 y el 20:
- **Obras en la calzada** (pozo con tablón, valla a rayas con lámpara y conos): bloquean el paso. Si chocas, pierdes una vida (4 en el nivel 1 → 20 en el 20). Las patrullas las esquivan.
- **Lomos de toro** (franja amarilla y negra en tramos rectos): no matan; te frenan a la mitad por 1 segundo, y también frenan a las patrullas (4 → 14).
- **Quiltros** (perros callejeros): caminan por las calles y a veces se detienen. Si los tocas pierdes 18 de bencina y 100 puntos, y te frenas un momento; el perro sale corriendo. Cuando un perro se cruza con una patrulla, la deja detenida 1,2 s (2 → 6).

## Otro juego en este repositorio
`chanchitos/` contiene **Chanchitos de tierra**, un juego educativo para niños (corredor + terrario). Ver `chanchitos/README.md`.
