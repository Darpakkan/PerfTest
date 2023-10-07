from embedding import embeddingModel
from server import app, db, redis_client
from models import Document, Embeddings
import argparse
import random
import numpy as np
import read_metrics

# Parse the Command Line Arguments
parser = argparse.ArgumentParser(description="Populate the database with random data")
parser.add_argument("--documents", type=int, help="Number of documents to generate")
parser.add_argument("--parts", type=int, help="Number of parts per document")
parser.add_argument("--words", type=int, help="Minimum number of words per part")
args = parser.parse_args()

if not all([args.documents, args.parts, args.words]):
    parser.error("All arguments are required.")


# Random Text
def generate_random_text(words: int):
    return " ".join(
        [
            "".join(
                random.choices("abcdefghijklmnopqrstuvwxyz ", k=random.randint(1, 10))
            )
            for _ in range(words)
        ]
    )


print("------------------STARTING TEST--------------------")


print("\n\nPopulating Redis and SQLite Database......\n\n")

print(f"\nShape of Embeddings stored: {np.random.random((768,)).shape}\n")

# Create the tables
with app.app_context():
    for key in redis_client.scan_iter("embedding:*"):
        redis_client.delete(key)

    db.drop_all()

    db.create_all()

    # Populate the Sqlite Database with random documents and embeddings
    for doc in range(1, args.documents + 1):
        content = generate_random_text(args.words * args.parts)

        document = Document(name=f"Document {doc}", content=content, text_embeddings=0)
        document.id = doc
        db.session.add(document)
        db.session.commit()

        # For this document fill the embeddings table
        for part in range(1, args.parts + 1):
            text = generate_random_text(args.words)
            embedding = np.random.random((768,))

            embedding_data = Embeddings(
                num=part, docId=doc, text=text, embedding=embedding.tobytes()
            )
            embedding_data.document = document
            db.session.add(embedding_data)

            ## We store only the embedding field for each row to save space
            redis_field = {
                "embedding": embedding.tobytes(),
            }

            redis_key = f"embedding:{doc}:{part}"
            redis_client.hmset(redis_key, redis_field)

        db.session.commit()

print("------------------------------------------------------------------")

print("Running Read Test......\n\n")

read_metrics.main()

print("\n\n------------------FINISHING TEST--------------------")
