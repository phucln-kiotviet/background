from src.database import session_scope
from sqlalchemy.sql import func
from .models import Ansibles
from sqlalchemy import or_
import json


def create():
    with session_scope() as s:
        ansible_object = Ansibles(
            inventory="inventory_name3", playbook="playbook_name3")
        s.add(ansible_object)
        s.commit()
        s.refresh(ansible_object)
        return ansible_object


def get_by_id(ansible_id):
    with session_scope() as s:
        ansible = s.query(Ansibles).filter(Ansibles.id == ansible_id).first()
        s.expunge(ansible)
        return ansible


def find(keyword):
    with session_scope() as s:
        ansible = s.query(Ansibles).filter(
            or_(Ansibles.inventory == keyword, Ansibles.playbook == keyword)).all()
        s.expunge_all()
        return ansible


def get_list():
    with session_scope() as s:
        ansibles = s.query(Ansibles, func.count(
            Ansibles.id).over().label("total")).limit(1).offset(2).all()
        s.expunge_all()
        return ansibles
