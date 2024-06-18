import pyautogui
import keyboard
import time

def toggle_macro(key):
    global running
    running = not running
    if running:
        print("Macro is now ON.")
    else:
        print("Macro is now OFF.")

def main():
    global running
    running = False
    # 'ctrl+alt' 키 조합을 핫키로 설정하여 매크로 시작/중지 토글
    keyboard.add_hotkey('ctrl+alt', toggle_macro, args=('ctrl+alt',))

    try:
        while True:
            if running:
                pyautogui.click()
                time.sleep(1.5)  # 클릭 간격을 3초로 설정
            else:
                time.sleep(0.1)  # 매크로가 중지된 상태에서는 CPU 사용을 줄이기 위해 대기 시간을 늘림
    except KeyboardInterrupt:
        print("Program exited.")

if __name__ == "__main__":
    main()