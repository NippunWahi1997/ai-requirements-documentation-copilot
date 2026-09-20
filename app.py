from pathlib import Path

import pandas as pd
import streamlit as st

from llm_service import generate_requirement_analysis
from prompts import REQUIREMENT_ANALYSIS_PROMPT


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Requirements Documentation Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "logo.png"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Hide Streamlit default menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Page spacing */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    .project-title {
        font-size: 2.4rem;
        font-weight: 750;
        margin-bottom: 0.2rem;
    }

    .project-subtitle {
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }

    /* Section titles */
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }

    /* Metric numbers */
    .metric-number {
        font-size: 2rem;
        font-weight: 750;
        text-align: center;
    }

    .metric-label {
        font-size: 0.85rem;
        color: #64748b;
        text-align: center;
    }

    /* Small labels */
    .small-label {
        font-size: 0.8rem;
        color: #64748b;
    }

    /* Footer */
    .app-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.8rem;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "last_requirement" not in st.session_state:
    st.session_state.last_requirement = ""


# ============================================================
# LOGO
# ============================================================

if LOGO_PATH.exists():
    st.image(
        str(LOGO_PATH),
        use_container_width=True,
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="project-title">AI Requirements Documentation Copilot</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="project-subtitle">
        Transform natural-language business requirements into
        structured Business Analysis documentation using Generative AI.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📌 Project")

    st.write(
        """
        This AI application analyzes business requirements and
        generates structured Business Analysis documentation.
        """
    )

    st.divider()

    st.subheader("🤖 AI Capabilities")

    capabilities = [
        "Requirement analysis",
        "Stakeholder identification",
        "Functional requirements",
        "Non-functional requirements",
        "User stories",
        "Acceptance criteria",
        "Business rules",
        "Assumptions",
        "Constraints",
        "Risks",
        "Clarification questions",
    ]

    for capability in capabilities:
        st.write(f"✓ {capability}")

    st.divider()

    st.subheader("🧪 Sample Requirement")

    sample_options = {
        "Student Attendance System": (
            "Build a student attendance management system where "
            "faculty can mark attendance, students can view their "
            "attendance, and program leaders can generate attendance reports."
        ),
        "Employee Reimbursement System": (
            "Build an employee reimbursement system where employees "
            "can submit claims, managers can approve claims, and "
            "the finance team can process approved reimbursements."
        ),
        "Hospital Appointment System": (
            "Build a hospital appointment management system where "
            "patients can book appointments, doctors can view their "
            "schedules, and administrators can manage appointments."
        ),
    }

    selected_sample = st.selectbox(
        "Select a sample",
        ["Select a sample"] + list(sample_options.keys()),
    )

    if selected_sample != "Select a sample":

        if st.button(
            "Load Sample",
            use_container_width=True,
        ):
            st.session_state.last_requirement = (
                sample_options[selected_sample]
            )
            st.rerun()

    st.divider()

    if st.button(
        "🗑️ Clear Analysis",
        use_container_width=True,
    ):
        st.session_state.analysis_result = None
        st.session_state.last_requirement = ""
        st.rerun()


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">1. Business Requirement</div>',
    unsafe_allow_html=True,
)

requirement = st.text_area(
    "Business Requirement",
    value=st.session_state.last_requirement,
    height=220,
    max_chars=10000,
    label_visibility="collapsed",
    placeholder=(
        "Example:\n\n"
        "Build a student attendance management system where "
        "faculty can mark attendance, students can view their "
        "attendance, and program leaders can generate reports."
    ),
)

