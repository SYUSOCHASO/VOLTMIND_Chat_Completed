from functions.funs import gemini_chat, groq_chat, gpt_chat, claude_chat, xai_chat

def get_llm_function(llm_model):
    model_functions = {
        'gemini': gemini_chat,
        'groq': groq_chat,
        'gpt': gpt_chat,
        'claude': claude_chat,
        'xai': xai_chat
    }
    return model_functions.get(llm_model, gemini_chat)

def VOLTMINDBOT(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 税務GPT(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 薬科GPT(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 敬語の鬼(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 節税商品説明AI(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def IT用語説明AI(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 要件定義書のヒアリングAI(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def ビジネス向け要件定義書(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def エンジニア向け要件定義書(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res

def 金額提示相談AI(user_inputs, system_prompt, llm_model='gemini'):
    chat_function = get_llm_function(llm_model)
    res = chat_function(user_inputs, system_prompt)
    return res
