@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo ========================================
echo Скрипт миграций Django
echo ========================================

echo.
echo Шаг 1: Создание миграций...
python manage.py makemigrations > temp_output.txt 2>&1
set MIGRATION_STATUS=!errorlevel!

findstr /C:"No changes detected" temp_output.txt > nul
if !errorlevel!==0 (
    echo  Изменений не обнаружено
    set NO_CHANGES=1
) else (
    set NO_CHANGES=0
)

type temp_output.txt
del temp_output.txt

if !MIGRATION_STATUS! neq 0 (
    echo.
    echo  ОШИБКА: Не удалось создать миграции!
    pause
    exit /b !MIGRATION_STATUS!
)

if !NO_CHANGES!==1 (
    echo.
    echo  Пропускаем применение миграций - нет изменений
) else (
    echo.
    echo Шаг 2: Применение миграций...
    python manage.py migrate
    if !errorlevel! neq 0 (
        echo.
        echo  ОШИБКА: Не удалось применить миграции!
        pause
        exit /b !errorlevel!
    ) else (
        echo  Миграции успешно применены!
    )
)

echo.
echo ========================================
echo Скрипт миграций завершен!
echo ========================================
echo.
