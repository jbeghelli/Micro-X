# Micro-X

Juego de navegador al estilo Rally-X, con sabor chileno: conduces una **micro amarilla**
por un laberinto de calles de Santiago, esquivando **baches** y huyendo de las
**radiopatrullas de Carabineros** (verde y blanco, con balizas).

## Cómo jugar
Abre `index.html` en el navegador (no requiere instalación).

- **Flechas / WASD**: mover (en móvil: botones o deslizar sobre la pantalla)
- **Espacio / Z**: soltar **humo negro** (gasta bencina); las radiopatrullas que lo toquen se detienen 3 s
- **P**: pausa

Junta las 10 banderas chilenas para pasar de nivel. Cada bandera seguida vale más (100, 200… 1000).
Los bidones **D** rellenan bencina. Si caes en un bache o te pilla Carabineros, pierdes una vida.
El radar de la derecha muestra el mapa completo.

## Mapa
El laberinto es fijo y reproduce el mapa de Rally-X (32×56 casillas, transcrito de una imagen del mapa original).

## Niveles y menú
- 20 niveles con dificultad gradual (más baches y patrullas, patrullas más rápidas, menos bencina). Al completar el 20 ganas.
- Menú principal: JUGAR, **RÉCORD HISTÓRICO** (editable: Enter, escribes el número, Enter), NIVEL INICIAL y ZOOM. En juego, `+`/`-` cambian el zoom.

## Controles táctiles
- En vertical: el juego arriba y, abajo, una **cruceta de 4 botones grandes** y el **botón de humo**. En horizontal los controles se superponen al mapa.
- **Un toque fija la dirección**: la micro gira hacia ahí en la próxima esquina posible (el toque se recuerda hasta 3 s). También puedes mantener pulsado y deslizar el dedo entre botones.
- Para probar los controles táctiles en un computador, abre `index.html?touch`.
- El radar es minimalista, como el de Rally-X: fondo negro con puntos (amarillo = banderas, rojo = patrullas, verde = bidones, blanco = tu micro).
