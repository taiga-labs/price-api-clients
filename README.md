# price-api

# SSE DOCS

в sse.py пример есть пример подключения к SSE серверу 
параметры передаются в headers HTTP GET запроса

```
   --token "!!PublicTests!!" \
   --trigger_perc "0.0001" \
   --dex_name "dedust" \
   --asset_in "TON" \
   --asset_out "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs" \
   --pool_address "EQA-X_yo3fzzbDbJ_0bzFWKqtRuZFIRa1sJsveZJ1YpViO3r"
```

в sse.py также есть и описание каждого из параметров

# API DOCS

Tакже можно запрашивать цену с DeDust или StonFi

## DeDust example

В случае с DeDust нам нужен адрес пула

123 TONNEL to VIRUS

1) - DEX: dedust
2) - TONNEL/VIRUS dedust pool address: EQDuq089U7fWJtKTHRxk6UwRmBl95yrBM9JiWRfUKXqwd5rW 
3) - TONNEL master address, asset it, because we exchange TONNEL: EQDNDv54v_TEU5t26rFykylsdPQsv5nsSZaH_v7JSJPtMitv

```json
{
  "pool_address": "EQDuq089U7fWJtKTHRxk6UwRmBl95yrBM9JiWRfUKXqwd5rW", 
  "custom": true,
  "custom_settings": {
    "amount": 123000000000,
    "asset_in": "EQDNDv54v_TEU5t26rFykylsdPQsv5nsSZaH_v7JSJPtMitv"
  },
  "dex": "dedust"
}
```

## StonFi example

В случае с StonFi нам нужен адрес жетона, НА который меняем, то есть цену в котором хотим получить

123 DOGS to USDT

1) - DEX: stonfi
2) - DOGS master address, asset it, because we exchange DOGS: EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS
3) - USD₮ master address, asset it, because we recieve USD₮: EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs

```json
{
  "asset_out": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
  "custom": true,
  "custom_settings": {
    "amount": 123000000000,
    "asset_in": "EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS"
  },
  "dex": "stonfi"
}
```

## Если в пуле есть TON и мы хотим получить цену в Jetton за один TON (Without custom settings)

### DeDust

1 TON to USD₮

1) - pool_address - адрес пула, активы которого нас интересуют

```json
{
  "pool_address": "EQA-X_yo3fzzbDbJ_0bzFWKqtRuZFIRa1sJsveZJ1YpViO3r",
  "custom": false,
  "dex": "dedust"
}
```

### StonFi

1 TON to USD₮

1) - asset_out - адрес Jetton мастера жеттона, цену в котором хотим получить(т.е в случае 'ленивым' запросом в пуле с TON - просто адрес жетон мастера жетона, который есть в пуле помимо TON)

```json
{
  "asset_out": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
  "custom": false,
  "dex": "stonfi"
}
```

