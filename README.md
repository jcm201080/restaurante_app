# 🍽️ Restaurante App – SaaS para Bares y Restaurantes

## 🚀 Descripción

Aplicación web desarrollada con Flask para la gestión de cartas digitales de bares y restaurantes.

Permite:

* Mostrar carta pública moderna
* Gestionar productos desde un panel admin (móvil-friendly)
* Destacar platos, sugerencias y fuera de carta
* Integrar IA para recomendaciones

---

## 🧱 Estructura del proyecto

```
restaurante_app/
│
├── app.py
├── config.py
├── extensions.py
│
├── models/
│   ├── user.py
│   ├── producto.py
│
├── routes/
│   ├── public.py
│   ├── admin.py
│   ├── ia.py
│
├── templates/
│   ├── base.html
│   ├── public/
│   │   ├── menu.html
│   │   └── index.html
│   │
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── productos.html
│   │   └── login.html
│
├── static/
│   ├── css/
│   ├── js/
│
└── database/
    └── app.db
```

---

## ✅ FUNCIONALIDADES IMPLEMENTADAS

### 🟢 Parte pública

* Carta dinámica desde base de datos
* Agrupación por categorías
* Secciones:

  * ⭐ Sugerencias
  * 🍽️ Plato del día
  * 🔥 Fuera de carta
* Botón IA → recomendación automática

---

### 🔐 Panel Admin

* Login básico (usuario: `admin`, pass: `1234`)
* CRUD de productos:

  * Añadir
  * Editar
  * Eliminar (con confirmación)
* Campos:

  * nombre
  * precio
  * categoría
  * tipo (tapa / media / ración)
* Flags:

  * destacado
  * plato del día (único)
  * fuera de carta
* Filtro por categoría

---

### ⚙️ Backend

* Flask + SQLAlchemy
* Base de datos SQLite auto-creada
* Sistema de sesión para admin
* Arquitectura con Blueprints

---

## 🧠 DECISIONES IMPORTANTES

* Un solo endpoint `/update` para:

  * guardar
  * eliminar (usando `action`)
* Uso de `request.form.get()` para evitar errores
* Separación de vistas:

  * `base.html` → público
  * `base_admin.html` → panel admin
* Cache busting con `?v=timestamp` en CSS

---

## ⚠️ COSAS A MEJORAR (PRÓXIMOS PASOS)

### 🎨 UI / UX

* Mejorar diseño de carta (menu.html)

  * badges visuales (tapa, ración…)
  * destacar plato del día
  * mejorar tipografía
* Diseño responsive más pulido

---

### 🔍 Funcionalidad

* Búsqueda por nombre en admin
* Selector dinámico de categorías (desde DB)
* Edición más cómoda (UX tipo app)
* Mensajes flash visibles

---

### 📸 Contenido

* Subida de imágenes de productos
* Mostrar imágenes en carta

---

### 🤖 IA

* Recomendaciones más inteligentes
* Chat tipo asistente (no solo alert)

---

### 🔐 Seguridad

* Sistema de usuarios real (no hardcode)
* Hash de contraseñas
* Protección CSRF

---

### 📱 Negocio (MUY IMPORTANTE)

* Generación de QR para carta
* Multi-restaurante (SaaS)
* Panel por cliente
* Hosting + despliegue

---

## 🎯 OBJETIVO DEL PROYECTO

Crear un sistema vendible a:

* Bares 🍺
* Restaurantes 🍽️
* Hamburgueserías 🍔
* Cafeterías ☕

Con:
👉 Carta digital
👉 Gestión sencilla
👉 IA integrada

---

## 🚀 ESTADO ACTUAL

🟢 MVP funcional
🟡 UX mejorable
🔴 Falta capa comercial (lo que lo hace vendible)

---

## 🔥 SIGUIENTE PASO

👉 Mejorar `menu.html` → diseño visual que impacte

---

## 😏 VISIÓN

Convertir esto en:

💰 SaaS de gestión de cartas digitales + IA para hostelería


MEJORAS Y PROGRESO:

# 📅 PROGRESO – Carta digital (día actual)

## ✅ MEJORAS IMPLEMENTADAS

### 🎨 Frontend (menu.html + menu.css)

* 🔄 Rediseño completo de la carta:

  * Uso de `card-producto` como componente base
  * Eliminación de estilos antiguos (`.card`, `.destacado`, etc.)
  * Estructura más limpia y escalable

