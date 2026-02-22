# ライブラリ読み込み
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Hiragino Sans" # フォントを指定しないと文字化けになります

# CSVファイル読み込み
csv_path = "sales_data_sample.csv" # 同じフォルダに置く
data = pd.read_csv(csv_path)

# それぞれ陳列位置のアイコンの形状
icon_shapes = {
    1: "o",   # ○
    2: "^",   # △
    3: "s",   # □
    4: "D"    # ◆
}
# それぞれ陳列位置のアイコンの意味
icon_locations = {
    1: "入口付近",
    2: "主通路の中段付近",
    3: "売場奥",
    4: "エレベータ付近"
}

# プロットのパラメータ（固定値）
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
# プロット
for pos in data["display_position"].unique():
    subset = data[data["display_position"] == pos]
    ax.scatter(
        subset["stay_time"],                   # X：商品前での滞在時間（秒）
        subset["customers"],                   # Y：来店客数（人）
        subset["sales"],                       # Z：販売数（個）
        s=subset["minutes_after_restock"] * 5, # サイズ：補充後経過時間
        marker=icon_shapes[pos],               # 形状：陳列位置
        alpha=0.7,
        label=icon_locations[pos]
    )

# X・Y・Z軸のラベル(説明文字)
ax.set_xlabel("商品前での滞在時間（秒）")
ax.set_ylabel("来店客数（人）")
ax.set_zlabel("販売数（個）")
# タイトル下の点の大きさの説明文
ax.text2D(
    0.25, # 0~1　わからないけど0.25はちょうど真ん中Σ੧(❛□❛✿)
    0.97, # 0~1　大きいほどトップに近い
    "※点が大きいほど補充後の経過時間が長い",
    transform=ax.transAxes,
    fontsize=10,
    color="red"
)
# legendのタイトル（中身はforの「label=」に設定済）
ax.legend(title="陳列位置")
# タイトル
plt.title("商品「XXX」の販売分析")
plt.show()
