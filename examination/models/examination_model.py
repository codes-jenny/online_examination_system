from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL =  'mysql+pymysql://root:khush952004@localhost/ONLINE_EXAM_SYSTEM'


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Reflect the existing tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Map to the existing tables
Examination = Base.classes.examination
UserResponse= Base.classes.userresponses
Question = Base.classes.question
Option = Base.classes.options
QuestionPaper = Base.classes.questionpaper
CorrectAnswer = Base.classes.correctanswers
# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)