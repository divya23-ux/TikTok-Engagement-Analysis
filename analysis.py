import pandas as pd

df = pd.read_csv("data/tiktok_data.csv")

print(df)

print("\nData types:")
print(df.dtypes)

df["engagement_rate"] = (
    (df["likes"] + df["comments"] + df["shares"] + df["saved"])
    / df["views"]
) * 100

print("\nEngagement rates:")
print(df[["video_id", "views", "engagement_rate"]])

import matplotlib.pyplot as plt

plt.scatter(df["views"], df["engagement_rate"])

plt.xlabel("Views")
plt.ylabel("Engagement Rate (%)")
plt.title("Views vs Engagement Rate")

plt.show()

plt.figure(figsize=(10, 5))

plt.bar(df["video_id"], df["engagement_rate"])

plt.xlabel("Video")
plt.ylabel("Engagement Rate (%)")
plt.title("Engagement Rate by Video")

plt.xticks(df["video_id"])

plt.show()

# Convert posting time into a time value
df["time_posted"] = pd.to_datetime(df["time_posted"], format="%H:%M")

# Extract the hour
df["posting_hour"] = df["time_posted"].dt.hour

print("\nPosting hours:")
print(df[["video_id", "time_posted", "posting_hour", "engagement_rate"]])
