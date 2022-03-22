from textwrap import dedent

import pytest
from indentify import indentify


@pytest.mark.parametrize(
    ("source", "expected"),
    (
        (
            '{"results": [{"gender": "male","name": { "title": "Mr", "first": "John", "last": "Doe" },"email": "john.doe@example.com"}]}',
            """\
            {
              "results":[
                {
                  "gender":"male",
                  "name":{
                    "title":"Mr",
                    "first": "John",
                    "last": "Doe"
                  },
                  "email": "john.doe@example.com"
                }
              ]
            }
            """,
        ),
    ),
)
def test_indentify(source: str, expected: str) -> None:
    breakpoint()
    assert indentify(source).strip() == dedent(expected).strip()
