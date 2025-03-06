import base64
import zlib

# encoded_str_3 = "eJw9jlGOAiEQRK9i+N52BgWG8TKmB2gl6wCBVmOMd9+wuvtZr+ol9RTn3FgcNuLMXNphGAreLjnFB4Lcxvidt5EH8bURl3yKqQ9PgdcYk++wYGv3XH3nUsmdknsle1FDY7xWTHyMv63W3spl9uBG7UFRILAGCZZpJOuNtE5TF30oWHkN/yLtlJosIaDfB1DGTICz1kCjXAin2bkZu+jyWjA9PpbpqAVXAx//Dr6jeP0AoyxJrg=="
encoded_str_3 ='eyJob3N0IjogImh0dHBzOi8vcGF2bG9uaXlhLTEuaWlrby5pdC8iLCAibG9naW4iOiAiZ2V0bWlpbmQiLCAicGFzc3dvcmQiOiAiMTQxMjQxMzQxIiwgInJlc3RhdXJhbnRfaWQiOiAiZGE4MzhlY2MtOTEyNy00ZTE5LWE2Y2MtZTA4MDI1NDg4OGE5IiwgImRlcGFydG1lbnRfaWQiOiAiZjI0NDc4ZmEtYWQzZS00NjY3LWE5NTUtZjAxYmZhNzljYzlhIiwgImNvbXBhbnlfaWQiOiAiNiIsICJzZWNyZXRfd29yZCI6ICJzZWNyZXQifQ=='
# Декодирование Base64 и попытка распаковки
try:
    decoded_bytes_3 = base64.b64decode(encoded_str_3)
    try:
        decompressed_data_3 = zlib.decompress(decoded_bytes_3)
        result_3 = decompressed_data_3.decode('utf-8', errors='ignore')
    except zlib.error:
        result_3 = decoded_bytes_3.decode('utf-8', errors='ignore')
except Exception as e:
    result_3 = f"Ошибка декодирования: {e}"

print(result_3)