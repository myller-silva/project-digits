# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracao do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://teste:teste@localhost/teste_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *
from models import *

if __name__ == '__main__':
    # Cria o banco de dados se não existir
    db.create_all()
    # Inicia a aplicação Flask 
    app.run(debug=True, host='0.0.0.0')



# import numpy as np
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
# def plot_matrix(matrix_str):
#     matrix = np.array(eval(matrix_str))
#     plt.imshow(matrix, cmap='gray')  # Usando o mapa de cores 'gray'
#     plt.axis('off')  # Removendo os eixos
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()
#     return base64.b64encode(image_png).decode('utf-8')

# @app.route('/plot_matrix', methods=['GET', 'POST'])
# def plot():
#     if request.method == 'POST':
#         matrix_str = request.form['matrix']
#         image_base64 = plot_matrix(matrix_str)
#         return f'<img src="data:image/png;base64,{image_base64}" alt="Matrix Plot">'
#     else:
#         return render_template('plot_matrix.html')


if __name__ == '__main__':
    app.run(debug=True)
