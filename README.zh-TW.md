# Random Walker Grid

[English](README.md) | 繁體中文

[DEMO](https://random-walk-grid.streamlit.app/)

---

一個用 [Streamlit](https://streamlit.io/) 做的互動式隨機漫步（random walk）模擬。在 10×10 的格子上點擊放置「行走者」，觀察他們各自隨機移動、逐步擴散或離開格子的過程。

## 功能

- **點擊放置**：點擊任一格即可在該格新增一位行走者
- **逐步 / 自動執行**：可按「Move 1 step」單步前進，或用 Pause / Auto Run 切換自動播放
- **速度調整**：以滑桿在 50%～200% 之間調整自動播放的速度
- **清除重來**：「Clear」會清空所有行走者並重置步數
- **密度視覺化**：每格最多以 25 個圓點顯示人數，超過 25 人時格子會變紅

## 模擬規則

每一步，每位行走者會從上、下、左、右四個方向中**隨機選一個**移動一格。如果移動後超出 10×10 的邊界，該行走者就會**離開模擬並被移除**（邊界是「出口」，不是反彈牆）。

## 專案結構

| 檔案 | 說明 |
| --- | --- |
| `simulation.py` | 模擬核心邏輯，包含格子大小、四個移動方向，以及 `step_people` 函式（移動所有行走者並剔除出界者） |
| `streamlit_app.py` | Streamlit 介面：格子繪製、按鈕與滑桿、自動執行迴圈，狀態存放在 `st.session_state` |
| `requirements.txt` | 相依套件（`streamlit>=1.48,<2`） |

## 安裝與執行

```bash
# 1. 取得專案
git clone https://github.com/tim32142000/random-walk-grid.git
cd random-walk-grid

# 2. （建議）建立虛擬環境
python -m venv .venv
source .venv/bin/activate      # Windows 請用 .venv\Scripts\activate

# 3. 安裝相依套件
pip install -r requirements.txt

# 4. 啟動
streamlit run streamlit_app.py
```

啟動後瀏覽器會自動開啟（預設為 http://localhost:8501）。

## 使用方式

1. 在格子上點擊想放置行走者的位置（同一格可重複點擊以增加人數）
2. 按「Move 1 step」觀察單步移動，或按「Auto Run」讓它持續進行
3. 用速度滑桿調整播放節奏
4. 按「Clear」清除全部並重新開始

## 可以延伸的方向

- 調整格子大小，或改成可在介面上設定
- 加入邊界反彈、環狀（wrap-around）等不同邊界規則
- 統計並圖表化「剩餘人數隨步數變化」或「平均存活步數」
