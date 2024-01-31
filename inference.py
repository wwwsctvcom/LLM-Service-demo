import openai
from loguru import logger
from typing import Optional, List, Dict, Any


class ChatGPT:
    API_TYPE = "azure"
    API_KEY = ""
    API_BASE = ""
    header_mtk = {
        "X-User-Id": "",
    }

    def __init__(self, engine="aide-gpt-4-turbo", embedding_engine='aide-text-embedding-ada-002-v2', temperature=0.4):
        """
        :param engine: "aide-gpt-35-turbo-16k-4k", "aide-gpt-4-turbo"
        """
        self.engine = engine
        self.embedding_engine = embedding_engine
        self.temperature = temperature

    def start_embedding(self, text: Optional[str] = None):
        # env
        openai.api_type = self.API_TYPE
        openai.api_base = self.API_BASE
        openai.api_version = "2023-05-15"
        openai.api_key = self.API_KEY

        # start embedding
        resp = openai.Embedding.create(
            engine=self.embedding_engine,
            input=text,
            headers=self.header_mtk
        )
        resp_embedding = resp["data"][0]["embedding"]
        return resp_embedding

    @staticmethod
    def build_prompt(user_text: Optional[str] = None,
                     system_text: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        messages = [
            {'role': 'system',
             'content': system_text if system_text else " "},
            {'role': 'user', 'content': user_text}
        ]
        return messages

    @staticmethod
    def build_prompt_with_history(content: Optional[str] = None,
                                  questions: List[str] = None,
                                  answers: List[str] = None,
                                  max_length: Optional[int] = None):
        # check max message token
        def messages_max_tokens(messages: List[Dict[str, str]]):
            max_tokens = 0
            for message_dict in messages:
                max_tokens += len(message_dict["content"])
            return max_tokens

        messages = [
            {"role": "system", "content": " "},
        ]
        if len(content) > max_length and max_length:
            return messages.append({"role": "user", "content": content[:max_length]})

        for idx in range(len(questions)):
            messages.append({"role": "user", "content": questions[idx]})
            messages.append({"role": "assistant", "content": answers[idx]})
        messages.append({"role": "user", "content": content})

        # truncate the messages to max_length
        while messages_max_tokens(messages) >= max_length:
            messages = [messages[0]] + messages[3:]
        return messages

    def chat(self,
             user_text: Optional[str] = None,
             system_text: Optional[str] = None) -> Optional[str]:
        # env
        openai.api_type = self.API_TYPE
        openai.api_base = self.API_BASE
        openai.api_version = '2023-07-01-preview'
        openai.api_key = self.API_KEY

        # start chat
        res_content = ""
        try:
            if system_text is not None:
                messages = self.build_prompt(user_text, system_text)
            else:
                messages = self.build_prompt(user_text)

            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=messages,
                headers=self.header_mtk,
                temperature=self.temperature
            )

            res_content = response['choices'][0]['message']['content']
        except Exception as char_error:
            logger.exception(char_error)
        return res_content

    def chat_with_history(self,
                          content: Optional[str] = None,
                          questions: List[str] = None,
                          answers: List[str] = None,
                          max_length: Optional[int] = 4096) -> Optional[str]:
        # env
        openai.api_type = self.API_TYPE
        openai.api_base = self.API_BASE
        openai.api_version = '2023-07-01-preview'
        openai.api_key = self.API_KEY

        # start chat
        res_content = ""
        try:
            messages = self.build_prompt_with_history(content, questions=questions, answers=answers,
                                                      max_length=max_length)
            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=messages,
                headers=self.header_mtk,
                temperature=self.temperature
            )

            res_content = response['choices'][0]['message']['content']
        except Exception as char_error:
            logger.exception(char_error)
        return res_content
