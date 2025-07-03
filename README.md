<<<<<<< HEAD
# WCL2
=======
# 虛擬展廳 Django 專案

本專案為一個基於 Django 的虛擬展廳網站，首頁嵌入 Unity WebGL 展廳。

## 結構
- `exhibition`：主要 app，首頁顯示 Unity 展廳
- `static/UnityBuild/`：請將 Unity WebGL Build 輸出檔案放在此資料夾
- `templates/exhibition/index.html`：首頁模板，已嵌入 WebGL 展廳

## 如何啟動
1. 安裝依賴：`pip install django`
2. 運行資料庫遷移：`python manage.py migrate`
3. 啟動伺服器：`python manage.py runserver`
4. 瀏覽器開啟 http://127.0.0.1:8000/

## 注意
- 請將你的 Unity WebGL Build 輸出檔案（index.html、Build、TemplateData 等）放到 `static/UnityBuild/` 目錄下，首頁會自動載入。
- 如需擴展功能，請在 `exhibition` app 內開發。
>>>>>>> 9384d0c (初始化 Django 虛擬展廳專案，嵌入 Unity WebGL)
