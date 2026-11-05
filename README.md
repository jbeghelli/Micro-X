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
Inspirados en Pac-Man (móvil) y Pac-Man 256: la micro avanza sola y tú solo eliges hacia dónde.
- **Deslizar el dedo** en cualquier parte de la pantalla: gira. El gesto se reconoce al instante y se recuerda hasta que la micro pueda girar (máx. 3 s). El giro en U es inmediato.
- **Toque corto** en cualquier parte: suelta humo (también hay un botón de humo pequeño en la esquina).
- **Cruceta (opcional)**: en el menú, `CONTROL < CRUCETA >` muestra 4 botones translúcidos en la esquina.
- Pantalla completa: el HUD es una barra delgada arriba y el radar una ventana pequeña en la esquina.
- Para probar los controles táctiles en un computador, abre `index.html?touch`.
- El radar es minimalista, como el de Rally-X: fondo negro con puntos (amarillo = banderas, rojo = patrullas, verde = bidones, blanco = tu micro).
