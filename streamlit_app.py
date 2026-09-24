import time

import streamlit as st

from simulation import step_people

GRID_SIZE = 10
DOTS_PER_LINE = 10
MAX_DOTS_DISPLAY = 30
CELL_SIZE = 48


def make_cell_label(count):
    if count == 0:
        return " "

    visible_count = min(count, MAX_DOTS_DISPLAY)

    lines = []

    for start in range(0, visible_count, DOTS_PER_LINE):

        dots_in_line = min(
            DOTS_PER_LINE,
            visible_count - start,
        )
        lines.append("•" * dots_in_line)

    return "\n".join(lines)


st.title("Random Walker Grid")

if "people" not in st.session_state:
    st.session_state.people = []

if "step_count" not in st.session_state:
    st.session_state.step_count = 0

if "auto_run" not in st.session_state:
    st.session_state.auto_run = False

st.write(
    f"Step：{st.session_state.step_count} | "
    f"目前小人數量：{len(st.session_state.people)}"
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("move 1 step"):
        st.session_state.people = step_people(
            st.session_state.people,
            GRID_SIZE,
        )

        st.session_state.step_count += 1

        st.rerun()

with col2:
    if st.button("auto move"):
        st.session_state.auto_run = True

        st.rerun()

with col3:
    if st.button("pause"):
        st.session_state.auto_run = False

        st.rerun()

with col4:
    if st.button("Clear"):
        st.session_state.people = []
        st.session_state.step_count = 0
        st.session_state.auto_run = False
        st.rerun()


st.markdown(
    f"""
    <style>
    .st-key-grid {{
        width: {GRID_SIZE * CELL_SIZE}px;
        max-width: {GRID_SIZE * CELL_SIZE}px;
    }}

    .st-key-grid div[data-testid="stColumn"] {{
        width: {CELL_SIZE}px !important;
        min-width: {CELL_SIZE}px !important;
        flex: 0 0 {CELL_SIZE}px !important;
    }}

    .st-key-grid div[data-testid="stButton"] button {{
        width: {CELL_SIZE}px !important;
        height: {CELL_SIZE}px !important;
        min-height: {CELL_SIZE}px !important;

        padding: 2px !important;
        margin: 0 !important;

        border-radius: 0 !important;

        white-space: pre-line !important;
        overflow: hidden !important;

        font-size: 11px !important;
        line-height: 10px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

highlighted_cells = []

with st.container(
    key="grid",
    gap=None,
):
    for row in range(GRID_SIZE):
        columns = st.columns(
            GRID_SIZE,
            gap=None,
        )

        for col in range(GRID_SIZE):
            position = (row, col)

            count = st.session_state.people.count(position)

            label = make_cell_label(count)

            cell_key = f"cell_{row}_{col}"

            if count > MAX_DOTS_DISPLAY:
                highlighted_cells.append(cell_key)

            if columns[col].button(
                label,
                key=cell_key,
                help=f"人數：{count}",
            ):
                st.session_state.people.append(position)
                st.rerun()

selectors = ",\n".join(
    f".st-key-{key} button p"
    for key in highlighted_cells
)

highlight_css = ""

if selectors:
    highlight_css = f"""
    {selectors} {{
        color: #ff4b4b !important;
    }}
    """

st.markdown(
    f"""
    <style>

    /* 每個 timestep 先把所有點恢復正常顏色 */
    .st-key-grid button p {{
        color: inherit !important;
    }}

    /* 再把目前超過上限的格子變紅 */
    {highlight_css}

    </style>
    """,
    unsafe_allow_html=True,
)

if st.session_state.auto_run:
    if st.session_state.people:
        time.sleep(0.2)

        st.session_state.people = step_people(st.session_state.people, GRID_SIZE)

        st.session_state.step_count += 1

        st.rerun()

    else:
        st.session_state.auto_run = False
        st.session_state.step_count = 0
        st.success("No people on the grid!")
