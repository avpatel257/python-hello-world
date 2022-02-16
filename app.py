from service import catalog_service;

from flask import Flask
from flask import jsonify

import json
def main():
    tracks = catalog_service.get_tracks()
    print(type(tracks))
    # print(res)


if __name__ == "__main__":
   main()