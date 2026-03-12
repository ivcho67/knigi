import streamlit as st

# 1. Инициализиране на базата данни (session_state)
# Използваме session_state, за да не се изтриват данните при всяко презареждане
if "books" not in st.session_state:
    st.session_state.books = []

st.title("📚 Приложение за управление на библиотека")

# --- СЕКЦИЯ: ДОБАВЯНЕ НА КНИГА ---
st.header("➕ Добави книга")

title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0, step=0.1)

if st.button("Добави книгата"):
    if title.strip() == "" or author.strip() == "":
        st.warning("Моля, попълнете заглавие и автор!")
    else:
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state.books.append(book)
        st.success(f"Книгата '{title}' е добавена успешно!")

st.divider()

# --- СЕКЦИЯ: ПОКАЗВАНЕ НА ВСИЧКИ КНИГИ ---
st.header("📋 Списък с книги")

if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write(f"**Заглавие:** {book['title']}")
            st.write(f"**Автор:** {book['author']}")
            st.write(f"**Цена:** {book['price']:.2f} лв.")
            st.write("--------------------")

st.divider()

# --- СЕКЦИЯ: ТЪРСЕНЕ ПО АВТОР ---
st.header("🔍 Търсене по автор")

search_author = st.text_input("Въведи име на автор за търсене")

if st.button("Търси по автор"):
    found = False
    
    if search_author.strip() == "":
        st.warning("Моля, въведете име на автор.")
    else:
        for book in st.session_state.books:
            # Търсим съвпадение (може да добавиш .lower(), за да не е чувствително към главни букви)
            if book["author"].lower() == search_author.lower():
                st.write(book)
                found = True
        
        if not found:
            st.error("Няма намерени книги от този автор.")
