<div align="center">

<img src="assets/icon.png" width="96" alt="Shtil VPN">

# Shtil VPN · Штиль

[Русский](README.md) · [English](README.en.md) · [Deutsch](README.de.md) · **Español** · [فارسی](README.fa.md)

**Aplicaciones VPN sobre el núcleo [sing-box](https://github.com/SagerNet/sing-box)
(VLESS + Reality) para teléfonos Android, Android TV, Windows y macOS.**

Los sitios rusos —bancos, servicios públicos, tiendas— siguen abriéndose por la ruta directa
con la VPN encendida, así que mantienen toda su velocidad.

![Android](https://img.shields.io/badge/Android-6.0%2B-3ddc84)
![Android TV](https://img.shields.io/badge/Android%20TV-con%20mando-3ddc84)
![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078d4)
![macOS](https://img.shields.io/badge/macOS-12%2B-000000)
![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-sing--box-blue)
![Protocolo](https://img.shields.io/badge/protocolo-VLESS%20%2B%20Reality-blue)

</div>

---

## De un vistazo

| Pregunta | Respuesta |
|---|---|
| Qué es | Un cliente VPN para teléfonos y televisores Android, Windows y macOS |
| Núcleo y protocolo | sing-box, VLESS + Reality sobre TCP |
| Sitios rusos | van por la ruta directa; las listas viajan dentro de la app y nunca se descargan |
| Clave | un enlace de suscripción de nuestro bot de Telegram — también sirve el de otro proveedor en formato VLESS |
| Tiendas de aplicaciones | no hacen falta: distribuimos los archivos nosotros y la actualización llega por el aire |
| Idiomas de la interfaz | ruso, inglés, alemán, español, persa |
| Precio | 30 días gratis y después 499 ₽ al mes; 2 horas se pueden probar sin Telegram |
| Cuentas dentro de la app | ninguna. Sin publicidad ni compras integradas |

---

## Descargas

| Dispositivo | Archivo | Cómo instalar |
|---|---|---|
| **Teléfono o tableta Android** | [sub.ndvsdom54.ru/get](https://sub.ndvsdom54.ru/get) — la página elige el archivo | Abrir la dirección en el navegador del teléfono y pulsar «Descargar» |
| **Android TV** | [sub.ndvsdom54.ru/tv.apk](https://sub.ndvsdom54.ru/tv.apk) — el archivo empieza enseguida | Escribir la dirección con el mando en una app descargadora (por ejemplo Downloader) |
| **Windows** | [ShtilVPN-windows.exe](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-windows.exe) | Descargar y ejecutar |
| **Mac con chip Apple** | [ShtilVPN-mac-apple.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-apple.dmg) | Arrastrar a «Aplicaciones» |
| **Mac con Intel** (2020 y anteriores) | [ShtilVPN-mac-intel.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-intel.dmg) | Arrastrar a «Aplicaciones» |

Si no sabe qué archivo de Android necesita, tome el
[universal](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-android-universal.apk):
es el más pesado (unos 76 MB), pero entra en cualquier dispositivo.

Todos los archivos en una lista: [«Shtil — archivos de
instalación»](https://github.com/narvinIR/shtil-vpn/releases/tag/apps). Las direcciones son
permanentes: cambia el archivo, el enlace se mantiene.

La clave de suscripción la entrega [@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot):
30 días gratis y después 499 ₽ al mes. También se puede empezar sin Telegram — el botón
«Probar ahora» abre una sesión de invitado de 2 horas.

---

## Tres pasos hasta la conexión

1. Descargar el archivo de la tabla y instalarlo.
2. Pulsar «Probar ahora» (2 horas, sin Telegram) **o** pedir el enlace de suscripción al bot y
   añadirlo en la app — a mano, desde el portapapeles o con el código corto de la imagen QR.
3. Pulsar «Conectar». Los sitios rusos seguirán abriéndose directamente: está previsto así.

En el televisor no hay que teclear nada: el código corto aparece como imagen QR, el teléfono lo
escanea y la suscripción llega sola.

---

## Cómo se ve

| Teléfono: conectado | Teléfono: rutas separadas | Televisor | Ordenador |
|---|---|---|---|
| <img src="assets/phone-connected.png" width="180"> | <img src="assets/phone-split-routing.png" width="180"> | <img src="assets/tv-connected.png" width="260"> | <img src="assets/desktop-main.png" width="260"> |

---

## Qué puede cada aplicación

| Función | Teléfono | Televisor | Windows | macOS |
|---|:---:|:---:|:---:|:---:|
| VLESS + Reality sobre el núcleo sing-box | sí | sí | sí | sí |
| Sitios rusos por la ruta directa (listas dentro de la app) | sí | sí | sí | sí |
| Enlace de suscripción en vez de clave larga | sí | sí | sí | sí |
| Código corto del bot | sí | sí | sí | sí |
| Código como imagen QR desde el teléfono | sí | sí | — | — |
| Acceso de invitado de 2 horas sin Telegram | sí | sí | sí | sí |
| Actualización por el aire, sin tienda | sí | sí | sí | sí |
| Elección de apps dentro del túnel | sí | sí | — | — |
| Diseño pensado para el mando | — | sí | — | — |
| Registro y tabla de conexiones | en curso | en curso | sí | sí |
| Cinco idiomas | sí | sí | sí | sí |

---

## Qué hay dentro

- **Núcleo** — [sing-box](https://github.com/SagerNet/sing-box), VLESS + Reality sobre TCP.
- **Rutas separadas.** Las listas de dominios y rangos rusos viven dentro de la aplicación y
  nunca se descargan: un servidor de reglas remoto puede ser inalcanzable desde Rusia y entonces
  la VPN ni siquiera arrancaría. Para los dominios de ruta directa solo se responden direcciones
  IPv4; de otro modo el dispositivo seguiría un registro AAAA por fuera de la ruta.
- **Una clave para todos los dispositivos.** El enlace de suscripción vale a la vez para el
  teléfono, el televisor y el ordenador; si la clave cambia en el servidor, todos toman la nueva.
- **Actualización por el aire.** La aplicación busca versiones nuevas por su cuenta; en el
  ordenador solo se instala lo que lleva nuestra firma.
- **Nada de más.** Sin cuentas dentro de la app, sin publicidad y sin compras integradas.

---

## Qué dirá el sistema al instalar

Las aplicaciones se reparten fuera de Google Play y de la App Store, así que cada sistema
pregunta una vez, como con cualquier app ajena a una tienda.

**Android (teléfono).** «Instalación desde este origen no permitida» → permitir al navegador
instalar aplicaciones. Después Google puede mostrar una pantalla roja → «Instalar de todos modos».

**Android TV.** La misma pantalla roja de Google; el botón de confirmación está abajo y se
alcanza con el mando.

**Windows.** Ventana azul «Windows protegió su PC» → **«Más información» → «Ejecutar de todas
formas»**. No tenemos certificado de editor: desde 2024 Microsoft ya no vende confianza
inmediata; se gana con el número de instalaciones.

**macOS.** El primer arranque se rechaza → **Ajustes del Sistema → Privacidad y seguridad →
«Abrir igualmente»** → contraseña de administrador. Después la app se abre con doble clic.

---

## Preguntas frecuentes

**¿Hace falta Google Play o la App Store?**
No. El archivo se descarga desde aquí o desde la [página de instalación](https://sub.ndvsdom54.ru/get),
y la app encuentra las versiones nuevas sola.

**¿Cómo instalar en un televisor sin navegador?**
Con una app descargadora tipo Downloader: escribir `sub.ndvsdom54.ru/tv.apk` con el mando y el
archivo empieza enseguida. La dirección es corta a propósito y no lleva «https://».

**¿Por qué fallan los bancos y los servicios públicos con otras VPN?**
Porque su tráfico pasa por el túnel y el sitio ve una dirección extranjera. Aquí esos sitios se
quedan en la ruta directa y la lista viaja dentro de la aplicación.

**¿Sirve una clave de otro proveedor?**
Sí, si es un enlace de suscripción o una clave en formato VLESS. La app es la entrada al túnel;
el servidor no va incluido.

**¿Cuántos dispositivos por clave?**
Dos a la vez. Un enlace cubre teléfono, televisor y ordenador.

**¿Hay versión para iOS o Linux?**
Propia no. El enlace de suscripción funciona en clientes de terceros — v2RayTun en iOS o
cualquier cliente basado en sing-box.

---

## Aplicaciones y código fuente

| Aplicación | Sistema | Código | Licencia |
|---|---|---|---|
| Shtil (Android) | Android 6.0+, teléfonos y televisores | fork de [vpn4tv-native](https://github.com/VPN4TV/vpn4tv-native) | GPL-3.0 |
| Shtil para ordenador | Windows 10/11, macOS 12+ | [shtil-vpn-desktop](https://github.com/narvinIR/shtil-vpn-desktop) | MIT |
| Núcleo | dentro de ambas apps | [sing-box](https://github.com/SagerNet/sing-box) | GPL-3.0 |

Este repositorio es el escaparate: descripciones y enlaces permanentes a los archivos. Cada
archivo se distribuye bajo la licencia de su propia aplicación.

Preguntas, fallos y sugerencias — [issues](https://github.com/narvinIR/shtil-vpn/issues) o el bot
[@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot).
