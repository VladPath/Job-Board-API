from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy import Float
from sqlalchemy import DateTime

from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM

from base.database import Base




class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True)

class JobType(Enum):
    fulltime = 'Fulltime'
    parttime = 'Parttime'


class Vacancy(Base):
    __tablename__ = 'vacancy'

    id = Column(Integer, primary_key=True)
    title = Column(String(50) )
    description = Column(String(355))
    location = Column(String(50))
    salary = Column(Float)
    job_type = Column(ENUM(JobType,name='job_type'), default=JobType.fulltime)
    company_id = Column(Integer, ForeignKey('company.id'))

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(50), unique=True)
    location = Column(String(50))
    description = Column(String(255))
    website = Column(String(255))
    industry = Column(String(50))
    count_workers = Column(Integer)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    role_id = Column(Integer, ForeignKey("role.id"))

class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    resume_id = Column(Integer)
    age = Column(Integer)
    role_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Resume(Base):
    __tablename__ = 'resume'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    skills = Column(String(255))
    location = Column(String(50))
    job_type = Column(ENUM(JobType,name='job_type'), default=JobType.fulltime)
    salary = Column(Float)
    age = Column(Integer)

class VacancyWorker(Base):
    __tablename__ = 'vacancy_worker'
    id = Column(Integer, primary_key=True, index=True)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    worker_id = Column(Integer, ForeignKey('worker.id'))
