#! tools-env/bin/python
import pymongo
Uin = raw_input('This command deletes all users.  Are you sure you want to continue [Y/n]')
Uin = Uin.lower()

if Uin == 'y':
    pymongo.MongoClient().project.drop_collection('User')