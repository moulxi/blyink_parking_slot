import parking_slot as ps

# declare a SlotGroup object, input is the token
rasp = ps.SlotGroup("")

# send a sig 0/1 to led
rasp.send_led_sig("v0", 1)
rasp.send_led_sig("v3", 1)

# send a nmuber to label
rasp.send_label_sig("v5", 39)