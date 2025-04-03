import pandas as pd

# Đọc file CSV
file_path = "movies_list.csv"  # Thay thế bằng đường dẫn file CSV của bạn
df = pd.read_csv(file_path)

# Danh sách link YouTube
youtube_links = [
    "Qx7aEV_a6r0",
    "mTH4qIBDDV0",
    "9hFWutGWs54",
    "raJ8CXRs5O8",
    "G_angLL4FeE",
    "U9us98iOgEs",
    "DoLAsMXxGxw",
    "xzglePk2zAo",
    "iPrvA79tfyE",
    "hFXy9nhfUnw",
    "TPpO-zqqUH0",
    "AdTeAIkV3KQ",
    "fmLGhAPmC1c",
    "miGSyGPS0XE",
    "hrUJ3JZ1EMI",
    "-Y9IxI68pdg",
    "xad5r0VMX2E",
    "pYLtQE8u9Ds",
    "eOnkSpCjUQ4",
    "vKePaSJ77co",
    "YtABAX64-7c",
    "_0c_ntgknYA",
    "OfFztWdzCis",
    "OfFztWdzCis",
    "nLtEk7QHRCY",
    "9jofVA1CLP8",
    "Yh_jxdv8NFs",
    "KAjBvQ2Ow80",
    "yxOWJ6dGQDQ",
    "VZQmj6bH5cY",
    "ozwywy1eeXs",
    "_jDrjF7TyZQ",
    "4q2dd0Nc8sk",
    "Lhsg1DPp9No",
    "PAoxB1Yhv0I",
    "ySTdWAFPsNU",
    "u2NeUbZXd4A",
    "IZs3R7VrY6Q"
]



# Kiểm tra nếu số lượng link ít hơn số dòng trong CSV, điền NaN cho các dòng thừa
while len(youtube_links) < len(df):
    youtube_links.append(None)  # Thêm giá trị rỗng nếu cần

# Thêm cột "link vid" vào DataFrame
df["link vid"] = youtube_links[:len(df)]

# Ghi lại file CSV
df.to_csv(file_path, index=False)

print("✔ Đã thêm cột 'link vid' vào file CSV thành công!")
