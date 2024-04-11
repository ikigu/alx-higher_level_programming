from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
	__tablename__= 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	nickname = Column(String)

	def __repr__(self):
		return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

Base.metadata.create_all(engine)

# create a new user

ed_user = User(name='ed', fullname='Ed Jones', nickname='EJ')
session = Session()

session.add(ed_user)