st.caption(
    f"{len(requirement):,} characters"
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze_clicked = st.button(
    "🚀 Analyze Requirement",
    type="primary",
    use_container_width=True,
)


# ============================================================
# AI ANALYSIS
# ============================================================

if analyze_clicked:

    if not requirement.strip():

        st.warning(
            "Please enter a business requirement."
        )

    elif len(requirement.strip()) < 20:

        st.warning(
            "Please provide a more detailed business requirement."
        )

    else:

        st.session_state.last_requirement = requirement

        with st.spinner(
            "🤖 AI is analyzing the requirement..."
        ):

            try:

                # Important:
                # Do NOT use .format() because the prompt contains
                # JSON braces. Replace only the requirement placeholder.
                prompt = REQUIREMENT_ANALYSIS_PROMPT.replace(
                    "{requirement}",
                    requirement,
                )

                result = generate_requirement_analysis(
                    prompt
                )

                st.session_state.analysis_result = result

                st.success(
                    "Requirement analysis completed successfully."
                )

            except Exception as error:

                st.session_state.analysis_result = None

                st.error(
                    "The AI analysis could not be completed."
                )

                st.code(
                    str(error),
                    language="text",
                )


# ============================================================
# RESULTS
# ============================================================

result = st.session_state.analysis_result


if result is not None:

    st.divider()

    st.markdown(
        '<div class="section-title">2. AI-Generated Analysis</div>',
        unsafe_allow_html=True,
    )


    # ========================================================
    # PROJECT OVERVIEW
    # ========================================================

    st.header(
        result.project_title or "Untitled Project"
    )

    if result.overview:
        st.write(result.overview)

    if result.business_objective:

        st.info(
            f"**Business Objective:** {result.business_objective}"
        )


    # ========================================================
    # KPI CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        (
            len(result.stakeholders),
            "Stakeholders",
        ),
        (
            len(result.functional_requirements),
            "Functional Requirements",
        ),
        (
            len(result.non_functional_requirements),
            "Non-Functional Requirements",
        ),
        (
            len(result.user_stories),
            "User Stories",
        ),
    ]

    for column, (number, label) in zip(
        [col1, col2, col3, col4],
        metrics,
    ):

        with column:

            with st.container(border=True):

                st.markdown(
                    f'<div class="metric-number">{number}</div>',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f'<div class="metric-label">{label}</div>',
                    unsafe_allow_html=True,
                )


    # ========================================================
    # STAKEHOLDERS
    # ========================================================

    st.subheader("👥 Stakeholders")

    if result.stakeholders:

        stakeholder_columns = st.columns(
            min(3, len(result.stakeholders))
        )

        for index, stakeholder in enumerate(
            result.stakeholders
        ):

            with stakeholder_columns[
                index % len(stakeholder_columns)
            ]:

                with st.container(border=True):

                    st.markdown(
                        f"### {stakeholder.role}"
                    )

                    st.write(
                        stakeholder.description
                    )

    else:

        st.info(
            "No stakeholders identified."
        )


    # ========================================================
    # FUNCTIONAL REQUIREMENTS
    # ========================================================

    st.subheader("⚙️ Functional Requirements")

    if result.functional_requirements:

        functional_rows = []

        for item in result.functional_requirements:

            functional_rows.append(
                {
                    "ID": item.id,
                    "Name": item.name or "—",
                    "Description": item.description,
                    "Actor": item.actor or "—",
                    "Priority": item.priority or "—",
                    "Category": item.category or "—",
                }
            )

        functional_df = pd.DataFrame(
            functional_rows
        )

        st.dataframe(
            functional_df,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No functional requirements identified."
        )


    # ========================================================
    # NON-FUNCTIONAL REQUIREMENTS
    # ========================================================

    st.subheader("🛡️ Non-Functional Requirements")

    if result.non_functional_requirements:

        nfr_rows = []

        for item in result.non_functional_requirements:

            nfr_rows.append(
                {
                    "ID": item.id,
                    "Name": item.name or "—",
                    "Description": item.description,
                    "Category": item.category or "—",
                    "Priority": item.priority or "—",
                }
            )

        nfr_df = pd.DataFrame(
            nfr_rows
        )

        st.dataframe(
            nfr_df,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No non-functional requirements identified."
        )


    # ========================================================
    # USER STORIES
    # ========================================================

    st.subheader("🧑‍💻 User Stories")

    if result.user_stories:

        for index, story in enumerate(
            result.user_stories,
            start=1,
        ):

            story_id = getattr(
                story,
                "id",
                "",
            )

            title = (
                f"{story_id} — User Story {index}"
                if story_id
                else f"User Story {index}"
            )

            with st.expander(title):

                st.markdown(
                    f"**Story:** {story.story}"
                )

                st.markdown(
                    "**Acceptance Criteria**"
                )

                if story.acceptance_criteria:

                    for criterion_index, criterion in enumerate(
                        story.acceptance_criteria,
                        start=1,
                    ):

                        st.write(
                            f"{criterion_index}. {criterion}"
                        )

                else:

                    st.info(
                        "No acceptance criteria generated."
                    )

    else:

        st.info(
            "No user stories identified."
        )


    # ========================================================
    # BUSINESS RULES
    # ========================================================

    st.subheader("📋 Business Rules")

    if result.business_rules:

        rule_columns = st.columns(
            min(2, len(result.business_rules))
        )

        for index, rule in enumerate(
            result.business_rules
        ):

            with rule_columns[
                index % len(rule_columns)
            ]:

                with st.container(border=True):

                    st.markdown(
                        f"**{rule.id} — {rule.name or 'Business Rule'}**"
                    )

                    st.write(
                        rule.description
                    )

    else:

        st.info(
            "No business rules identified."
        )


    # ========================================================
    # ASSUMPTIONS
    # ========================================================

    st.subheader("💡 Assumptions")

    if result.assumptions:

        with st.container(border=True):

            for assumption in result.assumptions:

                st.write(
                    f"• {assumption}"
                )

    else:

        st.info(
            "No assumptions identified."
        )


    # ========================================================
    # CONSTRAINTS
    # ========================================================

    st.subheader("🚧 Constraints")

    if result.constraints:

        with st.container(border=True):

            for constraint in result.constraints:

                st.write(
                    f"• {constraint}"
                )

    else:

        st.info(
            "No constraints identified."
        )


    # ========================================================
    # RISKS
    # ========================================================

    st.subheader("⚠️ Risks")

    if result.risks:

        for risk in result.risks:

            title_parts = []

            if risk.id:
                title_parts.append(
                    risk.id
                )

            if risk.name:
                title_parts.append(
                    risk.name
                )

            risk_title = (
                " — ".join(title_parts)
                if title_parts
                else "Risk"
            )

            with st.expander(
                risk_title
            ):

                if risk.description:

                    st.write(
                        f"**Description:** {risk.description}"
                    )

                if risk.category:

                    st.write(
                        f"**Category:** {risk.category}"
                    )

                if risk.likelihood:

                    st.write(
                        f"**Likelihood:** {risk.likelihood}"
                    )

                if risk.impact:

                    st.write(
                        f"**Impact:** {risk.impact}"
                    )

                if risk.mitigation:

                    st.write(
                        f"**Mitigation:** {risk.mitigation}"
                    )

    else:

        st.info(
            "No risks identified."
        )


    # ========================================================
    # CLARIFICATION QUESTIONS
    # ========================================================

    st.subheader("❓ Clarification Questions")

    if result.clarification_questions:

        for question in result.clarification_questions:

            question_id = (
                question.id
                if question.id
                else "Question"
            )

            with st.expander(
                question_id
            ):

                st.write(
                    question.question
                )

                if question.reason:

                    st.caption(
                        f"Why this matters: {question.reason}"
                    )

    else:

        st.success(
            "No major clarification questions identified."
        )


    # ========================================================
    # EXPORT
    # ========================================================

    st.divider()

    st.subheader("📥 Export Analysis")

    json_output = result.model_dump_json(
        indent=4
    )

    # --------------------------------------------------------
    # Readable text report
    # --------------------------------------------------------

    report_lines = []

    report_lines.append(
        "AI REQUIREMENTS DOCUMENTATION COPILOT"
    )

    report_lines.append(
        "=" * 60
    )

    report_lines.append(
        f"\nPROJECT TITLE\n{result.project_title}"
    )

    report_lines.append(
        f"\nOVERVIEW\n{result.overview}"
    )

    report_lines.append(
        f"\nBUSINESS OBJECTIVE\n{result.business_objective}"
    )

    report_lines.append(
        "\n\nSTAKEHOLDERS"
    )

    for stakeholder in result.stakeholders:

        report_lines.append(
            f"\n- {stakeholder.role}: "
            f"{stakeholder.description}"
        )

    report_lines.append(
        "\n\nFUNCTIONAL REQUIREMENTS"
    )

    for item in result.functional_requirements:

        report_lines.append(
            f"\n{item.id} | "
            f"{item.name} | "
            f"{item.description} | "
            f"Actor: {item.actor} | "
            f"Priority: {item.priority}"
        )

    report_lines.append(
        "\n\nNON-FUNCTIONAL REQUIREMENTS"
    )

    for item in result.non_functional_requirements:

        report_lines.append(
            f"\n{item.id} | "
            f"{item.name} | "
            f"{item.description} | "
            f"Category: {item.category} | "
            f"Priority: {item.priority}"
        )

    report_lines.append(
        "\n\nUSER STORIES"
    )

    for story in result.user_stories:

        report_lines.append(
            f"\n{story.story}"
        )

        for criterion in story.acceptance_criteria:

            report_lines.append(
                f"\n  - {criterion}"
            )

    report_lines.append(
        "\n\nBUSINESS RULES"
    )

    for rule in result.business_rules:

        report_lines.append(
            f"\n{rule.id} | "
            f"{rule.name} | "
            f"{rule.description}"
        )

    report_lines.append(
        "\n\nASSUMPTIONS"
    )

    for assumption in result.assumptions:

        report_lines.append(
            f"\n- {assumption}"
        )

    report_lines.append(
        "\n\nCONSTRAINTS"
    )

    for constraint in result.constraints:

        report_lines.append(
            f"\n- {constraint}"
        )

    report_lines.append(
        "\n\nRISKS"
    )

    for risk in result.risks:

        report_lines.append(
            f"\n{risk.id} | "
            f"{risk.name} | "
            f"{risk.description}"
        )

        if risk.mitigation:

            report_lines.append(
                f"\n  Mitigation: {risk.mitigation}"
            )

    report_lines.append(
        "\n\nCLARIFICATION QUESTIONS"
    )

    for question in result.clarification_questions:

        report_lines.append(
            f"\n{question.id}: "
            f"{question.question}"
        )

        if question.reason:

            report_lines.append(
                f"\n  Reason: {question.reason}"
            )

    readable_report = "\n".join(
        report_lines
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="⬇️ Download JSON",
            data=json_output,
            file_name="requirements_analysis.json",
            mime="application/json",
            use_container_width=True,
        )

    with col2:

        st.download_button(
            label="⬇️ Download Text Report",
            data=readable_report,
            file_name="requirements_analysis.txt",
            mime="text/plain",
            use_container_width=True,
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="app-footer">
        AI Requirements Documentation Copilot |
        GenAI / LLM Application Engineering Project |
        Nippun Wahi
    </div>
    """,
    unsafe_allow_html=True,
)