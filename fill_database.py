from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
#from prokarotic_declarative import Species, Base, Gene, Bacteria_Gene, Primer
from prokarotic_declarative import Species, Base
 
engine = create_engine('sqlite:///prokarotic.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def is_na(key, value):
	if value == 'na':
		key = 0
	elif value != 'na' and key != 'GC':
		value = int(value.replace(',', ''))
	elif value != 'na' and key == 'GC':
		value = float(value.replace(',', ''))

	return value

def insert_values(fileLine):
	# Insert a species of bacteria (E. coli) in the species table
	
	sLine = fileLine.split('\t')

	Species = 'E. coli'
	Serotype = sLine[0]
	Strain = sLine[1]
	Accession = sLine[2]
	G_size = is_na('G_size', sLine[3])
	count_plasmid = is_na('plasmid_count', sLine[4])
	GC = is_na('GC', sLine[5])
	count_gene = is_na('gene_count', sLine[6])
	sTechnology = sLine[7]
	additional_info = sLine[8]
	
	new_species = Species(genus_name=Species, serotype = Serotype, strain=Strain, accession=Accession, GC_percentage=GC, gene_count=count_gene, plasmid_count=count_plasmid, sequencing_technology=sTechnology, description=additional_info)
	
	session.add(new_species)
	session.commit()
 
# Insert an Address in the gene table
#new_gene = Gene(gene_name='stx2', species=new_species)
#session.add(new_gene)
#session.commit()

 
with open('mimiDb.txt', 'r') as inputFile:
	firstLine = inputFile.readline()
	
	lines = inputFile.readlines()
	for line in lines:
		line = line.replace('\n', '')
		insert_values(line)
		
'''
Press ENTER or type command to continue
Traceback (most recent call last):
  File "fill_database.py", line 54, in <module>
    insert_values(line)
  File "fill_database.py", line 38, in insert_values
    new_species = Species(genus_name=Species, serotype = Serotype, strain=Strain, accession=Accession, GC_percentage=GC, gene_count=count_gene, plasmid_count=count_plasmid, sequencing_technology=sTechnology, description=additional_info)
TypeError: 'str' object is not callable

shell returned 1

Serotype^IStrain name^IAccession # (GenBank)^ISize of Chromosome (bp)^INo. of Plasmids^IG+C (%)^I# of Genes^ISequencing Technology^IStrain information$
class Species(Base):
	__tablename__ = 'species'
	# Here we define columns for the table species
	# Notice that each column is also a normal Python instance attribute.
	id = Column(INTEGER, primary_key=True)
	genus_name = Column(String(250), nullable=False)
	serotype = Column(String(20), nullable=False)
	strain = Column(String(20), nullable=False)
	description = Column(String(250), nullable=False)
	accession = Column(String(15), nullable=False)
	GC_percentage = Column(FLOAT(4), nullable=False)
	genome_size = Column(INTEGER, nullable=False)
	gene_count = Column(INTEGER, nullable=False)
	plasmid_count = Column(INTEGER, nullable=False)
	#plasmids = Column(String(250), nullable=False)
	#PAI_count = Column(INTEGER, nullable=False)
	#sequence = Column(String(250), nullable=False)
	sequencing_technology = Column(String(20), nullable=False)
'''
