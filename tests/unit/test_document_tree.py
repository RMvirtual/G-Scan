from document_tree import DocumentTree


class TestDocumentTree:
    def test_should_determine_job_branches(self) -> None:
        tree = DocumentTree()
        tree.create_job_branch("GR190100100")
        tree.create_job_branch("GR190100200")

        assert len(tree.job_branches) == 2
