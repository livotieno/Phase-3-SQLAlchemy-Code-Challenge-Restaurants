from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# engine = create_engine('mysql+mysqlconnector://root:Freemo@254#>@localhost:3306/jaribu1')
engine = create_engine('sqlite:///Restaurants.db')


class Customers(Base):
    __tablename__ = 'Customers'
    customer_id = Column (Integer(),primary_key=True)
    first_name = Column(String (50))
    last_name = Column(String (50))
    
    def __init__(self, customer_id, first_name, last_name):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        
    def __repr__(self):
        pass
    
       



class Restaurants(Base):
    __tablename__ = 'Restaurants' 
    Restaurants_id = Column (Integer(),primary_key=True)  
    name =  Column(String (40))
    price = Column(Integer ())
    
    def __init__(self, Restaurants_id, name, price):
        self.Restaurants_id = Restaurants_id
        self.name = name
        self.price = price
        
    def __repr__(self):
        pass
        
    
    
    
    
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

