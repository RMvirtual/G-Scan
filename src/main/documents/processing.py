


class DocumentToProcess:
    def __init__(self):
        self.file_path = ""
        self.tree_item_id = None



class DocumentWorkload:
    def __init__(self):
        self.pending: list[DocumentToProcess] = []
        self.processed: list[DocumentToProcess] = []
