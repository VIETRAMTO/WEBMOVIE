import pandas as pd

# Đọc file CSV
file_path = "movies_list.csv"  # Thay thế bằng đường dẫn file CSV của bạn
df = pd.read_csv(file_path)

# Danh sách link YouTube
youtube_links = [
    "Qx7aEV_a6r0",
    "https://youtu.be/mTH4qIBDDV0",
    "https://youtu.be/9hFWutGWs54",
    "https://youtu.be/raJ8CXRs5O8",
    "https://youtu.be/G_angLL4FeE",
    "https://youtu.be/dmd7h5p2cp8",
    "https://youtu.be/U9us98iOgEs",
    "https://youtu.be/DoLAsMXxGxw",
    "https://youtu.be/xzglePk2zAo",
    "https://youtu.be/iPrvA79tfyE",
    "https://youtu.be/hFXy9nhfUnw",
    "https://youtu.be/TPpO-zqqUH0",
    "https://youtu.be/AdTeAIkV3KQ",
    "https://youtu.be/fmLGhAPmC1c",
    "https://youtu.be/miGSyGPS0XE",
    "https://youtu.be/hrUJ3JZ1EMI",
    "https://youtu.be/-Y9IxI68pdg",
    "https://youtu.be/xad5r0VMX2E",
    "https://youtu.be/pYLtQE8u9Ds",
    "https://youtu.be/eOnkSpCjUQ4",
    "https://youtu.be/vKePaSJ77co",
    "https://youtu.be/YtABAX64-7c",
    "https://youtu.be/_0c_ntgknYA",
    "https://youtu.be/OfFztWdzCis",
    "https://youtu.be/OfFztWdzCis",
    "https://youtu.be/nLtEk7QHRCY",
    "https://youtu.be/9jofVA1CLP8",
    "https://youtu.be/Yh_jxdv8NFs",
    "https://youtu.be/KAjBvQ2Ow80?t=1",
    "https://youtu.be/yxOWJ6dGQDQ",
    "https://youtu.be/SyrbVsAvY-I",
    "https://youtu.be/VZQmj6bH5cY",
    "https://youtu.be/ozwywy1eeXs",
    "https://youtu.be/_jDrjF7TyZQ",
    "https://youtu.be/4q2dd0Nc8sk",
    "https://youtu.be/Lhsg1DPp9No",
    "https://youtu.be/PAoxB1Yhv0I",
    "https://youtu.be/ySTdWAFPsNU",
    "https://youtu.be/u2NeUbZXd4A",
    "https://youtu.be/IZs3R7VrY6Q"
]

# Kiểm tra nếu số lượng link ít hơn số dòng trong CSV, điền NaN cho các dòng thừa
while len(youtube_links) < len(df):
    youtube_links.append(None)  # Thêm giá trị rỗng nếu cần

# Thêm cột "link vid" vào DataFrame
df["link vid"] = youtube_links[:len(df)]

# Ghi lại file CSV
df.to_csv(file_path, index=False)

print("✔ Đã thêm cột 'link vid' vào file CSV thành công!")
