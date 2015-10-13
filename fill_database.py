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
	# Handles na issues as well as conversion to int/float
	if value == 'na' or value == 'NA' or value == 'Na': #value = value.ascii_lowercase()
		value = 0
	elif value != 'na' and key != 'GC': #this will need to be update in the future
		value = int(value.replace(',', ''))
	elif value != 'na' and key == 'GC':
		value = float(value.replace(',', ''))

	return value

def insert_values(fileLine):
	# Insert a species of bacteria (E. coli) in the species table
	
	sLine = fileLine.split('\t')

	name_genus = 'E. coli'
	Serotype = sLine[0]
	Strain = sLine[1]
	Accession = sLine[2]
	G_size = is_na('G_size', sLine[3])
	count_plasmid = is_na('plasmid_count', sLine[4])
	GC = is_na('GC', sLine[5])
	count_gene = is_na('gene_count', sLine[6])
	sTechnology = sLine[7]
	additional_info = sLine[8]
	
	new_species = Species(genus_name=name_genus, serotype = Serotype, genome_size=G_size, strain=Strain, accession=Accession, GC_percentage=GC, gene_count=count_gene, plasmid_count=count_plasmid, sequencing_technology=sTechnology, description=additional_info)
	
	session.add(new_species)
	session.commit()
 
# Insert an Address in the gene table
#new_gene = Gene(gene_name='stx2', species=new_species)
#session.add(new_gene)
#session.commit()

count = 2 
with open('mimiDb.txt', 'r') as inputFile:
	firstLine = inputFile.readline()
	
	lines = inputFile.readlines()
	for line in lines:
		print count
		line = line.replace('\n', '')
		insert_values(line)
		count+=1
