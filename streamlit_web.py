import streamlit as st
from loguru import logger
from inference import ChatGPT


@st.cache_resource
def load_model():
    return ChatGPT()


def app():
    logger.info("Start ChatBot APP")

    # load model
    GPT = load_model()

    # create chatbot UI
    st.title("🤖 ChatBot Demo")

    if "questions" not in st.session_state:
        st.session_state["questions"] = []

    if "answers" not in st.session_state:
        st.session_state["answers"] = []

    if "cur_model_type" not in st.session_state:
        st.session_state["cur_model_type"] = "chatGPT"

    if "counter" not in st.session_state:
        st.session_state["counter"] = 0

    user_input = st.chat_input('Ask me anything...')

    if user_input:
        response = GPT.chat_with_history(content=user_input,
                                         questions=st.session_state.questions,
                                         answers=st.session_state.answers)
        st.session_state.questions.append(user_input.strip())
        st.session_state.answers.append(response)

        for i in range(len(st.session_state.answers)):
            with st.chat_message("assistant"):
                st.info(st.session_state.questions[i])
                st.info(st.session_state.answers[i])


if __name__ == "__main__":
    app()
