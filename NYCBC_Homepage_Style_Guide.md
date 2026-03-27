# NYCBC Home Page Style Guide

## 1. 設計目標

- 現代（modern）
- 平靜（peaceful）
- 優雅（elegant）
- 色調為藍綠（blue-green）
- 適合教會和社區網頁：清新、親和、信仰溫度

## 2. 色彩方案

- 主要色：`#1A7A9B`（深藍青）
- 輔助色：`#4DA18B`（沉靜綠）
- 亮點色：`#96CDB6`（柔和薄荷）
- 背景色：`#F5F9F7`（米白）`
- 互動色：`#23657c`、`#efedf2`等。

### 補充建議
- 卡片／區塊：白底（#ffffff）+ 微陰影 + 1px 調色邊框
- CTA 按鈕：純白＋藍綠文字 / 藍綠＋白文字

## 3. 字體與排版

- 中英文字體：
  - `Noto Sans TC`（中文優先）
  - `Montserrat`（英文字體）
  - 備選：`Noto Serif TC`（標題次級、其實會更優雅）

- 標題字重：
  - H1：700
  - H2：600
  - H3：500

- 正文字重：400-500
- 行高：1.5 - 1.7
- 行距與段落：
  - 段落間距 `1rem` 以上
  - 內容留白 `4rem` 以上

## 4. 版面結構（首頁 Sections）

1. Hero 橫幅
   - 大標：教會名稱（中/英）
   - 小標：信仰、關懷、社群 tagline
   - CTA 按鈕：教會簡介、主日聚會、聯絡
   - 背景：藍綠混合 + 淡透光暈圖形

2. About（我們的故事）
   - 兩欄廣度卡片，內含：多語敬拜、彼此關懷

3. Worship（本週聚會）
   - 三格卡片：主日崇拜、禱告會、查經小組
   - 重要提示 CTA：初訪迎接流程

4. Ministries（事工亮點）
   - 以：親子、社區服務、生命培育為主題

5. Contact（聯絡我們）
   - 地址 / 電話 / Email
   - 內部連結：直播/禱告/報名

6. Footer
   - 版權 / 備註 / 社交連結

## 5. 圖片素材建議

- 風格：自然、城市、教會人群、友愛互動
- 色調：向日偏藍綠冷暖，避免硬對比
- 形象：靜水、樹葉、拱門、溫暖笑容

## 6. 互動效果

- 滑動漸入（scroll reveal）
- 懸停按鈕輕微升起（transform translateY(-2px)）
- 卡片陰影過渡（box-shadow .2s ease）
- 平滑滾動（smooth scroll anchor）

## 7. SEO / 無障礙

- 標題順序語意化（H1, H2, H3）
- 圖片 alt 說明
- 字體尺寸可調 (`font-size`/`clamp`) 
- 高對比文本/背景
- aria-label action 按鈕

## 8. 建議鍵結與資訊

- `/#about`、`/#worship`、`/#ministries`、`/#connect`
- 立即可呈現：
  - 目前教會地點、電話、週日時間
  - 本週消息/活動卡片
  - 線上參與連結

---

### 快速安裝片段

- 在頁首 `<head>` 加入：
  - Google 字體
  - `meta viewport` 和描述

- 內容結構 1:1 放進 `index.html`（或現有 `home` 入口）
- CSS 直接內嵌或 SCSS：
```css
:root { --primary: #1A7A9B; ... }
body { background: var(--soft); }
.hero { background-image: linear-gradient(135deg, var(--primary), var(--secondary)); }
```

## 9. 追蹤與分析

- 加 Google Analytics / Plausible 或 Matomo
- 加 sitewide structured data（JSON-LD, Organization / LocalBusiness）

---

### 備註

這份說明僅對「首頁」進行風格定位，並依你的要求做「藍綠、現代、優雅」主題設定。