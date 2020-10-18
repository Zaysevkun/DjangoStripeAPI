# DjangoStripeAPI

With this API you can pay for your order with Stripe online payments.

You can check out live project on [Heroku](https://djangostripeapi.herokuapp.com/)

## Project setup using Docker

In order to use this method you need Docker installed

1. `git clone https://github.com/Zaysevkun/DjangoStripeAPI`
2. `cd DjangoStripeAPI`
3. Add __.env__ file
##### EXAMPLE:
```
SECRET_KEY=qwerty123
DATABASE_URL=postgres://your_db_user_name:user_password@db:5432/your_db_name
ALLOWED_HOSTS=*
DEBUG=0

STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```
3. Add __.env.db__ file
##### EXAMPLE:
```
POSTGRES_USER=your_db_user_name
POSTGRES_PASSWORD=user_password
POSTGRES_DB=your_db_name
```
4. `docker-compose build`
5. `docker-compose up -d`
6. `docker-compose exec web python manage.py migrate`
7. `docker-compose exec web python manage.py collectstatic`

## Project setup without Docker

1. `git clone https://github.com/Zaysevkun/DjangoStripeAPI`
2  `create postgres db`
3. `cd DjangoStripeAPI`
4. `pip install -r requirements.txt`
5. Add __.env__ file
##### EXAMPLE:
```
SECRET_KEY=qwerty123
DATABASE_URL=postgres://your_db_user_name:user_password@127.0.0.1:5432/your_db_name
ALLOWED_HOSTS=*
DEBUG=0

STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```
6. `python manage.py migrate`
7. `python manage.py runserver 0.0.0.0:8000`

## END POINTS

| *URL* | *Method*|*Description*|
|-------|---------|-------------|
| `api/items/{id}/buy` | `GET` | creates Stripe PaymentIndent for Order and returns __user_secret__|

Success Response:
- Code: 200
- Content:
```
{"client_secret": "some_secret_key"}
```
| *URL* | *Method*|*Description*|
|-------|---------|-------------|
| `api/items/{id}` | `GET` | returns page with your order summary and form to pay with card through Stripe|

Success Response:
- Code: 200
- Content:Checkout page

![form](https://i.ibb.co/F4XCYbT/Screenshot-from-2020-10-18-11-02-08.png 'Форма оплаты')

