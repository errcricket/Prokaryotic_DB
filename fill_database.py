from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from prokarotic_declarative import Species, Base, Gene, Bacteria_Gene, Primer
 
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
 
# Insert a species of bacteria (E. coli) in the species table
new_species = Species(genus_name='E. coli', strain='RM9387', serotype='O104:H7', accession='CP009104', GC_percentage=50.8)
session.add(new_species)
session.commit()
 
# Insert an Address in the gene table
new_gene = Gene(gene_name='stx2', species=new_species)
session.add(new_gene)
session.commit()
