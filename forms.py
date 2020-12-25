from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, SubmitField, DateField, Form
from wtforms.validators import InputRequired, Length

from models import Provider, Order, Department


def get_all_providers():
    return Provider.query.all()


def get_all_orders():
    return Order.query.all()


def get_all_departments():
    return Department.query.all()


class OrderForm(Form):
    name = StringField("Название заказа")
    unit = StringField("Еденица измерения")
    provider = QuerySelectField("Поставщик", query_factory=get_all_providers)
    submit = SubmitField("Подтвердить")


class DepartmentForm(Form):
    name = StringField("Название")
    chief = StringField("Имя начальника")
    submit = SubmitField("Подтвердить")


class ProviderForm(Form):
    name = StringField("Наименование поставщика")
    submit = SubmitField("Подтвердить")


class OpenOrderForm(Form):
    order = QuerySelectField("Заказ", query_factory=get_all_orders)
    amount = IntegerField("Колличество")
    department = QuerySelectField("Исполнитель заказа", query_factory=get_all_departments)
    due_date = DateField("Срок исполнения", format='%Y-%m-%d')
    customer = StringField("Заказчик")
    submit = SubmitField("Печать")

