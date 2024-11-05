from webscout import ChatGPTES # pip install webscout
import autocoder 

i = autocoder.AutoCoder().intro_prompt
ai = ChatGPTES(is_conversation=True, max_tokens=800, timeout=30, intro=i,  update_file=True, proxies=None, history_offset=10250, act=None)

while True:
    u = input(">>> ")
    print("\033[94m" + u + "\033[0m")
    opt = autocoder.Optimizers.code(u)

    print("\033[92m" + opt + "\033[0m")
    resp = ai.chat(opt)

    autocoder.AutoCoder(internal_exec=False, path_to_script=r"C:\Users\koula\OneDrive\Desktop\DEVELOPER\Projects\JARVIS\run.py").main(resp)

# makd sure this path should exist