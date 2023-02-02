

class DocumentToProcess:
    def __init__(self):
        self.file_path = ""


class DocumentWorkload:
    def __init__(self):
        self.pending: list[DocumentToProcess] = []
        self.processed: list[DocumentToProcess] = []
