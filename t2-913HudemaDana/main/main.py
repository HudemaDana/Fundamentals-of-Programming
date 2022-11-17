from repository.repo_taxi import RepoTaxi
from service.serv_rider import Service
from ui.ui import UI


def main():
    repo = RepoTaxi()
    serv = Service(repo)
    new_ui = UI(serv)
    new_ui.controller()


main()
