from trashcli.put.candidate import Candidate
from trashcli.put.same_volume_gate import SameVolumeGate
from trashcli.put.trashee import Trashee


class TrashingChecker:
    def __init__(self, trash_dir_volume):
        self.trash_dir_volume = trash_dir_volume

    def file_could_be_trashed_in(self,
                                 trashee,  # type: Trashee
                                 candidate,  # type: Candidate,
                                 ):
        return candidate.gate.can_trash_in(trashee, candidate, self.trash_dir_volume)
