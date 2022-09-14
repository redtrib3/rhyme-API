from fastapi import FastAPI	
import rhymedb as rdb

app = FastAPI()


@app.get('/')
def index_page():
	return {"Description":"GET Rhyming words for a word.", "documentation":'visit /docs'}


@app.get('/rhyme/{word}')
def get_rhyming_words(word: str, count: int = None):

	rhymes = rdb.rhymes_with(word)

	if count:
		rhymesUpdated = rhymes[0:count]
		return {word: rhymesUpdated,"COUNT":len(rhymesUpdated),"maxCount":len(rhymes)}

	else:
		return {word:rhymes, "COUNT":len(rhymes)}