* ⭐ Secciones mejoradas:

  * Plato del día destacado (card especial)
  * Sugerencias con badge ⭐
  * Fuera de carta con badge 🔥
  * Categorías organizadas visualmente

* 🎯 UX mejorada:

  * Grid responsive
  * Jerarquía visual clara
  * Hover effects en productos

---

### 🧠 Mejora clave: TIPOS DE PRODUCTO (MUY IMPORTANTE)

* Se añade campo `tipo` en productos:

  * `tapa`
  * `media`
  * `racion`
  * `plato`

* Implementación visual con colores:

  * 🟢 tapa → verde
  * 🟡 media → amarillo
  * 🔴 ración → rojo
  * 🔵 plato → azul

* Badge dinámico en HTML:

  ```html
  <span class="badge tipo {{ p.tipo }}">{{ p.tipo }}</span>
  ```

---

### 🧱 Backend

* ✔️ Modelo `Producto` preparado correctamente:

  * tipo
  * categoria
  * flags (destacado, fuera_carta, plato_dia)

* ✔️ Script `seed_productos.py` mejorado:

  * Más variedad de productos
  * Inclusión de tipos
  * Preparado para demo realista

---

### ⚙️ Arquitectura (MEJORA PRO)

* 🔥 Separación de estilos:

  * `menu.css` → solo frontend
  * `admin.css` → panel admin

* Evitamos mezclar UI pública con admin

---

## 🧹 LIMPIEZA REALIZADA

* Eliminación de CSS no utilizado:

  * `.card`
  * `.hero`
  * `.btn` antiguos
  * `.alert`, `.danger`, etc.

* Código más mantenible y claro

---

## 🚀 ESTADO ACTUAL

🟢 Carta visualmente atractiva
🟢 UX moderna tipo app
🟢 Base sólida para SaaS
🟡 Admin funcional (mejorable UX)

---

## 🔥 PRÓXIMOS PASOS

### 🎯 PRIORIDAD ALTA

* Mejorar UX del admin:

  * Edición sin recargar
  * Mejor layout (tipo panel real)

* Modal para IA (eliminar alert)

* Añadir imágenes a productos

---

### 💡 NIVEL PRO

* Filtros dinámicos por tipo (tapa, ración…)
* Categorías dinámicas desde DB
* Modo móvil tipo app (scroll + sticky)

---

### 💰 NEGOCIO

* Generar QR para restaurantes
* Multi-restaurante (SaaS)
* Branding por cliente

---

## 😏 NOTA

El proyecto ya ha pasado de:

👉 “proyecto de curso”
👉 a “producto vendible con potencial real”

---


# 🍔 Restaurante App – Roadmap

## 🚧 Estado actual

Aplicación web funcional con:

* Panel admin de productos
* Subida de imágenes
* Carta visual moderna
* Despliegue en VPS con Nginx + Gunicorn
* Subdominio activo

---

## 🔥 Tareas pendientes (prioridad alta)

### 🗄️ Backend

* [ ] Migrar base de datos a PostgreSQL
* [ ] Revisar modelo de datos (optimizar categorías / tipos)
* [ ] Evitar duplicados en seed

---

### 🎨 Frontend / UX

* [ ] Crear página de contacto moderna
* [ ] Mejorar footer:

  * enlaces útiles
  * info del restaurante
  * año dinámico
* [ ] Mejorar header:

  * resaltar página activa
  * navegación más clara
* [ ] Separar bebidas en página independiente

---

### 🤖 IA

* [ ] Mejorar asistente:

  * recomendaciones reales
  * preguntas tipo:

    * "quiero algo ligero"
    * "voy con niños"
    * "sin gluten"
* [ ] UI más atractiva para el asistente

---

### 🖼️ Imágenes

* [ ] Añadir imágenes reales a productos clave
* [ ] Optimizar tamaños (rendimiento)
* [ ] Placeholder elegante para productos sin imagen

---

### 🚀 Producción

* [ ] Migrar a PostgreSQL
* [ ] Logs y control de errores
* [ ] Optimizar Gunicorn (workers)
* [ ] Revisar seguridad básica

---

## 💡 Ideas futuras

* [ ] Sistema de reservas
* [ ] Pedido online
* [ ] Panel cliente
* [ ] Multi-restaurante (SaaS)

---

## 🧠 Notas

* No modificar código directamente en VPS (usar Git)
* Mantener permisos correctos (uploads y DB)
* Testear siempre en local antes de subir

---

## 🚀 Objetivo

Convertir esto en:
👉 Producto real para restaurantes
👉 Posible SaaS escalable

---
