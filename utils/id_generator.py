
import uuid


def generate_id(prefix="lng"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"