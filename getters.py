import json
import requests

class DEXPrices:
        def __init__(self, api_address="http://127.0.0.1:8081/get_price/", custom=False, 
                     pool_address=None, asset_in=None, asset_out=None, amount=None):
            self.api_address = api_address
            
            self.custom = custom

            self.pool_address = pool_address
            self.asset_in = asset_in
            self.asset_out = asset_out
            self.amount = amount
            
        def logPostRequest(self, body):
            response = requests.post(self.api_address, data=json.dumps(body), headers={"Authorization": "Bearer !!PublicTests!!"}).json()
            print(response)
        
        def getDedust(self):
            
            dedustPostBody = {"pool_address": self.pool_address, "custom": self.custom, "dex": "dedust"}
            if self.custom == True:
                dedustPostBody = {"pool_address": self.pool_address, "custom": self.custom,
                    "custom_settings": { "amount": self.amount, "asset_in": self.asset_in},
                    "dex": "dedust"
                }
                
            self.logPostRequest(dedustPostBody)
            
        def getStonfi(self):

            stonfiPOstBody = {"asset_out": self.asset_out, "custom": self.custom,"dex": "stonfi"}
            if self.custom == True:
                stonfiPOstBody = {"asset_out": self.asset_out,"custom": self.custom,
                    "custom_settings": {"amount": self.amount,"asset_in": self.asset_in},
                    "dex": "stonfi"
                }
            self.logPostRequest(stonfiPOstBody)
            
     
print("[ deDust ]: 123 TONNEL to VIRUS")       
dedustObj = DEXPrices(
            custom=True, 
            asset_in="EQDNDv54v_TEU5t26rFykylsdPQsv5nsSZaH_v7JSJPtMitv",    # TONNEL JETTON MASTER ADDRESS
            amount=123 * 10**9,                                             # AMOINT OF TONNELS WITH DECIMALS
            
            pool_address="EQDuq089U7fWJtKTHRxk6UwRmBl95yrBM9JiWRfUKXqwd5rW" # TONNEL/VIRUS POOL ADDRESS

)
dedustObj.getDedust()

print("[ stonFi ]: 123 DOGS to USDT")
stonfiObj = DEXPrices(
            custom=True, 
            asset_in="EQDNDv54v_TEU5t26rFykylsdPQsv5nsSZaH_v7JSJPtMitv",  # DOGS JETTON MASTER ADDRESS
            amount=123 * 10**9,                                           # AMOUNT OF DOGS WITH DECIMALS
            
            asset_out="EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs", # USDT JETTON MASTER ADDRESS
)    
stonfiObj.getStonfi()





