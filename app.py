from flask import Flask, redirect, url_for, flash
from config import Config
from extensions import db, login_manager
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    app.secret_key = "clave_super_secreta"

    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB
    @app.errorhandler(413)
    def too_large(e):
        if request.content_type.startswith("multipart/form-data"):
            flash("❌ La imagen supera el tamaño permitido (5MB)")
            return redirect(url_for("admin.productos"))
        return {"error": "File too large"}, 413

    db.init_app(app)
    #login_manager.init_app(app)

    from routes.public import public_bp
    from routes.admin import admin_bp
    from routes.ia import ia_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(ia_bp, url_prefix="/ia")

    # 🔥 AUTO CREAR BD
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, "database")

    if not os.path.exists(db_path):
        os.makedirs(db_path)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)