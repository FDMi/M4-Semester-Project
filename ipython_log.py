# IPython log file

runcell(1, 'C:/Users/kesut/.spyder-py3/Sentiment analysis.py')
runcell(2, 'C:/Users/kesut/.spyder-py3/Sentiment analysis.py')
runcell(3, 'C:/Users/kesut/.spyder-py3/Sentiment analysis.py')
data
#[Out]#                              time            id  ... likecount retweetcount
#[Out]# 0       2021-04-26 23:59:39+00:00  1.390000e+18  ...         3            0
#[Out]# 1       2021-04-26 23:59:35+00:00  1.390000e+18  ...         1            0
#[Out]# 2       2021-04-26 23:59:24+00:00  1.390000e+18  ...         1            0
#[Out]# 3       2021-04-26 23:58:18+00:00  1.390000e+18  ...         6            0
#[Out]# 4       2021-04-26 23:57:55+00:00  1.390000e+18  ...         0            0
#[Out]# ...                           ...           ...  ...       ...          ...
#[Out]# 372371  2020-01-01 05:59:21+00:00  1.210000e+18  ...         0            0
#[Out]# 372372  2020-01-01 05:17:20+00:00  1.210000e+18  ...         0            0
#[Out]# 372373  2020-01-01 04:55:47+00:00  1.210000e+18  ...         1            0
#[Out]# 372374  2020-01-01 04:55:37+00:00  1.210000e+18  ...         0            0
#[Out]# 372375  2020-01-01 01:41:19+00:00  1.210000e+18  ...         1            0
#[Out]# 
#[Out]# [372376 rows x 7 columns]
data["body"][7]
#[Out]# 'Pixelated Dreams NFT #10! 🎨🌈✌ @pixelateddream5  \n\nhttps://t.co/z36yQuD6TD\n\n#nft #nfts #nftcommunity #nftdrop #nftart #nftartist #crypto #cryptoart #cryptoartist #cryptocurrency #blockchain #blockchainart #blockchainartist #ethereum #opensea'
import pandas as pd
data = pd.read_csv(r"C:\Users\kesut\Desktop\cleaned.csv")
data.info()
data.loc[:,"Datetime_updated"]
#[Out]# 0          2018-03-01 00:00:00
#[Out]# 1          2018-03-01 00:00:00
#[Out]# 2          2018-02-28 00:00:00
#[Out]# 3          2018-02-28 00:00:00
#[Out]# 4          2018-02-28 00:00:00
#[Out]#                   ...         
#[Out]# 1443610    2021-04-01 00:00:00
#[Out]# 1443611    2021-04-01 00:00:00
#[Out]# 1443612    2021-04-01 00:00:00
#[Out]# 1443613    2021-04-01 00:00:00
#[Out]# 1443614    2021-04-01 00:00:00
#[Out]# Name: Datetime_updated, Length: 1443615, dtype: object
data["Datetime_updated"] = pd.to_datetime(data.Datetime_updated)
data.sort_values(by=["Datetime_updated"], inplace=True, ascending=True)
data
#[Out]#                                      Seller_address  ...     Category
#[Out]# 5611     0xa77c4fe17cfd86a499ade6ecc8b3bee2f698c8e0  ...  Collectible
#[Out]# 5610     0x53ec525b9df849be99263311f5b7f9fd6cfebea6  ...  Collectible
#[Out]# 5609     0x7494eb2916cad8649f4f91eb1db6e20be605dad6  ...  Collectible
#[Out]# 5608     0xa2381223639181689cd6c46d38a1a4884bb6d83c  ...  Collectible
#[Out]# 5607     0x8ad7e433f00fbb22ae23f8eda8aadd359d411cf4  ...  Collectible
#[Out]# ...                                             ...  ...          ...
#[Out]# 1328401  0xa2516ac5233acdadc31bcffc771609f020378a82  ...        Games
#[Out]# 1328400  0x7615d86d003cc20ac3de1cbbe47b5375c47048b5  ...  Collectible
#[Out]# 1328399  0x327305a797d92a39cee1a225d7e2a1cc42b1a8fa  ...  Collectible
#[Out]# 1328410  0x7cabb73f5b840b245ec2528751445da1f6dd7eee  ...          Art
#[Out]# 1328722  0x327305a797d92a39cee1a225d7e2a1cc42b1a8fa  ...  Collectible
#[Out]# 
#[Out]# [1443615 rows x 9 columns]
