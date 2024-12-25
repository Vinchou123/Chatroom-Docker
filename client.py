import asyncio
from aioconsole import ainput

async def async_input(writer):
    try:
        while True:
            user_input = await ainput("\rVous : ")
            if user_input.strip():
                writer.write(user_input.encode())
                await writer.drain()
    except asyncio.CancelledError:
        print("\nArrêt de la saisie utilisateur.")

async def async_receive(reader):
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                print("\nConnexion avec le serveur fermée.")
                break
            print(f"\rServeur : {data.decode()}\n", end="")
            print("\rVous : ", end="", flush=True)
    except asyncio.CancelledError:
        print("\nArrêt de la réception des messages.")

async def main():
    host = "localhost"
    port = 8888

    try:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"Connecté au serveur {host}:{port}")

        tasks = [
            asyncio.create_task(async_input(writer)),
            asyncio.create_task(async_receive(reader))
        ]

        await asyncio.gather(*tasks)
    except ConnectionRefusedError:
        print(f"Impossible de se connecter au serveur {host}:{port}")
    except asyncio.CancelledError:
        print("\nClient arrêté par l'utilisateur.")
    finally:
        print("Fermeture de la connexion.")
        if writer:
            writer.close()
            await writer.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt du client (CTRL + C).")
