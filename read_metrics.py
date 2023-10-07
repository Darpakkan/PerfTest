import time
import numpy as np
from models import Embeddings
from server import db, redis_client, app


def read_from_redis():
    start = time.time()
    embeddings = []

    pattern = "embedding:*"

    keys = redis_client.keys(pattern)

    pipeline = redis_client.pipeline()
    for key in keys:
        pipeline.hget(key, "embedding")

    res = pipeline.execute()

    mid = time.time()

    # print("\n\ntime taken to fetch from redis: ")
    # print(mid-start)
    # print('\n\n')

    for key, result in zip(keys, res):
        if result is not None:
            doc_id, num = (str(key).split(":")[1], str(key).split(":")[2])
            embeddings.append((doc_id, num, np.frombuffer(result, dtype=np.float64)))

    print(f"\nShape of Embeddings Read from Redis: {embeddings[0][2].shape}\n")

    return (time.time() - start, embeddings)


def read_from_sqlite():
    start = time.time()
    embeddings = []
    with app.app_context():
        query_result = db.session.query(Embeddings).all()
    for item in query_result:
        embeddings.append(
            (item.docId, item.num, np.frombuffer(item.embedding, dtype=np.float64))
        )
    print(f"\nShape of Embeddings Read from SqLite: {embeddings[0][2].shape}\n")
    return (time.time() - start, embeddings)


def main():
    elapsed_time_redis, embedding_redis = read_from_redis()
    elapsed_time_sqlite, embedding_sqlite = read_from_sqlite()

    print(
        f"\nRead from Redis - Time: {elapsed_time_redis}s, No of Embeddings: {len(embedding_redis)}\n"
    )

    print(
        f"\nRead from SQLite - Time: {elapsed_time_sqlite}s, No of Embeddings: {len(embedding_sqlite)}\n"
    )

    print(f"\nRedis Speeeedup: {elapsed_time_sqlite/elapsed_time_redis}x 🔥🔥🔥")


if __name__ == "__main__":
    main()
