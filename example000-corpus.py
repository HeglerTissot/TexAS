import json
import texas as tx

# create a document
mydoc1 = tx.Document("Hello world!!! How are you today?", "en") # pType = "statement")
mydoc1.meta().set("authors","hegler,yiwen,celine,yuqian")
mydoc1.date().setTimestamp("2021-01-19T14:44") # ??
mydoc1.setTokenList( ["Hello", "world", "!","!","!","How","are","you","today","?"] )
mydoc1.addTokenView( "POS", ["?", "NOUN", "PUNCT","PUNCT","PUNCT","?","VERB","PRON","?","PUNCT"] )
mydoc1.setSentenceList( [5,10] )

# create another document reversing from the previous document JSON 
mydoc2 = tx.reverse(mydoc1.TAS())

print("==========")
print("mydoc2")
print("----------")
print( "--- Token List" )
print( mydoc2.getTokenList() )
print( "--- Token Info" )
print( json.dumps( mydoc2.getTokenInfo() ) )
print( "--- Sentence Info" )
print( json.dumps( mydoc2.getSentenceInfo() ) )
print( "--- Document TAS" )
print( json.dumps(mydoc2.TAS()) )

# create a corpus with a single document
mycorpus1 = tx.Corpus()
mycorpus1.bits().add(mydoc2)

# create a second corpus duplicating documents in the first (reverse)
mycorpus2 = tx.reverse(mycorpus1.TAS())

print("==========")
print("mycorpus2")
print("----------")
print( "--- Corpus TAS" )
print ( json.dumps(mycorpus2.TAS()) )

print("")
print("end!")
print("")

