from data_structures_new import DocumentTree
from documents import DocumentType


class TestDocumentTree:
    def test_should_create_job_branches(self) -> None:
        tree = DocumentTree()
        tree.create_job_branch("GR190100100")
        tree.create_job_branch("GR190100200")

        assert len(tree.jobs) == 2
        assert len(tree.pending) == 0

    def test_should_create_pending_document(self) -> None:
        tree = DocumentTree()
        result = tree.create_pending_document(self._example_document_type())

        assert result.type.short_code == "ShortCode1"
        assert len(tree.pending) == 1
        assert len(tree.jobs) == 0

    def test_should_move_pending_document_to_job_branch(self) -> None:
        tree = DocumentTree()
        job_branch = tree.create_job_branch("GR190100100")

        pending_item = tree.create_pending_document(
            self._example_document_type()
        )

        assert pending_item.parent is tree.pending
        assert len(tree.pending) == 1
        assert len(job_branch) == 0

        job_branch.append(pending_item)
        assert pending_item.parent is job_branch
        assert len(job_branch) == 1
        assert len(tree.pending) == 0

    def _example_document_type(self) -> DocumentType:
        return DocumentType(
            "ShortCode1",
            "FullName1",
            "AnalysisCode1",
        )
