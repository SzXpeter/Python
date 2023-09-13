pizza_ar = 4990
cola_ar = 499

egyenleg = 20000


pizza_db = int(input("Mennyi pizzát szeretne: "))
pizza_ossz_ar = pizza_ar * pizza_db


if pizza_ossz_ar > egyenleg:
    print("Nincs elég pénze!")
else:
    cola_db = int(input("Szeretne valami üdítőt is: "))
    cola_ossz_ar = cola_ar * cola_db
    if cola_ossz_ar + pizza_ossz_ar > egyenleg:
        print("Nincs elég pénze!")
    else:
        print(f"Itt a visszajáró: {egyenleg - cola_ossz_ar - pizza_ossz_ar}, itt vannak az üdítők és ha kész a pizza szólunk") 
