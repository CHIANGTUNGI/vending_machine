# 商品リストと価格の辞書
items = {
    "お茶": 100,
    "水": 100,
    "ジュース": 150,
    "コーヒー": 120
}

# 自動販売機のクラス
class VendingMachine:
    def __init__(self):
        self.total_amount = 0

    # 商品を選択して金額を加算するメソッド
    def select_item(self, item):
        if item in items:
            self.total_amount += items[item]
        else:
            print("無効な商品です。")

    # 商品の購入可否を判定するメソッド
    def can_purchase(self):
        if self.total_amount >= 120:
            return True
        else:
            return False

# 自動販売機のインスタンスを作成
vending_machine = VendingMachine()

# 商品を選択して金額を加算
vending_machine.select_item("お茶")
vending_machine.select_item("コーヒー")

# 購入可否を判定
if vending_machine.can_purchase():
    print("商品を購入できます。")
else:
    print("購入金額が不足しています。")

