"""The application's model objects"""
from emp.model.meta import Session, Base

from emp.model.user import User

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
