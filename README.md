# Roo Mizi | Task Management App

A simple web-based task management application built with Flask and SQLite.

[English](#english) | [فارسی](#فارسی)

---

# English

## Overview

ROO MIZI is a web-based task management application designed to help users create, view, and organize their tasks.

In the current version, all newly created tasks are assigned the **To Do** status and displayed in a single task column.

## Features

- **Add Tasks:** Create new tasks with a required title and an optional description.
- **View Tasks:** Display saved tasks in the To Do column.
- **Input Validation:** Prevent empty titles and enforce input length limits.
- **Data Persistence:** Store tasks in an SQLite database so they remain available after restarting the application.
- **Creation Timestamp:** Display the date and time each task was created.
- **Flash Messages:** Show success and error messages for user actions.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML
- CSS

## Project Structure

```text
ToDoApp/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── Documents/
│   ├── Product_Backlog.docx
│   ├── Sprint1_Backlog.docx
│   ├── Sprint1_Coordination_Meetings_Report.docx
│   ├── Sprint1_Performance_Report.docx
│   └── Sprint1_Review.docx
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ZahraAhmaddi/ROO-MIZI-ToDoApp.git
cd ROO-MIZI-ToDoApp
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python run.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Task Workflow

In the current version, all newly created tasks are assigned the **To Do** status.

Users can:
1. Create a task by entering a title and an optional description.
2. View saved tasks in the To Do column.
3. Keep their tasks stored in the SQLite database across application restarts.

Task status management is not enabled in the current version.

## Database

The application uses SQLite with Flask-SQLAlchemy for data storage.

Each task contains the following fields:

| Field | Description |
|---|---|
| id | Unique task identifier |
| Title | Task title (required) |
| Description | Optional task description |
| Status | Current task status |
| Created At | Task creation date and time |

## Project Status

This project is developed as part of a Software Engineering course using the Scrum framework.

---

# فارسی

## معرفی پروژه

رو میزی (Roo Mizi) یک سامانه تحت وب برای ثبت، مشاهده و سازمان‌دهی وظایف است که با استفاده از فریم‌ورک Flask و پایگاه داده SQLite توسعه داده شده است.

در نسخه فعلی، تمام وظایف تازه ثبت‌شده با وضعیت «انجام‌نشده» (To Do) ذخیره می‌شوند و در یک ستون نمایش داده می‌شوند.

## قابلیت‌ها

- **افزودن وظیفه:** امکان ثبت وظایف جدید با عنوان الزامی و توضیحات اختیاری.
- **مشاهده وظایف:** نمایش وظایف ذخیره‌شده در ستون انجام‌نشده.
- **اعتبارسنجی ورودی‌ها:** جلوگیری از ثبت عنوان خالی و محدود کردن طول عنوان و توضیحات.
- **ذخیره‌سازی اطلاعات:** نگهداری اطلاعات وظایف در پایگاه داده SQLite و حفظ آن‌ها پس از اجرای مجدد برنامه.
- **نمایش زمان ایجاد:** ثبت و نمایش تاریخ و زمان ایجاد هر وظیفه.
- **پیام‌های بازخورد:** نمایش پیام‌های موفقیت و خطا متناسب با عملیات انجام‌شده.

## فناوری‌های مورد استفاده

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML
- CSS
- JavaScript

## ساختار پروژه

```text
ToDoApp/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── Documents/
│   ├── Product_Backlog.docx
│   ├── Sprint1_Backlog.docx
│   ├── Sprint1_Coordination_Meetings_Report.docx
│   ├── Sprint1_Performance_Report.docx
│   └── Sprint1_Review.docx
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## راهنمای نصب و اجرا

### ۱. دریافت مخزن پروژه

```bash
git clone https://github.com/ZahraAhmaddi/ROO-MIZI-ToDoApp.git
cd ROO-MIZI-ToDoApp
```

### ۲. ایجاد محیط مجازی

```bash
python -m venv .venv
```

### ۳. فعال‌سازی محیط مجازی

**در ویندوز (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**در Linux و macOS:**

```bash
source .venv/bin/activate
```

### ۴. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### ۵. اجرای برنامه

```bash
python run.py
```

پس از اجرای برنامه، آدرس زیر را در مرورگر باز کنید:

```text
http://127.0.0.1:5000/
```

## گردش کار وظایف

در نسخه فعلی، تمام وظایف جدید با وضعیت «انجام‌نشده» (To Do) ثبت می‌شوند.

کاربر می‌تواند:
۱. با وارد کردن عنوان و توضیحات اختیاری، وظیفه جدیدی ثبت کند.
۲. وظایف ذخیره‌شده را در ستون انجام‌نشده مشاهده کند.
۳. با استفاده از پایگاه داده SQLite، اطلاعات وظایف را پس از اجرای مجدد برنامه حفظ کند.

قابلیت مدیریت و تغییر وضعیت وظایف در نسخه فعلی فعال نیست.

## پایگاه داده

برای ذخیره‌سازی اطلاعات از پایگاه داده SQLite و کتابخانه Flask-SQLAlchemy استفاده شده است.

اطلاعات هر وظیفه شامل فیلدهای زیر است:

| فیلد | توضیحات |
|---|---|
| id | شناسه منحصربه‌فرد هر وظیفه |
| Title | عنوان وظیفه (الزامی) |
| Description | توضیحات وظیفه (اختیاری) |
| Status | وضعیت فعلی وظیفه |
| Created At | تاریخ و زمان ایجاد وظیفه |

## وضعیت توسعه پروژه

این پروژه در قالب درس مهندسی نرم‌افزار و با استفاده از چارچوب توسعه چابک Scrum در حال توسعه است.