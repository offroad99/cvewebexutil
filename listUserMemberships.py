import json
import cveLogger
import sys
import getrooms, getMemberId, deleteMembership
import argparse

def listUserMemberships(ACCESS_TOKEN, email, roomName, delete = False):
    for room in getrooms.getRooms(ACCESS_TOKEN, roomName):
        foundPerson = getMemberId.getRoomMember(ACCESS_TOKEN, room.get('id'), email)
        if foundPerson is not None:
            #print(foundPerson.get("personDisplayName"))
            cveLogger.mylogger(f'{cveLogger.lineno()} Found {foundPerson.get("personDisplayName")} in room {room.get("title")}')
            yield f'User {foundPerson.get("personDisplayName")} found in room {room.get("title")}'
            if delete:
                deleteMembership.deleteMembership(ACCESS_TOKEN, foundPerson.get("id"))
    return None


if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    parser = argparse.ArgumentParser(description='Hidden Options', epilog='Use at your own risk :)')
    parser.add_argument("-A", "--Action", default="False", required=False)
    if parser.parse_args().Action == 'DELETE':
        Action = True
    else:
        Action = False
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin listUserMemberships')
    ACCESS_TOKEN = input('bearer token: ')
    emailAddress = input('eMail Address: ')
    roomName = input('Room name or pattern: ')
    for foundInRoom in listUserMemberships(ACCESS_TOKEN, emailAddress, roomName, Action):
        print(f'Iterating: {foundInRoom}')