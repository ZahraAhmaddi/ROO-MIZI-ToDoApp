# ROO MIZI | Task Management App

A pixel-art, web-based task management application built with Python, Flask, Flask-SQLAlchemy, and SQLite.

[English](#english) | [فارسی](#فارسی)

---

# English

## Overview

ROO MIZI is a task management web application developed as part of a Software Engineering course. It allows users to create, view, edit, delete, and organize tasks through a three-column task board.

## Features

- **Create tasks:** Add a task with a required title and an optional description.
- **View tasks:** Display tasks in the To Do, In Progress, and Completed columns.
- **Change task status:** Move tasks between the three status columns.
- **Edit tasks:** Update a task's title and description.
- **Delete tasks:** Remove tasks after confirmation.
- **Input validation:** Trim input, reject empty or invisible titles, reject unsupported control characters, and enforce field-length limits.
- **Task limits:** Titles can contain up to 100 characters; descriptions can contain up to 2,000 characters.
- **Persistent storage:** Save task data in a local SQLite database.
- **Creation timestamps:** Display when each task was created.
- **Pixel-art interface:** Responsive task board with light/dark theme support.

## Technologies

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML, CSS, and JavaScript
- Jinja templates

## Project Structure

```text
ROO-MIZI-ToDoApp/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── Documents/
│   ├── Product_Backlog.docx
│   ├── Sprint1_Backlog.docx
│   ├── Sprint1_Coordination_Meetings_Report.docx
│   ├── Sprint1_Performance_Report.docx
│   └── Sprint1_Review.docx
├── test/
│   └── test_task_validation.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/ZahraAhmaddi/ROO-MIZI-ToDoApp.git
cd ROO-MIZI-ToDoApp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python run.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Running Tests

With the virtual environment activated, run:

```bash
python -m unittest discover -s test -v
```

## Task Statuses

| Status | Meaning |
|---|---|
| TODO | The task has not been started |
| IN_PROGRESS | The task is currently being worked on |
| DONE | The task has been completed |

New tasks are created with the TODO status by default.

## Data Storage

The application uses SQLite through Flask-SQLAlchemy. The database is created locally when the application starts. The database file is intentionally excluded from version control; each local installation maintains its own task data.

Each task stores:
- A unique ID
- A title (maximum 100 characters)
- An optional description (maximum 2,000 characters)
- A status (TODO, IN_PROGRESS, or DONE)
- A creation timestamp

## Configuration

The application reads its Flask secret key from the `SECRET_KEY` environment variable. If it is not set, the application uses a development fallback. Set a private value through the environment when deploying beyond local development.

## Development

This project is developed for a Software Engineering course using the Scrum framework. Project planning and sprint documents are available in the `Documents/` directory.

---

# فارسی

## معرفی پروژه

«رو میزی» (ROO MIZI) یک برنامه مدیریت وظایف تحت وب است که در قالب درس مهندسی نرم‌افزار و با استفاده از Python، فریم‌ورک Flask و پایگاه داده SQLite توسعه داده شده است. این برنامه امکان ثبت، مشاهده، ویرایش، حذف و دسته‌بندی وظایف را در یک برد سه‌ستونه فراهم می‌کند.

## قابلیت‌ها

- **ثبت وظیفه:** افزودن وظیفه با عنوان الزامی و توضیحات اختیاری.
- **مشاهده وظایف:** نمایش وظایف در ستون‌های «انجام‌نشده»، «در حال انجام» و «انجام‌شده».
- **تغییر وضعیت:** انتقال وظایف بین سه ستون وضعیت.
- **ویرایش وظیفه:** تغییر عنوان و توضیحات وظیفه.
- **حذف وظیفه:** حذف وظیفه پس از نمایش پنجره تأیید.
- **اعتبارسنجی ورودی‌ها:** جلوگیری از ثبت عنوان خالی یا نامرئی، کنترل نویسه‌های نامعتبر و محدودیت طول فیلدها.
- **محدودیت طول:** حداکثر ۱۰۰ نویسه برای عنوان و ۲۰۰۰ نویسه برای توضیحات.
- **ذخیره‌سازی پایدار:** نگهداری اطلاعات در پایگاه داده محلی SQLite.
- **زمان ایجاد:** نمایش زمان ثبت هر وظیفه.
- **رابط کاربری پیکسلی:** طراحی برد وظایف با پشتیبانی از پوسته روشن و تاریک.

## فناوری‌های مورد استفاده

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML، CSS و JavaScript
- قالب‌های Jinja

## ساختار پروژه

```text
ROO-MIZI-ToDoApp/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── Documents/
│   ├── Product_Backlog.docx
│   ├── Sprint1_Backlog.docx
│   ├── Sprint1_Coordination_Meetings_Report.docx
│   ├── Sprint1_Performance_Report.docx
│   └── Sprint1_Review.docx
├── test/
│   └── test_task_validation.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## نصب و راه‌اندازی

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

**ویندوز (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### ۴. نصب وابستگی‌ها

```bash
python -m pip install -r requirements.txt
```

### ۵. اجرای برنامه

```bash
python run.py
```

سپس آدرس [http://127.0.0.1:5000/](http://127.0.0.1:5000/) را در مرورگر باز کنید.

## اجرای تست‌ها

پس از فعال‌سازی محیط مجازی، دستور زیر را اجرا کنید:

```bash
python -m unittest discover -s test -v
```

## وضعیت وظایف

| وضعیت | توضیح |
|---|---|
| TODO | انجام‌نشده |
| IN_PROGRESS | در حال انجام |
| DONE | انجام‌شده |

تمام وظایف جدید به‌صورت پیش‌فرض با وضعیت TODO ثبت می‌شوند.

## ذخیره‌سازی اطلاعات

برای ذخیره اطلاعات از SQLite و Flask-SQLAlchemy استفاده می‌شود. پایگاه داده هنگام اجرای برنامه به‌صورت محلی ایجاد می‌شود. فایل پایگاه داده عمداً در Git ثبت نمی‌شود و هر نصب محلی، اطلاعات وظایف مستقل خود را دارد.

اطلاعات هر وظیفه شامل شناسه یکتا، عنوان، توضیحات اختیاری، وضعیت و زمان ایجاد است.

## تنظیمات

کلید امنیتی Flask از متغیر محیطی `SECRET_KEY` خوانده می‌شود. در صورت تنظیم‌نشدن این متغیر، برنامه از یک مقدار پیش‌فرض مخصوص توسعه استفاده می‌کند. برای استقرار خارج از محیط توسعه، باید مقدار خصوصی و امنی برای آن تنظیم شود.

## روند توسعه

این پروژه در قالب درس مهندسی نرم‌افزار و با چارچوب Scrum توسعه داده می‌شود. مستندات برنامه‌ریزی و اسپرینت‌ها در پوشه `Documents/` قرار دارند.
