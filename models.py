from server import db

# SqlAlchemy Schema


class Document(db.Model):
    __tablename__ = "documents"
    # Basic Stuff
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    embeddings = db.relationship(
        "Embeddings", back_populates="document"
    )  # SqlAlchemy ftw!!!

    # Constructor
    def __init__(self, name: str, content: str, text_embeddings: int):
        self.name = name
        self.content = content
        self.text_embeddings = text_embeddings
        pass


class Embeddings(db.Model):
    __tablename__ = "embeddings"

    # Basic Stuff
    id = db.Column(db.Integer, primary_key=True)
    docId = db.Column(db.Integer, db.ForeignKey("documents.id"))  # SqlAlchemy ftw!!!
    num = db.Column(db.Integer)
    text = db.Column(db.Text)
    embedding = db.Column(db.BLOB)
    document = db.relationship("Document", back_populates="embeddings")

    # Constructors
    def __init__(self, id: int, num: int, docId: int, text: str, embedding: str):
        self.id
        self.num = num
        self.docId = docId
        self.text = text
        self.embedding = embedding

    def __init__(self, num: int, docId: int, text: str, embedding: str):
        self.num = num
        self.docId = docId
        self.text = text
        self.embedding = embedding
