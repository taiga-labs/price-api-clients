import json
import httpx
import argparse


"""
EXAMPLE:

python3 sse.py \
    --token "!!PublicTests!!" \
    --trigger_perc "0.01" \
    --dex_name "dedust" \
    --asset_in "TON" \
    --asset_out "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs" \
    --pool_address "EQA-X_yo3fzzbDbJ_0bzFWKqtRuZFIRa1sJsveZJ1YpViO3r"
    
    
python3 sse.py \
    --token "!!PublicTests!!" \
    --trigger_perc "0.01" \
    --dex_name "dedust" \
    --asset_in "TON" \
    --asset_out "EQBYnUrIlwBrWqp_rl-VxeSBvTR2VmTfC4ManQ657n_BUILD" \
    --pool_address "EQCm0PCt-WNMWChT4MaMeIJzmg6boIwLPja3BxGZP8ijhRxZ"
"""

class SSEClient:
    def __init__(self, api_address="http://80.90.187.242:7979", timeout=None):
        self.api_address = api_address
        self.timeout = timeout or httpx.Timeout(
            connect=10.0,
            read=None,
            write=10.0,
            pool=60.0
        )

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="SSE клиент")
        parser.add_argument("--token",        required=True, help="Токен авторизации.")
        parser.add_argument("--trigger_perc", required=True, help="Ценовое изменение для триггера уведомления клиенту в процентах (дробная часть числа отделяется точкой).")
        parser.add_argument("--dex_name",     required=True, help="Название DEX.")
        parser.add_argument("--asset_in",     required=True, help="Адрес актива, цену за который будем получать.")
        parser.add_argument("--asset_out",    required=True, help="Адрес актива, цену в котором будем получать.")
        parser.add_argument("--pool_address", required=True, help="Адрес пула.")
        return parser.parse_args()

    def print_sse_event(self, sse_data):
        curr_price = sse_data.get('curr_price')
        changed_perc = sse_data.get('changed_perc')
        print(f"[ \033[0;35mPRICE UPDATE\033[0m ] price={curr_price}, changed={changed_perc}")

    def listen_sse(self, trigger_perc, dex_name, asset_in, asset_out, pool_address, token):
        sse_endpoint_url = f"{self.api_address}/subscribe"

        headers = {
            "Content-Type":  "application/json",
            "trigger_perc":  trigger_perc,
            "dex_name":      dex_name,
            "asset_in":      asset_in,
            "asset_out":     asset_out,
            "pool_address":  pool_address,
            "Authorization": f"Bearer {token}"
        }

        print(f"Подключение к SSE-эндпоинту: {sse_endpoint_url}")
        print(f"Параметры запроса (заголовки): {headers}")

        try:
            with httpx.Client(timeout=self.timeout) as client:
                with client.stream("GET", sse_endpoint_url, headers=headers) as response:
                    response.raise_for_status()

                    event_type = None
                    event_data = None
                    for raw_line in response.iter_lines():
                        line = raw_line.strip() if raw_line else ""
                        if line.startswith("event:"):
                            event_type = line.split(":", 1)[1].strip()
                        elif line.startswith("data:"):
                            event_data = line.split(":", 1)[1].strip()
                        elif line == "":
                            if event_type == "price_update" and event_data:
                                try:
                                    sse_data = json.loads(event_data)
                                    self.print_sse_event(sse_data)
                                except json.JSONDecodeError as e:
                                    print(f"JSON parsing error: {e}")
                            event_type = None
                            event_data = None

        except Exception as e:
            print(f"SSE error: {e}")


def main():
    args = SSEClient.parse_arguments()

    client = SSEClient()

    client.listen_sse(
        trigger_perc=args.trigger_perc,
        dex_name=args.dex_name,
        asset_in=args.asset_in,
        asset_out=args.asset_out,
        pool_address=args.pool_address,
        token=args.token,
    )

if __name__ == "__main__":
    main()