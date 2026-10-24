# Random Walker Grid

English | [繁體中文](/README.zh-TW.md)

[DEMO](https://random-walk-grid.streamlit.app/)

---

An interactive random walk simulation built with [Streamlit](https://streamlit.io/). Click cells on a 10×10 grid to place walkers, then watch each one move randomly, spread out, or wander off the edge.

## Features

- **Click to place**: click any cell to add a walker there
- **Step or auto-run**: press "Move 1 step" to advance once, or toggle Pause / Auto Run for continuous playback
- **Speed control**: a slider adjusts the auto-run speed from 50% to 200%
- **Reset**: "Clear" removes all walkers and resets the step counter
- **Density display**: each cell shows up to 25 dots, one per walker; cells with more than 25 walkers turn red

## Simulation Rules

On every step, each walker picks one of the four directions (up, down, left, right) **at random** and moves one cell. If the move would take it outside the 10×10 grid, the walker **leaves the simulation and is removed**. The edges act as exits, not bouncing walls.

## Project Structure

| File | Description |
| --- | --- |
| `simulation.py` | Core simulation logic: grid size, the four movement directions, and `step_people`, which moves every walker and drops those that leave the grid |
| `streamlit_app.py` | Streamlit UI: grid rendering, buttons and slider, the auto-run loop; state is kept in `st.session_state` |
| `requirements.txt` | Dependencies (`streamlit>=1.48,<2`) |

## Installation and Usage

```bash
# 1. Get the project
git clone https://github.com/tim32142000/random-walk-grid.git
cd random-walk-grid

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_app.py
```

Your browser should open automatically (by default at http://localhost:8501).

## How to Use

1. Click a cell to place a walker (click the same cell repeatedly to add more)
2. Press "Move 1 step" to advance one step, or "Auto Run" to keep going
3. Use the speed slider to change the pace
4. Press "Clear" to remove everything and start over

## Ideas for Extension

- Change the grid size, or make it configurable from the UI
- Add other boundary rules, such as reflecting walls or wrap-around edges
- Chart the number of remaining walkers over time, or the average survival time
