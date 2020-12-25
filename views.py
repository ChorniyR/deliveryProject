from datetime import date

from flask import Blueprint, render_template, request, redirect, url_for, session

from constants import constants
from forms import OrderForm, ProviderForm, DepartmentForm, OpenOrderForm
from models import Order, Department, Provider

import json

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def main_page():
    open_order_form = OpenOrderForm(request.form)
    if request.method == "POST":
        session['order'] = {
            'name': open_order_form.order.data.name,
            'unit': open_order_form.order.data.unit,
            'amount': open_order_form.amount.data,
            'due_date': open_order_form.due_date.data,
            'customer': open_order_form.customer.data
        }
        session['department'] = {
            'name': open_order_form.department.data.name,
            'chief': open_order_form.department.data.chief
        }
        return redirect(url_for("page.order_open"))
    return render_template('index.html', open_order_form=open_order_form)


@page.route('/creating_order', methods=['GET', 'POST'])
def creating_order():
    orders = Order.query.all()
    form = OrderForm(request.form)
    if request.method == "POST":
        name = form.name.data
        unit = form.unit.data
        provider_id = form.provider.data.id
        Order.save(Order(name=name, unit=unit, provider_id=provider_id))
    return render_template('orders.html', orders=orders, form=form)


@page.route('/creating_department', methods=['GET', 'POST'])
def creating_department():
    departments = Department.query.all()
    form = DepartmentForm(request.form)
    if request.method == "POST":
        name = form.name.data
        chief = form.chief.data
        Department.save(Department(name=name, chief=chief))
    return render_template('department.html', departments=departments, form=form)


@page.route('/creating_provider', methods=['GET', 'POST'])
def creating_provider():
    providers = Provider.query.all()
    form = ProviderForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        Provider.save(Provider(name=name))
    return render_template('provider.html', providers=providers, form=form)


@page.route('/order_open', methods=['GET', 'POST'])
def order_open():
    const = constants
    order = session['order']
    department = session['department']
    return render_template('order_open_print_form.html', order=order, department=department, const=const)
