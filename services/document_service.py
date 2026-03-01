from utils.file_handler import read_json, write_json
from utils.id_generator import generate_id
from config import DOCUMENTS_FILE


class DocumentService:

    def save_document(self, command, explanation, language):

        data = read_json(DOCUMENTS_FILE)

        doc_id = generate_id("doc")

        data[doc_id] = {
            "command": command,
            "language": language,
            "explanation": explanation
        }

        write_json(DOCUMENTS_FILE, data)