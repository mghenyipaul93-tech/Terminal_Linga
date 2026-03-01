from utils.file_handler import read_json
from config import TRANSLATIONS_FILE


class TranslationService:

    def __init__(self):
        self.translations = read_json(TRANSLATIONS_FILE)

    def explain_command(self, command, language):

        command_data = self.translations.get(command)

        if not command_data:
            return "Command explanation not found."

        lang_data = command_data.get(language)

        if not lang_data:
            return f"No translation available in {language}"

        explanation = lang_data["explanation"]
        analogy = lang_data["analogy"]

        return f"""
Explanation:
{explanation}

Analogy:
{analogy}
"""

    def transpile_logic(self, logic, target):

        logic = logic.lower()

        # simple demo transpiler
        if "ikiwa" in logic and "chapisha" in logic:

            if target == "python":
                return """if number > 10:
    print("kubwa")"""

            if target == "javascript":
                return """if (number > 10) {
    console.log("kubwa");
}"""

        return "# Unable to transpile logic"