import time

epoch_time = float(time.time())
date = time.strftime('%b %d %Y')

print("Seconds since January 1, 1970:", '{:,}'.format(epoch_time))
print("or", '{:.2e}'.format(epoch_time), "in scientific notation")
print(date)
