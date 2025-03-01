from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.types import PickleType
import json
from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

# Association table for many-to-many relationship (if needed for multiple subjects)
service_subject = db.Table('service_subject',
    db.Column('service_id', db.Integer, db.ForeignKey('services.id'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=True, unique=True)
    password = db.Column(db.String(128), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(20))

    expert_profile = db.relationship("Expert", uselist=False, back_populates="user")
    def set_password(self, password):
        """Hashes the password using Flask-Bcrypt"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if the password matches the hashed password"""
        return bcrypt.check_password_hash(self.password, password)

expert_project_types = db.Table(
    'expert_project_types',
    db.Column('expert_id', db.Integer, db.ForeignKey('experts.id'), primary_key=True),
    db.Column('project_type_id', db.Integer, db.ForeignKey('project_types.id'), primary_key=True)
)

expert_subjects = db.Table(
    'expert_subjects',
    db.Column('expert_id', db.Integer, db.ForeignKey('experts.id'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.id'), primary_key=True)
)

expert_services = db.Table(
    "expert_services",
    db.Column("expert_id", db.Integer, db.ForeignKey("experts.id"), primary_key=True),
    db.Column("service_id", db.Integer, db.ForeignKey("services.id"), primary_key=True),
)

class Expert(db.Model):
    __tablename__ = 'experts'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    expertise = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    biography = db.Column(db.Text, nullable=True)
    education = db.Column(db.String(255), nullable=True)
    languages = db.Column(db.String(255), nullable=True)
    profile_picture = db.Column(db.Text, nullable=True)

    user = db.relationship("User", back_populates="expert_profile")
    services = db.relationship("Service", secondary=expert_services, backref="experts")
    # Many-to-Many Relationships
    project_types = db.relationship('ProjectType', secondary=expert_project_types, backref='experts')
    subjects = db.relationship('Subject', secondary=expert_subjects, backref='experts')

    rating_avg = db.Column(db.Float, default=0.0)
    total_reviews = db.Column(db.Integer, default=0)
    success_rate = db.Column(db.Float, default=0.0)
    is_ai_free = db.Column(db.Boolean, default=False)
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    expert = db.relationship('Expert', backref='ratings')
    user = db.relationship('User', backref='ratings')

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    
    expert = db.relationship('Expert', backref='comments')
    # user = db.relationship('User', backref='comments', foreign_keys=[user_id])

class ProjectType(db.Model):
    __tablename__ = 'project_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    services = db.relationship('Service', backref='project_type')

class Conversation(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project_requests.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Remove the backref from here and keep it simple
    messages = db.relationship('Message', lazy=True, backref='conversation')

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    # Relationship to services
    services = db.relationship('Service', backref='subject')  # Adjusted to single subject relationship
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)  # Base price
    price_per_page = db.Column(db.Float, nullable=False)  # Price per page
    unit = db.Column(db.String(50), nullable=True)
    
    # Foreign key for subject
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)

    # Relationship to project types
    project_type_id = db.Column(db.Integer, db.ForeignKey('project_types.id'), nullable=False)

    def calculate_total_price(self, number_of_pages):
        """
        Calculate total price based on base price and number of pages
        
        :param number_of_pages: Number of pages for the project
        :return: Total price for the project
        """
        return self.base_price + (self.price_per_page * number_of_pages)

class ProjectRequest(db.Model):
    __tablename__ = 'project_requests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'))
    project_title = db.Column(db.Text, nullable=False)
    project_type_id = db.Column(db.Integer, db.ForeignKey('project_types.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    project_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    deadline = db.Column(db.DateTime, nullable=False)
    attachments = db.Column(db.String, nullable=True)  
    number_of_pages = db.Column(db.Integer, nullable=False)

    # Relationships
    user = db.relationship('User', backref='requests')
    expert = db.relationship('Expert', backref='requests')
    project_type = db.relationship('ProjectType', backref='requests')
    subject = db.relationship('Subject', backref='requests')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'expert_id': self.expert_id,
            'project_title': self.project_title,
            'project_type': self.project_type.to_dict() if self.project_type else None,
            'subject': self.subject.to_dict() if self.subject else None,
            'project_description': self.project_description,
            'status': self.status,
            'deadline': self.deadline,
            'attachments': self.attachments,
            'number_of_pages': self.number_of_pages, 
        }

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), nullable=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    attachments = db.Column(db.String, nullable=True)
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_messages')
    expert = db.relationship('Expert', backref='messages')  # Optional expert relationship
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Message from {self.sender.username} to {self.receiver.username if self.receiver else self.expert.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'conversation_id': self.conversation_id,
            'sender': self.sender.username,
            'receiver': self.receiver.username if self.receiver else None,
 
           'expert': self.expert.name if self.expert else None,
            'content': self.content,
            'attachments': self.attachments.split('||') if self.attachments else [],
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'read': self.read,
        }