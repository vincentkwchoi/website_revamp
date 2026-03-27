# NYCBC CSC Home Page Restyling Spec

## 1. 目標

- 將現有頁面（https://www.nycbc.ca/csc/home）更新為現代、平靜、優雅風格
- 主色調：藍綠 (blue-green)
- 保留原「資訊架構」與文案，但重構視覺/版面、互動、可讀性
- 嚴格針對「首頁」做變更，不動其他路由

## 2. 原頁面內容（待保留）

- 頁首logo+教會名稱
- 本主日場刊介紹
- 最新消息 / 活動區
- 告別：歡迎、聯絡、信徒資源連結

## 3. 新視覺系統

### 色彩
- 基色：`#1A7A9B` deep teal
- 副色：`#4DA18B`
- 輸出色：`#96CDB6`
- 背景：`#F5F9F7`, `#EEF4F1`
- 文字：`#203c4a`
- 邊界/卡片：`#e9f2f2`

### 字體
- 中文：`Noto Sans TC` / `Noto Serif TC`
- 英文：`Montserrat` / `Poppins`
- 標題：`700`
- 內文：`400/500`
- 前導線高：`1.5`

### 排版
- 使用同一主容器 `max-width: 1120px` 寬度
- 大段白空間：`padding: 4rem 0`
- 卡片式網格：`grid` 2-3 欄
- 移動響應：小於 720px 時轉 1 欄

## 4. 內容結構（section mapping）

1. Hero section (現有logo + 上宣) 
2. About / 事工說明
3. 本日場刊主要功能區
4. 最新活動卡片(3~4項)
5. Mechanics：下載、本週信息、連絡表
6. Footer: 聯繫 + 版權

## 5. HTML 元素規則

- 影像：`<img alt="...">`
- 按鈕：`<button class="btn-primary">` + `<a class="btn-muted">`
- 可訪問：`aria-label`、`role`、`tabindex`
- SEO：`<meta name="description">` + OG tags

## 6. 動態行為

- 滾動時 Section 逐個淡入
- nav anchor smooth scroll
- 按鈕 hover 微升位+陰影

## 7. 遷移方案

1. 取得現有 `home` HTML 內容並備份
2. 套用新 CSS 與結構套模板
3. 保留文字與連結
4. 測試桌機/平板/手機
5. UAT 檢查資料一致性 (本週聚會、場刊申請)

## 8. 針對現有內容列表

- 範例/要點:
  - `本主日場刊` 大標改為「本週敬拜聚會」
  - `最新消息` 改 `活動快訊` 卡片
  - 右側社群卡/報名表可改為固定 CTA 模組

## 9. 成果驗收

- 與原內容 1:1 資訊
- 視覺符合藍綠優雅印象
- 零 Trace JS、輕量 CSS（可行）
- 頁面無 2xx 404、語意標題結構正常

---

## 附錄：範例 CSS 快取

```css
:root {
  --color-brand: #1A7A9B;
  --color-accent: #4DA18B;
  /* ... */
}
.hero { background: linear-gradient(135deg, var(--color-brand), var(--color-accent)); }
.section { padding: 4rem 0; }
```
