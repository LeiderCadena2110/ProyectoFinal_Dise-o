# Car Rental System - Object Oriented Design

Sistema de alquiler de vehículos implementado en Python con principios de diseño orientado a objetos.

## Descripción

Este proyecto implementa un sistema completo de alquiler de automóviles basado en el diseño del libro "Grokking the Object-Oriented Design Interview". El sistema soporta:

- Diferentes tipos de vehículos: autos, vans, camionetas, SUVs y motocicletas
- Gestión de miembros y recepcionistas
- Reserva y alquiler de vehículos
- Devolución de vehículos con cálculo de multas por retraso
- Equipamiento adicional (GPS, sillas de bebé, portaesquíes)
- Servicios adicionales (asistencia en carretera, conductor adicional, WiFi)
- Seguros de alquiler
- Notificaciones
- Historial de vehículos

## Estructura del Proyecto

```
car-rental-system/
├── __init__.py
├── main.py                  # Demo completa del sistema
├── constants.py             # Enumeraciones y tipos de datos
├── address.py               # Clase Address
├── person.py                # Clase Person
├── account.py               # Account, Member, Receptionist, AdditionalDriver
├── vehicle.py               # Vehicle (ABC), Car, Van, Truck, SUV, Motorcycle
├── vehicle_log.py           # VehicleLog
├── vehicle_inventory.py     # Search, VehicleInventory
├── vehicle_reservation.py   # VehicleReservation
├── car_rental_location.py   # CarRentalLocation
├── car_rental_system.py     # CarRentalSystem
├── notification.py          # Notification
├── bill.py                  # Bill, BillItem
├── equipment.py             # Equipment
├── service.py               # Service
└── rental_insurance.py      # RentalInsurance
```

## Diagrama de Clases

Las clases principales del sistema son:

- **CarRentalSystem**: Punto de entrada principal del sistema
- **CarRentalLocation**: Representa las sucursales de alquiler
- **Vehicle** (abstracta): Clase base para todos los vehículos
  - **Car**, **Van**, **Truck**, **SUV**, **Motorcycle**: Tipos específicos
- **Account** (abstracta): Clase base para cuentas
  - **Member**: Clientes que alquilan vehículos
  - **Receptionist**: Personal que gestiona el sistema
- **VehicleReservation**: Gestiona las reservas
- **VehicleInventory**: Catálogo de vehículos disponibles
- **Bill**: Facturación con items detallados
- **Notification**: Sistema de notificaciones
- **Equipment / Service / RentalInsurance**: Servicios adicionales

## Casos de Uso Implementados

1. **Buscar vehículos** - Búsqueda por tipo, modelo y disponibilidad
2. **Reservar vehículo** - Crear una nueva reserva
3. **Agregar equipamiento/servicios/seguros** - Añadir extras a la reserva
4. **Check-out** - Recoger el vehículo
5. **Devolver vehículo** - Entregar el vehículo con cálculo de factura
6. **Cancelar reserva** - Cancelar una reserva existente
7. **Buscar miembro** - Búsqueda de miembros por recepcionista
8. **Notificaciones** - Envío de recordatorios

## Requisitos

- Python 3.8+

## Ejecución

```bash
python -m car_rental_system.main
```

O desde el directorio raíz:

```bash
python -m main
```
