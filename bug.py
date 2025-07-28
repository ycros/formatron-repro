from formatron.formatter import FormatterBuilder
from formatron.schemas import json_schema
import kbnf

schema_1 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "test",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "minItems": 2,
            "maxItems": 2,
            "foo": {"type": "string"},
        }
    },
}

schema_2 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "test",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "minItems": 1,
            "maxItems": 2,
            "foo": {"type": "string"},
        }
    },
}

schema_3 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "test",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "foo": {"type": "string"},
        }
    },
}

schema_4 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "test",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "maxItems": 2,
            "foo": {"type": "string"},
        }
    },
}

schema_5 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "test",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "minItems": 1,
            "foo": {"type": "string"},
        }
    },
}


def run_schema(schema):
    try:
        vocab = kbnf.Vocabulary(
            {i: kbnf.Token(bytes([i])) for i in range(256)},
            {i: chr(i) if i < 128 else f"<{i}>" for i in range(256)},
        )

        f = FormatterBuilder()
        f.append_line(f"{f.json(json_schema.create_schema(schema))}")
        f.build(vocab, lambda x: "")
        print("--- SUCCESS ---\n")
    except Exception as e:
        print(repr(e))
        print("--- FAILED ---\n")


print("minItems 2/maxItems 2")
run_schema(schema_1)
print("minItems 1/maxItems 2")
run_schema(schema_2)
print("no min max")
run_schema(schema_3)
print("maxItems 2")
run_schema(schema_4)
print("minItems 1")
run_schema(schema_5)
