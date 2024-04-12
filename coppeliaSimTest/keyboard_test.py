import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f'Key {event.name} was pressed')

keyboard.on_press(on_key_event)

# Щоб програма продовжувала виконання, додайте цей рядок
keyboard.wait('esc')  # Чекаємо натискання клавіші Esc для виходу
