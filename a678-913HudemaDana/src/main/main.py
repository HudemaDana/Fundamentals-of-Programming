from src.repository.Repo_Activity import RepoActivity
from src.repository.Repo_TextFile_Activity import RepoFileTextActivity
from src.repository.Repo_Bin_Activity import RepoBinActivity
from src.repository.Repo_Person import RepoPerson
from src.repository.Repo_TextFile_Person import RepoFileTextPerson
from src.repository.Repo_Bin_Person import RepoBinPerson
from src.services.Service_Undo_Redo import ServiceUndoRedo
from src.services.Service_Activity import ServiceActivity
from src.services.Service_Person import ServicePerson
from src.ui.UI import UI
from src.settings.settings import SettingsConfig


def main():
    setting = SettingsConfig()
    repo, activity, person = setting.read_setting()
    if str(repo) == "inmemory":
        repoAct = RepoActivity()
        repoPers = RepoPerson(repoAct)
    elif str(repo) == "textfiles":
        repoAct = RepoFileTextActivity()
        repoPers = RepoFileTextPerson(repoAct)
    elif str(repo) == "binaryfiles":
        repoAct = RepoBinActivity()
        repoPers = RepoBinPerson(repoAct)


    servPers = ServicePerson(repoPers, repoAct)
    servActv = ServiceActivity(repoAct, repoPers)
    servUndoRedo = ServiceUndoRedo(repoAct, repoPers)
    new_ui = UI(servPers, servActv, servUndoRedo)
    new_ui.controller()


main()
