# Roo Mizi | Task Management App

A simple web-based task management application built with Flask and SQLite.

[English](#english) | [فارسی](#فارسی)

---

# English

## Overview

Roo Mizi is a web-based task management application designed to help users organize and track their tasks through a Kanban-style board.

Tasks are organized into three columns: To Do, In Progress, and Completed.

## Features

- **Add Tasks:** Create new tasks with a required title and an optional description.
- **View Tasks:** Display all tasks organized by their current status.
- **Input Validation:** Prevent empty titles and enforce input length limits.
- **Task Status Management:** Move tasks between To Do, In Progress, and Completed.
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
- JavaScript

## Project Structure

```text
ToDoApp/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
│
├── requirements.txt
├── run.py
└── README.md
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

Tasks are organized into three status columns:

1. **To Do:** Newly created tasks.
2. **In Progress:** Tasks currently being worked on.
3. **Completed:** Tasks that have been finished.

Users can move tasks to the next status using the checkboxes displayed beside each task.

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

رو میزی (Roo Mizi) یک سامانه تحت وب برای مدیریت و سازمان‌دهی وظایف است که با استفاده از فریم‌ورک Flask و پایگاه داده SQLite توسعه داده شده است.

این برنامه با بهره‌گیری از یک برد کانبان، وظایف را در سه ستون «انجام‌نشده»، «در حال انجام» و «تکمیل‌شده» نمایش می‌دهد.

## قابلیت‌ها

- **افزودن وظیفه:** امکان ثبت وظایف جدید با عنوان الزامی و توضیحات اختیاری.
- **مشاهده وظایف:** نمایش وظایف ثبت‌شده بر اساس وضعیت آن‌ها.
- **اعتبارسنجی ورودی‌ها:** جلوگیری از ثبت عنوان خالی و محدود کردن طول عنوان و توضیحات.
- **مدیریت وضعیت وظایف:** امکان انتقال وظایف بین سه وضعیت انجام‌نشده، در حال انجام و تکمیل‌شده.
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
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
│
├── requirements.txt
├── run.py
└── README.md
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

وظایف در برنامه در قالب سه ستون سازمان‌دهی می‌شوند:

۱. **انجام‌نشده (To Do):** وظایف تازه ثبت‌شده در این بخش قرار می‌گیرند.

۲. **در حال انجام (In Progress):** وظایفی که کار روی آن‌ها آغاز شده است، در این بخش نمایش داده می‌شوند.

۳. **تکمیل‌شده (Completed):** وظایفی که انجام آن‌ها به پایان رسیده است، در این بخش قرار می‌گیرند.

کاربر می‌تواند با استفاده از چک‌باکس کنار هر وظیفه، وضعیت آن را به مرحله بعدی منتقل کند.

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