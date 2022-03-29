from src.main.paperwork.page_types.a4 import A4Page

class CustomerPaperworkPage(A4Page):
    def __init__(self, packet, job_reference, paperwork_image):
        super().__init__(packet)

        self.draw_barcode_on_page(job_reference)
        self.draw_job_reference_on_page(job_reference)
        self.draw_paperwork_type_on_page("Customer Paperwork")
        self.draw_image_on_page(paperwork_image)
        self.save()