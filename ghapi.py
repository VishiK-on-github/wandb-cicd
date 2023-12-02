import os
from ghapi.core import GhApi

owner, repo = os.environ["REPO"].split("/")

api = GhApi(owner=owner, repo=repo)

api.issues.create(os.environ["NUMBER"], "Hi, I am making a comment using ghapi !")
