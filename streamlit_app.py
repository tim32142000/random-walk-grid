import time
from collections import Counter

import streamlit as st

from simulation import step_people

GRID_SIZE = 10

DOTS_PER_LINE = 5
MAX_DOTS_DISPLAY = 25

CELL_SIZE = 48
DOT_SIZE = 4
DOT_GAP = 2

DOTS_WIDTH = (DOTS_PER_LINE - 1) * (DOT_SIZE + DOT_GAP) + DOT_SIZE
DOTS_OFFSET = DOTS_WIDTH / 2

BASE_TIMESTEP = 0.2


def make_dot_shadows(count):
    visible_count = min(count, MAX_DOTS_DISPLAY)

    shadows = []

    pitch = DOT_SIZE + DOT_GAP

    for i in range(1, visible_count):
        row = i // DOTS_PER_LINE
        col = i % DOTS_PER_LINE

        x = col * pitch
        y = row * pitch

        shadows.append(f"{x}px {y}px 0 0 currentColor")

    return ", ".join(shadows) if shadows else "none"


st.title("Random Walker Grid")

if "people" not in st.session_state:
    st.session_state.people = []

if "step_count" not in st.session_state:
    st.session_state.step_count = 0

if "auto_run" not in st.session_state:
    st.session_state.auto_run = False

if st.session_state.auto_run:
    st.write(f"🟢 **Running** | 目前小人數量：{len(st.session_state.people)}")
else:
    st.write(f"⏸️ **Paused** | 目前小人數量：{len(st.session_state.people)}")


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Move 1 step"):
        st.session_state.people = step_people(
            st.session_state.people,
            GRID_SIZE,
        )

        st.session_state.step_count += 1

        st.rerun()

with col2:
    if st.session_state.auto_run:
        if st.button("Pause"):
            st.session_state.auto_run = False
            st.rerun()
    else:
        if st.button("Play"):
            st.session_state.auto_run = True
            st.rerun()

with col3:
    if st.button("Clear"):
        st.session_state.people = []
        st.session_state.step_count = 0
        st.session_state.auto_run = False
        st.rerun()

speed_col, _ = st.columns([3, 1])

with speed_col:
    playback_speed = st.slider(
        "Playback speed",
        min_value=50,
        max_value=200,
        value=100,
        step=50,
        format="%d%%",
    )
    playback_rate = playback_speed / 100
    time_step = BASE_TIMESTEP / playback_rate


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

        border-radius: 0 !important;

        overflow: hidden !important;
    }}


    </style>
    """,
    unsafe_allow_html=True,
)

people_counts = Counter(st.session_state.people)

cell_styles = []

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

            count = people_counts[position]

            cell_key = f"cell_{row}_{col}"

            if count > 0:
                shadows = make_dot_shadows(count)

                if count > MAX_DOTS_DISPLAY:
                    dot_color = "#ff4b4b"
                else:
                    dot_color = "#ffffff"

                cell_styles.append(f"""
                    .st-key-{cell_key} button {{
                        position: relative;
                        color: transparent !important;
                    }}

                    .st-key-{cell_key} button::after {{
                        content: "";
                        position: absolute;

                        width: {DOT_SIZE}px;
                        height: {DOT_SIZE}px;

                        left: 50%;
                        top: 50%;

                        transform: translate(-{DOTS_OFFSET}px, -{DOTS_OFFSET}px);

                        border-radius: 50%;

                        background-color: {dot_color};
                        color: {dot_color};

                        box-shadow: {shadows};
                    }}
                    """)

            if columns[col].button(
                " ",
                key=cell_key,
            ):
                st.session_state.people.append(position)
                st.rerun()


st.markdown(
    f"""
    <style>
    {"".join(cell_styles)}
    </style>
    """,
    unsafe_allow_html=True,
)

if st.session_state.auto_run:
    if st.session_state.people:
        time.sleep(time_step)
        st.session_state.people = step_people(st.session_state.people, GRID_SIZE)
        st.session_state.step_count += 1

        st.rerun()

    else:
        st.session_state.auto_run = False
        st.success("No people on the grid!")
