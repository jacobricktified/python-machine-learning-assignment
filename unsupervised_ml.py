
# unsupervised_ml.py

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Prepare the customer dataset
# Columns: Monthly spending (KES), Monthly visits

X = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]

# 2. Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Create the K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 4. Train the model and assign clusters
model.fit(X_scaled)
predictions = model.predict(X_scaled)

# 5. Display each customer's cluster
print("CUSTOMER CLUSTER ASSIGNMENTS")
print("----------------------------")

for i, cluster in enumerate(predictions):
    print(f"Customer {i + 1} belongs to Cluster {cluster}")

# 6. Count customers in each cluster
print("\nTOTAL CUSTOMERS IN EACH CLUSTER")
print("--------------------------------")

for cluster in range(3):
    count = sum(predictions == cluster)
    print(f"Cluster {cluster}: {count} customers")

# 7. Bonus: Plot customer groups
for cluster in range(3):
    cluster_points = [
        X[i] for i in range(len(X))
        if predictions[i] == cluster
    ]

    if cluster_points:
        plt.scatter(
            [point[0] for point in cluster_points],
            [point[1] for point in cluster_points],
            label=f"Cluster {cluster}"
        )

# Show cluster centres in original units
centres = scaler.inverse_transform(model.cluster_centers_)

plt.scatter(
    centres[:, 0],
    centres[:, 1],
    marker="X",
    s=200,
    color="black",
    label="Cluster centres"
)

plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.title("Customer Segmentation Using K-Means")
plt.legend()
plt.grid(True)
plt.show()
