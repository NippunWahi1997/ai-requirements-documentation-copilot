from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


# ============================================================
# STAKEHOLDER
# ============================================================

class Stakeholder(BaseModel):
    model_config = ConfigDict(extra="ignore")

    role: str = ""
    description: str = ""

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "role": value,
                "description": ""
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# FUNCTIONAL REQUIREMENT
# ============================================================

class FunctionalRequirement(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    name: str = ""
    description: str = ""
    actor: str = ""
    category: Optional[str] = None
    priority: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "description": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# NON-FUNCTIONAL REQUIREMENT
# ============================================================

class NonFunctionalRequirement(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    name: str = ""
    description: str = ""
    category: Optional[str] = None
    priority: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "description": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# USER STORY
# ============================================================

class UserStory(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    story: str = ""
    acceptance_criteria: List[str] = Field(
        default_factory=list
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "story": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# BUSINESS RULE
# ============================================================

class BusinessRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    name: str = ""
    description: str = ""

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "description": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# RISK
# ============================================================

class Risk(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    name: str = ""
    description: str = ""
    category: Optional[str] = None
    likelihood: Optional[str] = None
    impact: Optional[str] = None
    mitigation: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "description": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# CLARIFICATION QUESTION
# ============================================================

class ClarificationQuestion(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str = ""
    question: str = ""
    reason: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if isinstance(value, str):
            return {
                "question": value
            }

        if isinstance(value, dict):
            return value

        return {}


# ============================================================
# MAIN REQUIREMENT ANALYSIS
# ============================================================

class RequirementAnalysis(BaseModel):
    model_config = ConfigDict(extra="ignore")

    project_title: str = ""

    overview: str = ""

    business_objective: str = ""

    stakeholders: List[Stakeholder] = Field(
        default_factory=list
    )

    functional_requirements: List[FunctionalRequirement] = Field(
        default_factory=list
    )

    non_functional_requirements: List[
        NonFunctionalRequirement
    ] = Field(
        default_factory=list
    )

    user_stories: List[UserStory] = Field(
        default_factory=list
    )

    business_rules: List[BusinessRule] = Field(
        default_factory=list
    )

    assumptions: List[str] = Field(
        default_factory=list
    )

    constraints: List[str] = Field(
        default_factory=list
    )

    risks: List[Risk] = Field(
        default_factory=list
    )

    clarification_questions: List[
        ClarificationQuestion
    ] = Field(
        default_factory=list
    )

    # ========================================================
    # TOP-LEVEL NORMALIZATION
    # ========================================================

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, value: Any):

        if not isinstance(value, dict):
            return {}

        data = value.copy()

        # ----------------------------------------------------
        # If overview exists but business objective doesn't,
        # use overview as fallback.
        # ----------------------------------------------------

        if not data.get("business_objective"):
            data["business_objective"] = data.get(
                "overview",
                ""
            )

        # ----------------------------------------------------
        # Normalize lists
        # ----------------------------------------------------

        list_fields = [
            "stakeholders",
            "functional_requirements",
            "non_functional_requirements",
            "user_stories",
            "business_rules",
            "assumptions",
            "constraints",
            "risks",
            "clarification_questions",
        ]

        for field in list_fields:

            if data.get(field) is None:
                data[field] = []

        # ----------------------------------------------------
        # Assumptions
        # ----------------------------------------------------

        assumptions = data.get("assumptions", [])

        normalized_assumptions = []

        for item in assumptions:

            if isinstance(item, str):
                normalized_assumptions.append(item)

            elif isinstance(item, dict):

                text = (
                    item.get("description")
                    or item.get("name")
                    or str(item)
                )

                normalized_assumptions.append(text)

        data["assumptions"] = normalized_assumptions

        # ----------------------------------------------------
        # Constraints
        # ----------------------------------------------------

        constraints = data.get("constraints", [])

        normalized_constraints = []

        for item in constraints:

            if isinstance(item, str):
                normalized_constraints.append(item)

            elif isinstance(item, dict):

                text = (
                    item.get("description")
                    or item.get("name")
                    or str(item)
                )

                normalized_constraints.append(text)

        data["constraints"] = normalized_constraints

        return data