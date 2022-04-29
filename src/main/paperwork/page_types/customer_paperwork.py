from src.main.paperwork.page_types.a4 import A4Page

class CustomerPaperworkPage(A4Page):
    def __init__(self, packet, job_reference, paperwork_image):
        super().__init__(packet)

        self.draw_barcode(job_reference)
        self.draw_job_reference(job_reference)
        self.draw_paperwork_type("Customer Paperwork")
        self.draw_image(paperwork_image)
        self.save()