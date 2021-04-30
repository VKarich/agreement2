from docxtpl import DocxTemplate

INPUT_FILENAME = "demo_in.docx"
OUTPUT_FILENAME = "demo.docx"


class Templater:
    @staticmethod
    def generate_file(model):
        doc = DocxTemplate(INPUT_FILENAME)
        doc.render(model)
        doc.save(OUTPUT_FILENAME)
