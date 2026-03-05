from config.database import app, db
from controllers.user_controller import user_blueprint

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
