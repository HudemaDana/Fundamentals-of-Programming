from src.exceptions.Exception import ServiceUndoRedoException


class ServiceUndoRedo():
    def __init__(self, repo_act, repo_pers):
        self.repo_activity = repo_act
        self.undo = []
        self.redo = []

    def add_to_undo_list(self, item):
        self.redo.clear()
        self.undo.append(item)

    def undo_operation(self):
        if len(self.undo) == 0:
            raise ServiceUndoRedoException("No more undo to be done")
        self.undo[-1][1]()
        if len(self.undo[-1]) == 4:
            for i in range(len(self.undo[-1][2])):
                self.repo_activity.repo_activity[self.undo[-1][2][i]][4].append(int(self.undo[-1][3]))

        self.redo.append(self.undo[-1])
        self.undo.pop()

    def redo_operation(self):
        if len(self.redo) == 0:
            raise ServiceUndoRedoException("No more redo to be done")
        self.redo[-1][0]()
        self.undo.append(self.redo[-1])
        self.redo.pop()