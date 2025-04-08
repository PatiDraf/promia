from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projet(db.Model):
    id_projet = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date, nullable=False)
    statut = db.Column(db.String(50), default="En cours")

    def __repr__(self):
        return f'<Projet {self.nom}>'

class Planning(db.Model):
    id_planning = db.Column(db.Integer, primary_key=True)
    id_projet = db.Column(db.Integer, db.ForeignKey('projet.id_projet'), nullable=False)
    date_creation = db.Column(db.Date, nullable=False)
    version = db.Column(db.String(50), nullable=False)
    fichier_nom = db.Column(db.String(255), nullable=False)

class Jalon(db.Model):
    id_jalon = db.Column(db.Integer, primary_key=True)
    id_projet = db.Column(db.Integer, db.ForeignKey('projet.id_projet'), nullable=False)
    nom = db.Column(db.String(255), nullable=False)

class Tache(db.Model):
    id_tache = db.Column(db.Integer, primary_key=True)
    id_projet = db.Column(db.Integer, db.ForeignKey('projet.id_projet'), nullable=False)
    id_jalon = db.Column(db.Integer, db.ForeignKey('jalon.id_jalon'), nullable=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_debut = db.Column(db.Date, nullable=False)
    duree_estimee = db.Column(db.Integer, nullable=False)
    statut = db.Column(db.String(50), default="Non démarré")
    priorite = db.Column(db.String(50), default="Normale")
