# PR0702
## Archivos con código fuente
[`controllers/controllers.py`](./files/controllers.py.md)
## Pruebas de funcionamiento
### Subscripciones
![Subscripciones 1](./img/subs_1.png)
![Subscripciones 2](./img/subs_2.png)
### `/api/subscription`
![/api/subscription](./img/api_subscription.png)
```json
[{"name": "Subscripcion1", "subscription_code": "1234", "price": 0.0, "status": "pending"}, {"name": "Subscripcion2", "subscription_code": "4312", "price": 0.0, "status": "expired"}, {"name": "1234", "subscription_code": "4322", "price": 0.0, "status": "cancelled"}, {"name": "3241235", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "4345", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "3212", "subscription_code": "123433", "price": 0.0, "status": "pending"}, {"name": "4321451", "subscription_code": "41234", "price": 0.0, "status": "active"}, {"name": "123412", "subscription_code": "1234", "price": 0.0, "status": "pending"}, {"name": "435124645fasfd", "subscription_code": "1234523", "price": 0.0, "status": "active"}, {"name": "121345123412", "subscription_code": "23412", "price": 0.0, "status": "pending"}, {"name": "412652141", "subscription_code": "42341", "price": 0.0, "status": "pending"}]
```
### `/api/subscription?status=active`
![status active](./img/status_active.png)
```json
[{"name": "3241235", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "4345", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "4321451", "subscription_code": "41234", "price": 0.0, "status": "active"}, {"name": "435124645fasfd", "subscription_code": "1234523", "price": 0.0, "status": "active"}]
```
### `/api/subscription?status=cancelled`
![status cancelled](./img/status_cancelled.png)
```json
[{"name": "1234", "subscription_code": "4322", "price": 0.0, "status": "cancelled"}]
```
### `/api/subscription?page=1`
![page 1](./img/page_1.png)
```json
[{"name": "Subscripcion1", "subscription_code": "1234", "price": 0.0, "status": "pending"}, {"name": "Subscripcion2", "subscription_code": "4312", "price": 0.0, "status": "expired"}, {"name": "1234", "subscription_code": "4322", "price": 0.0, "status": "cancelled"}, {"name": "3241235", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "4345", "subscription_code": "1234", "price": 0.0, "status": "active"}, {"name": "3212", "subscription_code": "123433", "price": 0.0, "status": "pending"}, {"name": "4321451", "subscription_code": "41234", "price": 0.0, "status": "active"}, {"name": "123412", "subscription_code": "1234", "price": 0.0, "status": "pending"}, {"name": "435124645fasfd", "subscription_code": "1234523", "price": 0.0, "status": "active"}, {"name": "121345123412", "subscription_code": "23412", "price": 0.0, "status": "pending"}]
```
### `/api/subscription?page=2`
![page 2](./img/page_2.png)
```json
[{"name": "412652141", "subscription_code": "42341", "price": 0.0, "status": "pending"}]
```
### `/api/subscription/Subscripcion1`
![name 1](./img/name_1.png)
```json
[{"name": "Subscripcion1", "subscription_code": "1234", "price": 0.0, "status": "pending"}]
```
### `/api/subscription/1234`
![name 2](./img/name_2.png)
```json
[{"name": "1234", "subscription_code": "4322", "price": 0.0, "status": "cancelled"}]
```