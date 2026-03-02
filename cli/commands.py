from services.translation_service import TranslationService
from services.document_service import DocumentService


translator = TranslationService()
documents = DocumentService()


def handle_explain(args):

    result = translator.explain_command(
        args.cmd,
        args.lang
    )

    documents.save_document(
        args.cmd,
        result,
        args.lang
    )

    print("\n=== Explanation ===")
    print(result)


def handle_transpile(args):

    code = translator.transpile_logic(
        args.code,
        args.to
    )

    print("\n=== Generated Code ===")
    print(code)