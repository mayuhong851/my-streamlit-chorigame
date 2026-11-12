import streamlit as st
import random

st.title("🎮 猜数字小游戏")

st.write("我已经设置好了一个秘密数字，快来猜猜看是多少吧！")

# 随机生成一个秘密数字
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# 记录猜测次数
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# 输入猜测数字
guess = st.number_input(
    "请输入你猜的数字：",
    min_value=1,
    max_value=100,
    step=1
)

# 提交答案
if st.button("提交答案"):
    st.session_state.attempts += 1

    if guess == st.session_state.secret_number:
        st.success("🎉 That's right! 猜对啦！")
        st.balloons()
    elif guess < st.session_state.secret_number:
        st.warning("猜小了，再试一次！")
    else:
        st.warning("猜大了，再试一次！")

    st.write(f"已经猜了 {st.session_state.attempts} 次")

# 重新开始
if st.button("重新开始"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()

