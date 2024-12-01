from website.database import create_db_connection
from website.views import views as views_blueprint
from website.api import api as api_blueprint

app, Session = create_db_connection()

app.register_blueprint(views_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)