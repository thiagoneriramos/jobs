# app/home/views.py
# encoding: utf-8

import sys
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from forms import VeiculoForm
from .. import db
from ..models import Veiculo


from . import home


reload(sys)
sys.setdefaultencoding('utf8')

@home.route('/', methods=['GET', 'POST'])
def list_veiculo():
    """
    List all veiculo
    """

    veiculos = Veiculo.query.all()

    return render_template('veiculos.html',
                           veiculos=veiculos, title="Veiculos")

@home.route('/add', methods=['GET', 'POST'])
def add_veiculo():
    """
    Add a veiculo to the database
    """
    add_veiculo = True

    form = VeiculoForm()
    if form.validate_on_submit():
        veiculo = Veiculo(marca=form.marca.data,
                                modelo =form.modelo.data,
                                cor = form.cor.data,
                                ano = form.ano.data,
                                preco = form.preco.data,
                                descricao = form.descricao.data,
                                novo= form.novo.data
                               )
        try:
            # add veiculo to the database
            db.session.add(veiculo)
            db.session.commit()
            flash('Você adicionou um veículo com sucesso.')
        except:
            # in case veiculo name already exists
            flash('Erro: Nome de veículo já existe.')

        # redirect to veiculo page
        return redirect(url_for('home.list_veiculo'))

    # load veiculo template
    return render_template('veiculo.html', action="Add",
                           add_veiculo=add_veiculo, form=form,
                           title="Add Veiculo")

@home.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_veiculo(id):
    """
    Edit a veiculo
    """

    add_veiculo = False

    veiculo = Veiculo.query.get_or_404(id)
    form = VeiculoForm(obj=veiculo)
    if form.validate_on_submit():
        veiculo.marca = form.marca.data
        veiculo.modelo = form.modelo.data
        veiculo.cor = form.cor.data
        veiculo.ano = form.ano.data
        veiculo.preco = form.preco.data
        veiculo.descricao = form.descricao.data
        veiculo.novo = form.novo.data
        db.session.commit()
        flash('Você editou um veículo com sucesso.')

        # redirect to the veiculo page
        return redirect(url_for('home.list_veiculo'))

    form.marca.data = veiculo.marca
    form.modelo.data = veiculo.modelo
    form.cor.data = veiculo.cor
    form.ano.data = veiculo.ano
    form.preco.data = veiculo.preco
    form.descricao.data = veiculo.descricao
    form.novo.data = veiculo.novo

    return render_template('veiculo.html', action="Edit",
                           add_veiculo=add_veiculo, form=form,
                           veiculo=veiculo, title="Edit Veiculo")

@home.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_veiculo(id):
    """
    Delete a veiculo from the database
    """

    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    flash('Você deletou um veículo com sucesso.')

    # redirect to the veiculo page
    return redirect(url_for('home.list_veiculo'))

    return render_template(title="Delete Veiculo")
