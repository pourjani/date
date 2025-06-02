# 📅 Custom Date Class in Python

This project implements a custom `Date` class in Python, offering functionality such as date validation, leap year handling, date comparison, day manipulation, and calculating the number of days between two dates. It works without using any external libraries like `datetime`.

---

## ✨ Features

- ✅ Validate date input (day, month, year)
- 📆 Correctly handles leap years
- ➕➖ Add or subtract days from a given date
- 🔄 Compare two dates
- 📏 Calculate number of days between dates
- 🧪 Includes `test.py` file for demonstration and testing

---

## 🧠 How It Works

The class uses its own logic to:

- Check if a year is a **leap year**
- Return **correct days per month**, including leap-year Februaries
- Manually **increment or decrement** the date when days are added/subtracted
- Track differences between two dates without using Python’s built-in datetime modules
