import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import ValidationError

from schemas import RequirementAnalysis


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError(
        "DEEPSEEK_API_KEY was not found in the .env file."
    )


# ============================================================
# DEEPSEEK CLIENT
# ============================================================

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_NAME = os.getenv(
    "DEEPSEEK_MODEL",
    "deepseek-flash",
)


# ============================================================
# GENERATE STRUCTURED REQUIREMENT ANALYSIS
# ============================================================

def generate_requirement_analysis(
    prompt: str,
) -> RequirementAnalysis:
    """
    Send a Business Analysis prompt to DeepSeek,
    receive JSON, parse it, and validate it using Pydantic.
    """

    # --------------------------------------------------------
    # Call DeepSeek
    # --------------------------------------------------------

    response = client.chat.completions.create(
        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert Business Analyst and "
                    "Requirements Engineer. "
                    "Return ONLY valid JSON. "
                    "Do not return Markdown or explanatory text."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],

        # DeepSeek JSON mode
        response_format={
            "type": "json_object"
        },

        # Disable thinking for this structured extraction task
        extra_body={
            "thinking": {
                "type": "disabled"
            }
        },

        # Keep output large enough for a complete analysis
        max_tokens=6000,

        # Low temperature gives more consistent structured output
        temperature=0.2,
    )

    # --------------------------------------------------------
    # Extract response message
    # --------------------------------------------------------

    if not response.choices:
        raise ValueError(
            "DeepSeek returned no choices in the response."
        )

    message = response.choices[0].message

    # --------------------------------------------------------
    # Extract content
    # --------------------------------------------------------

    content = message.content

    if not content:
        raise ValueError(
            "DeepSeek returned an empty response. "
            f"Finish reason: {response.choices[0].finish_reason}"
        )

    # --------------------------------------------------------
    # Parse JSON
    # --------------------------------------------------------

    try:
        data = json.loads(content)

    except json.JSONDecodeError as error:
        print("\n========== INVALID JSON ==========")
        print(content)
        print("==================================\n")

        raise ValueError(
            f"DeepSeek returned invalid JSON: {error}"
        ) from error

    # --------------------------------------------------------
    # Validate JSON with Pydantic
    # --------------------------------------------------------

    try:

        validated_result = RequirementAnalysis.model_validate(
            data
        )

        return validated_result

    except ValidationError as error:

        # ----------------------------------------------------
        # Print detailed diagnostic information
        # ----------------------------------------------------

        print("\n")
        print("=" * 70)
        print("PYDANTIC VALIDATION ERROR")
        print("=" * 70)

        print(error)

        print("\n")
        print("=" * 70)
        print("RAW LLM JSON")
        print("=" * 70)

        print(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            )
        )

        print("=" * 70)
        print("\n")

        raise ValueError(
            "Pydantic validation failed. "
            "Check the terminal output above for the exact "
            "field mismatch and the raw LLM JSON."
        ) from error


# ============================================================
# SIMPLE TEXT RESPONSE FUNCTION
# ============================================================

def generate_response(prompt: str) -> str:
    """
    Simple text-generation function.

    This is kept for compatibility with the earlier
    version of the application.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        temperature=0.2,
    )

    if not response.choices:
        raise ValueError(
            "DeepSeek returned no response."
        )

    content = response.choices[0].message.content

    if not content:
        raise ValueError(
            "DeepSeek returned an empty response."
        )

    return content