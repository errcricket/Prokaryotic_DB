import os
import sys
from sqlalchemy import Column, ForeignKey, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import \
	BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
	DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
	LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
	NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
	TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

Base = declarative_base()

class Species(Base):
	 __tablename__ = 'species'
	 # Here we define columns for the table species
	 # Notice that each column is also a normal Python instance attribute.
	 id = Column(INTEGER, primary_key=True)
	 genus_name = Column(String(250), nullable=False)
	 strain = Column(String(20), nullable=False)
	 serotype = Column(String(20), nullable=False)
	 description = Column(String(250), nullable=False)
	 accession = Column(String(15), nullable=False)
	 GC_percentage = Column(FLOAT(4), nullable=False)
	 genome_size = Column(INTEGER, nullable=False)
	 gene_count = Column(INTEGER, nullable=False)
	 plasmid_count = Column(INTEGER, nullable=False)
	 plasmids = Column(String(250), nullable=False)
	 PAI_count = Column(INTEGER, nullable=False)
	 sequence = Column(String(250), nullable=False)
	 sequencing_technology = Column(String(20), nullable=False)

class Gene(Base):
	 __tablename__ = 'gene'
	 # Here we define columns for the table gene.
	 # Notice that each column is also a normal Python instance attribute.
	 id = Column(INTEGER, primary_key=True)
	 gene_name = Column(String(250))
	 gene_sequence = Column(String(250))

class Bacteria_Gene(Base):
	 __tablename__ = 'genes_in_bacteria'
	 # Here we define columns for the table primer
	 # Notice that each column is also a normal Python instance attribute.
	 species_id = Column(INTEGER, ForeignKey('species.id'), primary_key=True)
	 species = relationship(Species)
	 gene_id = Column(INTEGER, ForeignKey('gene.id'), primary_key=True)
	 gene = relationship(Gene)

class Primer(Base):
	 __tablename__ = 'primer'
	 # Here we define columns for the table primer
	 # Notice that each column is also a normal Python instance attribute.
	 id = Column(INTEGER, primary_key=True)
	 name = Column(String(250), nullable=False)
	 primer_sequence = Column(String(50), nullable=False)
	 gene_id = Column(INTEGER, ForeignKey('gene.id'))
	 gene = relationship(Gene)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///prokarotic.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine) 
