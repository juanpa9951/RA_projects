import datetime

# Get the current date and time
new_datetime = datetime.datetime.now()

# Calculate old datetime with time difference
old_datetime = new_datetime - datetime.timedelta(days=0,hours=0,minutes=0,seconds=3)

def state_func(new_datetime,old_datetime,last_state):
    new_day=new_datetime.day
    new_hour=new_datetime.hour
    new_minute=new_datetime.minute
    old_day=old_datetime.day
    old_hour=old_datetime.hour
    old_minute=old_datetime.minute
    if new_day==old_day:   # si es el mismo dia
        delta_hour=new_hour-old_hour
        delta_minute=new_minute-old_minute
        if delta_minute<0:
            delta_minute = delta_minute+60
        if delta_hour<12:   # han pasado menos de 12 horas
           if delta_hour>1:  # ha pasado al menos 1 hora cambia estados
                if last_state==0:
                    state_acc=1
                else:
                    state_acc =0
           elif delta_minute>5: # ha pasado al menos 5 minutos cambia estados
                if last_state == 0:
                  state_acc = 1
                else:
                  state_acc = 0
           else: # ha pasado menos de 5 minutos (DOBLE FICHAJE), nuevo estado igual al anterior
                state_acc=last_state
        else:
          state_acc = last_state  # pasaron mas de 12 horas, nuevo estado igual al anterior
    else:
        state_acc=last_state  # paso mas de 1 dia, nuevo estado igual al anterior

    return state_acc

last_state=0
new_state=state_func(new_datetime,old_datetime,last_state)
print("old state is ",last_state," new state is ", new_state)