# app/models.py


from app import db


class Veiculo(db.Model):
    """
    Create a Veiculo table
    """

    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(40),nullable=False)
    modelo = db.Column(db.String(50),nullable=False)
    cor = db.Column(db.String(30),nullable=False)
    ano = db.Column(db.Integer,nullable=False)
    preco = db.Column(db.Float,nullable=False)
    descricao = db.Column(db.Text)
    novo = db.Column(db.Boolean,nullable=False)
    #data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return '<Veiculo: {}>'.format(self.name)
