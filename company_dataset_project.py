import pandas as pd

df = pd.read_csv("sales_data.csv" , encoding = "Latin1")
# print(df.isnull().sum())

df["Product"].fillna(df["Product"].mode()[0], inplace=True)
# print(df.isnull().sum())

df["Region"].fillna(df["Region"].mode()[0] , inplace=True)
# print(df.isnull().sum())

df["Payment_Mode"].fillna(df["Payment_Mode"].mode()[0] , inplace=True)
# print(df.isnull().sum())

# Fill missing Category values with mode
df["Category"].fillna(df["Category"].mode()[0], inplace=True)
# print(df.isnull().sum())


df["Date"] = pd.to_datetime(df["Date"])

df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)

region_total = df.groupby("Region")["Total_Sales"].mean().sort_values(ascending=False)
# print(region_total)

best_region = region_total.idxmax()
worst_region = region_total.idxmin()
best_value = region_total.max()

# print(f"The best region is {best_region} and average value per sale is {best_value:.2f}")

product_total = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

best_product = product_total.idxmax()
best_product_price = product_total.max()
worst_product = product_total.idxmin()
worst_product_price = product_total.min()

# print(f"The best product is {best_product} with price {best_product_price:.2f} and the worst product is {worst_product} with price {worst_product_price:.2f}")

catagory_total = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

best_catag = catagory_total.idxmax()
worst_catag = catagory_total.idxmin()

# print(f"The best catagory is {best_catag} and the worst catagory is {worst_catag}")

monthly_total = df.groupby("Month")["Total_Sales"].sum().sort_values(ascending=False)
best_month = monthly_total.idxmax()
worst_month = monthly_total.idxmin()

# print(f"The best month is {best_month} and the worst month is {worst_month}")


summary = (
    f"Best region is  {best_region} region. \n"
    f"Your highest performing product is {best_product} \n"
    f"Best category is {best_catag} catagory. \n"
    f"Your highest performing month is month no. {best_month} \n"
)

print(summary)
print("-----------------------------------------")
worst_message = (
    f"Focus more on {worst_region} region. \n"
    f"Make good strategies on {worst_product} \n"
    f"Maintain {worst_catag} catagory. \n"
    f"Make good schemes for month no. {worst_month}\n"
)
print(worst_message)


# saving files to CSV
final_data = {
    "Summary" : [summary],
    "Advice" : [worst_message]
}

final_df = pd.DataFrame(final_data)

df.to_csv("sales_data_cleaned.csv" , index = False , encoding="utf-8")
final_df.to_csv("sales_summary.csv", index=False, encoding="utf-8")
print("Data saving to CSV...")