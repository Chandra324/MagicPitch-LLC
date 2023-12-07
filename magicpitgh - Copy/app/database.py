# app/database.py
import databases
import sqlalchemy
DATABASE_URL = "mysql+mysqlconnector:3306//userpassword","root","root"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String, index=True),
    sqlalchemy.Column("age", sqlalchemy.String),
)
async def create_table():
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)


async def insert_user(name: str, age: str):
    query = users.insert().values(name=name, age=age)
    await database.execute(query)
