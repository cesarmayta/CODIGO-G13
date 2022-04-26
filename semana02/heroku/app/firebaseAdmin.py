## para conectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

### para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()